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

# --- Patch scikit-learn pour éviter l'erreur 'sklearn_tags' ---
try:
    from sklearn.base import BaseEstimator
    if not hasattr(BaseEstimator, "sklearn_tags"):
        @property
        def sklearn_tags(self):
            return {}
        BaseEstimator.sklearn_tags = sklearn_tags
except Exception as e:
    pass

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

# Configuration des variables
FEATURE_CONFIG = {
    "AGE": "Âge",
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
    """Charge un modèle pré-entraîné."""
    if not os.path.exists(model_path):
        st.error(f"❌ Modèle introuvable : {model_path}")
        return None

    try:
        _, ext = os.path.splitext(model_path)
        if ext in ['.keras', '.h5']:
            def cox_loss(y_true, y_pred):
                event = tf.cast(y_true[:, 0], dtype=tf.float32)
                risk = y_pred[:, 0]
                log_risk = tf.math.log(tf.cumsum(tf.exp(risk), reverse=True)
                loss = -tf.reduce_mean((risk - log_risk) * event)
                return loss
            return tf_load_model(model_path, custom_objects={"cox_loss": cox_loss})
        else:
            return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {e}")
        return None

def encode_features(inputs):
    """Encode les variables."""
    encoded = {}
    for k, v in inputs.items():
        if k == "AGE":
            encoded[k] = v
        else:
            encoded[k] = 1 if v.upper() == "OUI" else 0
    return pd.DataFrame([encoded])

def predict_survival(model, data, model_name):
    """Effectue la prédiction avec intervalles de confiance."""
    result = {'median': None, 'lower_ci': None, 'upper_ci': None}
    try:
        if model_name == "Cox PH":
            pred = model.predict_median(data, return_ci=True)
            if isinstance(pred, pd.DataFrame):
                result['median'] = pred['0.5'].iloc[0]
                result['lower_ci'] = pred['0.5_lower_ci'].iloc[0]
                result['upper_ci'] = pred['0.5_upper_ci'].iloc[0]
        
        elif model_name in ["RSF", "GBST"] and hasattr(model, 'estimators_'):
            all_predictions = []
            for estimator in model.estimators_:
                if hasattr(estimator, 'predict_median'):
                    pred = estimator.predict_median(data)
                else:
                    pred = estimator.predict(data)
                all_predictions.append(pred)
            if all_predictions:
                all_predictions = np.array(all_predictions).flatten()
                result['median'] = np.median(all_predictions)
                result['lower_ci'] = np.percentile(all_predictions, 2.5)
                result['upper_ci'] = np.percentile(all_predictions, 97.5)
        
        elif model_name == "DeepSurv":
            pred = model.predict(data)
            if isinstance(pred, np.ndarray):
                result['median'] = pred[0][0] if pred.ndim == 2 else pred[0]
        
        else:
            if hasattr(model, "predict_median"):
                pred = model.predict_median(data)
                result['median'] = pred[0] if isinstance(pred, (np.ndarray, pd.Series)) else pred
            
            elif hasattr(model, "predict"):
                pred = model.predict(data)
                result['median'] = pred[0] if isinstance(pred, (np.ndarray, pd.Series)) else pred

    except Exception as e:
        st.error(f"Erreur de prédiction : {e}")
    return result

def clean_prediction(value, model_name):
    """Nettoie les valeurs de prédiction."""
    if value is None:
        return None
    try:
        pred_val = float(value)
        if model_name in ["Cox PH", "RSF", "GBST"]:
            return max(pred_val, 0)
        elif model_name == "DeepSurv":
            return max(pred_val, 1)
        return pred_val
    except:
        return None

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
                if feature == "AGE":
                    inputs[feature] = st.number_input(label, min_value=18, max_value=120, value=50, key=feature)
                else:
                    inputs[feature] = st.selectbox(label, options=["Non", "Oui"], key=feature)
    
    input_df = encode_features(inputs)
    st.markdown("---")
    
    model_name = st.selectbox("Choisir un modèle", list(MODELS.keys()))
    model = load_model(MODELS[model_name])
    
    if st.button("Prédire le temps de survie"):
        if model:
            try:
                pred_result = predict_survival(model, input_df, model_name)
                cleaned_median = clean_prediction(pred_result.get('median'), model_name)
                lower_ci = clean_prediction(pred_result.get('lower_ci'), model_name)
                upper_ci = clean_prediction(pred_result.get('upper_ci'), model_name)
                
                if cleaned_median is None:
                    raise ValueError("Prédiction invalide")
                
                st.metric(label="Survie médiane estimée", value=f"{cleaned_median:.1f} mois")
                
                # Affichage des intervalles de confiance
                if lower_ci and upper_ci:
                    st.success(f"Intervalle de confiance 95% : {lower_ci:.1f} - {upper_ci:.1f} mois")
                else:
                    st.warning("Intervalle de confiance non disponible pour ce modèle")
                
                # Graphique de survie
                months = min(int(cleaned_median), 120)
                fig = px.line(
                    x=list(range(months)),
                    y=[100 - (i / months) * 100 for i in range(months)],
                    labels={"x": "Mois", "y": "Probabilité de survie (%)"},
                    color_discrete_sequence=['#2ca02c']
                )
                st.plotly_chart(fig, use_container_width=True)
            
            except Exception as e:
                st.error(f"❌ Erreur de prédiction : {str(e)}")

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
# Navigation Principale
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
