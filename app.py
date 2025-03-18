import os
import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import plotly.express as px
from PIL import Image

# ----------------------------------------------------------
# Patch pour les incompatibilités de versions
# ----------------------------------------------------------
# Patch pour trapz (SciPy)
import scipy.integrate as integrate
try:
    from scipy.integrate import trapz
except ImportError:
    from numpy import trapz as np_trapz
    integrate.trapz = np_trapz

# Patch pour validate_data (scikit-learn)
try:
    from sklearn.utils.validation import validate_data
except ImportError:
    def validate_data(*args, **kwargs):
        return

# Import pour Kaplan-Meier
from lifelines import KaplanMeierFitter

# ----------------------------------------------------------
# Configuration de l'application
# ----------------------------------------------------------
st.set_page_config(
    page_title="OncoSuite - Cancer Gastrique",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chemins vers les ressources
DATA_PATH = "data/GastricCancerData.xlsx"
LOGO_PATH = "assets/header.jpg"
TEAM_IMG_PATH = "assets/team.jpg"

# Configuration des modèles (ajout du modèle DeepSurv)
MODELS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib",
    "DeepSurv": "models/deepsurv.keras",
    "GBST": "models/gbst.joblib"
}

# ----------------------------------------------------------
# Configuration des variables
# Nous ajoutons "Âge" pour satisfaire l'exigence du modèle DeepSurv (12 features)
# Les autres variables restent catégorielles (Oui/Non)
# ----------------------------------------------------------
FEATURE_CONFIG = {
    "Age": "Âge",
    "Cardiopathie": "Cardiopathie",
    "Ulceregastrique": "Ulcère gastrique",
    "Douleurepigastrique": "Douleur épigastrique",
    "Ulcero-bourgeonnant": "Lésion ulcéro-bourgeonnante",
    "Denutrution": "Dénutrition",
    "Tabac": "Tabagisme actif",
    "Mucineux": "Type mucineux",
    "Infiltrant": "Type infiltrant",
    "Stenosant": "Type sténosant",
    "Metastases": "Métastases",
    "Adenopathie": "Adénopathie"
}

# ----------------------------------------------------------
# Fonction personnalisée pour DeepSurv
# ----------------------------------------------------------
@tf.keras.utils.register_keras_serializable()
def cox_loss(y_true, y_pred):
    """
    Implémente la fonction de perte Cox.
    Remplacez cette implémentation par celle utilisée lors de l'entraînement.
    """
    return tf.reduce_mean(tf.square(y_true - y_pred))

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
    """Charge un modèle en gérant les erreurs et en passant les custom_objects si nécessaire."""
    if not os.path.exists(model_path):
        st.error(f"❌ Modèle introuvable : {model_path}")
        return None
    try:
        if model_path.endswith(".keras"):
            return tf.keras.models.load_model(model_path, custom_objects={'cox_loss': cox_loss})
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {e}")
        return None

def encode_features(inputs):
    """
    Encode les variables en format numérique.
    Pour les variables catégorielles : "Oui" devient 1, "Non" devient 0.
    Pour les variables numériques, on conserve la valeur.
    """
    encoded = {}
    for key, value in inputs.items():
        if isinstance(value, (int, float)):
            encoded[key] = [value]
        else:
            encoded[key] = [1 if value == "OUI" else 0]
    return pd.DataFrame(encoded)

# ----------------------------------------------------------
# Définition des Pages
# ----------------------------------------------------------
def accueil():
    col1, col2 = st.columns([1, 3])
    with col1:
        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, width=200)
    with col2:
        st.title("🩺 OncoSuite - Plateforme d'Aide à la Décision")
        st.markdown("**Estimation du temps de survie post-traitement du cancer gastrique**")
    st.markdown("---")
    st.write("""
    ### Fonctionnalités principales :
    - 📊 Exploration interactive des données cliniques
    - 📈 Analyse statistique descriptive
    - 🤖 Prédiction multi-modèles de survie
    - 📤 Export des résultats cliniques
    """)

def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    if df.empty:
        return

    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(10))
        st.write(f"Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Distribution des variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var, color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig, use_container_width=True)
        
        # Histogramme de la distribution du traitement
        if "Traitement" in df.columns:
            st.subheader("📊 Distribution du Traitement")
            fig2 = px.histogram(df, x="Traitement", color_discrete_sequence=['#ff7f0e'])
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.warning("La colonne 'Traitement' n'est pas disponible dans les données.")
    
    with col2:
        st.subheader("🌡 Matrice de corrélation")
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r', labels={"color": "Corrélation"})
        st.plotly_chart(fig, use_container_width=True)
        
        # Courbe de survie Kaplan-Meier
        if "temps" in df.columns and "event" in df.columns:
            st.subheader("📉 Courbe de survie Kaplan-Meier")
            kmf = KaplanMeierFitter()
            kmf.fit(durations=df["Tempsdesuivi (Mois)"], event_observed=df["Deces"])
            km_data = kmf.survival_function_.reset_index()
            fig_km = px.line(km_data, x="index", y=km_data.columns[1],
                             labels={"index": "Temps", km_data.columns[1]: "Survie"},
                             title="Courbe de survie Kaplan-Meier")
            st.plotly_chart(fig_km, use_container_width=True)
        else:
            st.warning("Les colonnes 'temps' et/ou 'event' ne sont pas disponibles pour le calcul de Kaplan-Meier.")

def modelisation():
    st.title("🤖 Prédiction de Survie")
    
    with st.expander("📋 Paramètres du patient", expanded=True):
        inputs = {}
        cols = st.columns(3)
        for i, (feature, label) in enumerate(FEATURE_CONFIG.items()):
            with cols[i % 3]:
                if feature == "Age":
                    inputs[feature] = st.number_input(label, min_value=0, max_value=120, value=50, step=1, key=feature)
                else:
                    inputs[feature] = st.selectbox(label, options=["Non", "Oui"], key=feature)
    
    input_df = encode_features(inputs)
    st.markdown("---")
    
    tabs = st.tabs(list(MODELS.keys()))
    for tab, model_name in zip(tabs, MODELS.keys()):
        with tab:
            model = load_model(MODELS[model_name])
            if model:
                try:
                    prediction = model.predict(input_df)[0]
                    # Convertir la prédiction en float pour l'affichage
                    prediction_val = float(prediction.item()) if hasattr(prediction, "item") else float(prediction)
                    st.metric(label="Survie médiane estimée", value=f"{prediction_val:.1f} mois")
                    
                    months = min(int(prediction_val), 120)
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
            st.image(TEAM_IMG_PATH)
    with cols[1]:
        st.markdown("""
        ### Équipe Médicale
        - **Dr. Alioune Diop** - Oncologue
        - **Pr. Aminata Ndiaye** - Chirurgien Digestif
        - **M. Jean Dupont** - Data Scientist
        
        **Version**: 2.1.0  
        **Dernière mise à jour**: Juin 2024
        """)

def contact():
    st.title("📩 Contact")
    st.markdown("""
    #### Coordonnées
    **Adresse**: CHU de Dakar, BP 7325 Dakar Étoile, Sénégal  
    **Téléphone**: +221 33 839 50 00  
    **Email**: contact@oncosuite.sn
    """)
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
