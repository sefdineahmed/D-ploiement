import os
import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
import plotly.express as px
from PIL import Image
from lifelines import CoxPHFitter
from tensorflow.keras.models import load_model as tf_load_model

# ----------------------------------------------------------
# Configuration de l'application
# ----------------------------------------------------------
st.set_page_config(
    page_title="OncoSuite - Cancer Gastrique",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chemins vers les ressources
DATA_PATH = "data/GastricCancerData.xlsx"
LOGO_PATH = "assets/header.jpg"
TEAM_IMG_PATH = "assets/team.jpg"

# Configuration des modèles
MODELS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib",
    "DeepSurv": "models/deepsurv.keras",
    "GBST": "models/gbst.joblib"
}

# Configuration des variables (catégorielles -> Oui/Non)
FEATURE_CONFIG = {
    "Cardiopathie": "Cardiopathie",
    "Ulceregastrique": "Ulcère gastrique",
    "Douleurepigastrique": "Douleur épigastrique",
    "Ulcero-bourgeonnant": "Lésion ulcéro-bourgeonnante",
    "Denitrution": "Dénutrition",
    "Tabac": "Tabagisme actif",
    "Mucineux": "Type mucineux",
    "Infiltrant": "Type infiltrant",
    "Stenosant": "Type sténosant",
    "Metastases": "Métastases",
    "Adenopathie": "Adénopathie",
    "AGE": "Âge",
}

# ----------------------------------------------------------
# Fonctions Utilitaires
# ----------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_data():
    """Charge les données depuis le fichier Excel."""
    if os.path.exists(DATA_PATH):
        return pd.read_excel(DATA_PATH)
    else:
        st.error(f"❌ Fichier introuvable : {DATA_PATH}")
        return pd.DataFrame()

@st.cache_resource(show_spinner=False)
def load_model(model_path):
    """
    Charge un modèle pré-entraîné.
    Pour les modèles Keras (.keras) on utilise tf.keras.models.load_model avec les custom_objects.
    Pour les autres modèles, on utilise joblib.load.
    Pour le modèle RSF, on applique un monkey patch pour éviter l'erreur liée à get_tags.
    """
    if not os.path.exists(model_path):
        st.error(f"❌ Modèle introuvable : {model_path}")
        return None

    try:
        _, ext = os.path.splitext(model_path)
        # Correction spécifique pour RSF : patch pour get_tags si besoin
        if "rsf" in model_path.lower():
            try:
                from sklearn.utils._tags import get_tags
            except ImportError:
                # Si get_tags n'existe pas, on définit un stub minimal
                def get_tags(estimator):
                    return {}
                import sklearn.utils._tags as sk_tags
                sk_tags.get_tags = get_tags

        if ext in ['.keras', '.h5']:
            # Pour les modèles Keras, on peut avoir besoin d'une fonction de perte personnalisée
            # Ici, on définit une fonction cox_loss minimaliste si nécessaire
            def cox_loss(y_true, y_pred):
                event = tf.cast(y_true[:, 0], dtype=tf.float32)
                risk = y_pred[:, 0]
                log_risk = tf.math.log(tf.cumsum(tf.exp(risk), reverse=True))
                loss = -tf.reduce_mean((risk - log_risk) * event)
                return loss
            return tf_load_model(model_path, custom_objects={"cox_loss": cox_loss})
        else:
            return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {e}")
        return None

def encode_features(inputs):
    """
    Encode les variables catégorielles en format numérique (0/1).
    Chaque entrée "Oui" devient 1, "Non" devient 0.
    """
    return pd.DataFrame({k: [1 if v.upper() == "OUI" else 0] for k, v in inputs.items()})

def predict_survival(model, data, model_name):
    """
    Effectue la prédiction du temps de survie selon le type de modèle.
    Pour CoxPHFitter, on utilise predict_median.
    Pour les autres modèles, on suppose que la méthode predict retourne un array numpy.
    """
    # Cas pour CoxPHFitter (Cox PH)
    if hasattr(model, "predict_median"):
        pred = model.predict_median(data)
        # Si la prédiction est une Series ou un DataFrame, on prend la première valeur
        if hasattr(pred, '__iter__'):
            return pred.iloc[0] if isinstance(pred, pd.Series) else pred[0]
        return pred

    # Cas pour RSF, GBST ou DeepSurv
    elif hasattr(model, "predict"):
        prediction = model.predict(data)
        # Pour DeepSurv, la prédiction est souvent un tableau 2D
        if isinstance(prediction, np.ndarray):
            if prediction.ndim == 2:
                return prediction[0][0]
            return prediction[0]
        return prediction
    else:
        raise ValueError(f"Le modèle {model_name} ne supporte pas la prédiction de survie.")

def clean_prediction(prediction, model_name):
    """
    Nettoie la prédiction pour éviter les valeurs négatives et renvoie la valeur ajustée.
    """
    # Pour Cox PH et RSF, on retourne la valeur maximale entre la prédiction et 0
    if model_name in ["Cox PH", "RSF", "GBST"]:
        return max(prediction, 0)
    # Pour DeepSurv, on s'assure que la prédiction est au moins 1 (par exemple 1 mois)
    elif model_name == "DeepSurv":
        return max(prediction, 1)
    else:
        return prediction

# ----------------------------------------------------------
# Définition des Pages
# ----------------------------------------------------------
def accueil():
    col1, col2 = st.columns([1, 3])
    with col1:
        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, width=200)
    with col2:
        st.title("⚕️ Plateforme d'Aide à la Décision")
        st.markdown("**Estimation du temps de survie post-traitement du cancer gastrique**")
    st.markdown("---")
    st.write(
        """
    ### Fonctionnalités principales :
    - 📊 Exploration interactive des données cliniques
    - 📈 Analyse statistique descriptive
    - 🤖 Prédiction multi-modèles de survie
    - 📤 Export des résultats cliniques
    """
    )

def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    if df.empty:
        return

    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(5))
        st.write(f"Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Distribution des variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var, color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌡 Matrice de corrélation")
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r', labels={"color": "Corrélation"})
        st.plotly_chart(fig, use_container_width=True)

def modelisation():
    st.title("🤖 Prédiction de Survie")
    
    with st.expander("📋 Paramètres du patient", expanded=True):
        inputs = {}
        cols = st.columns(3)
        for i, (feature, label) in enumerate(FEATURE_CONFIG.items()):
            with cols[i % 3]:
                inputs[feature] = st.selectbox(label, options=["Non", "Oui"], key=feature)
    
    input_df = encode_features(inputs)
    st.markdown("---")
    
    # Vérifier que toutes les colonnes sont présentes
    missing_columns = [col for col in FEATURE_CONFIG.keys() if col not in input_df.columns]
    if missing_columns:
        st.error(f"❌ Colonnes manquantes : {', '.join(missing_columns)}")
        return
    
    model_name = st.selectbox("Choisir un modèle", list(MODELS.keys()))
    model = load_model(MODELS[model_name])
    
    if st.button("Prédire le temps de survie"):
        if model:
            try:
                # Pour le modèle Cox PH, s'assurer que les colonnes utilisées correspondent
                if model_name == "Cox PH" and hasattr(model, "params_"):
                    cols_to_use = list(model.params_.index) if hasattr(model.params_.index, '__iter__') else input_df.columns
                    input_df = input_df[cols_to_use]
                pred = predict_survival(model, input_df, model_name)
                cleaned_pred = clean_prediction(pred, model_name)
                st.metric(label="Survie médiane estimée", value=f"{cleaned_pred:.1f} mois")
                
                # Visualisation optionnelle : courbe de survie
                months = min(int(cleaned_pred), 120)
                fig = px.line(
                    x=list(range(months)),
                    y=[100 - (i / months) * 100 for i in range(months)],
                    labels={"x": "Mois", "y": "Probabilité de survie (%)"},
                    color_discrete_sequence=['#2ca02c']
                )
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"❌ Erreur de prédiction pour {model_name} : {e}")

def a_propos():
    st.title("📚 À Propos")
    cols = st.columns([1, 3])
    with cols[0]:
        if os.path.exists(TEAM_IMG_PATH):
            st.image(TEAM_IMG_PATH, width=150)
    with cols[1]:
        st.markdown(
            """
        ### Équipe  
        - **👨‍🏫 Pr. Aba Diop** - Maître de Conférences (UAD Bambey)  
        - **🎓 PhD. Idrissa Sy** - PhD en Statistiques (UAD Bambey)  
        - **💻 M. Ahmed Sefdine** - Data Scientist  

        Ce projet est développé dans le cadre d'une **recherche clinique** sur le cancer de l'estomac.  
        Il permet de prédire le **temps de survie des patients** après leur traitement, en utilisant des modèles avancés de survie.  
        """
        )

def contact():
    st.title("📩 Contact")
    st.markdown(
        """
    #### Coordonnées
    **Adresse**: CHU de Dakar, BP 7325 Dakar Étoile, Sénégal  
    
    **Téléphone**: +221 77 808 09 42
    
    **Email**: ahmed.sefdine@uadb.edu.sn
    """
    )
    with st.form("contact_form"):
        name = st.text_input("Nom complet")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Envoyer"):
            st.success("✅ Message envoyé avec succès !")

# ----------------------------------------------------------
# Navigation Principale (Onglets en haut)
# ----------------------------------------------------------
PAGES = {
    "🏠 Accueil": accueil,
    "📊 Analyse": analyse_descriptive,
    "🤖 Prédiction": modelisation,
    "📚 À Propos": a_propos,
    "📩 Contact": contact
}

def main():
    tabs = st.tabs(list(PAGES.keys()))
    for tab, (page_name, page_func) in zip(tabs, PAGES.items()):
        with tab:
            page_func()

if __name__ == "__main__":
    main()
