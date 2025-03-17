import os
import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import plotly.express as px
from PIL import Image

# ----------------------------------------------------------
# Configuration de l'application
# ----------------------------------------------------------
st.set_page_config(
    page_title="OncoSuite - Cancer Gastrique",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chargement des images
LOGO_PATH = "assets/header.jpg"

# Chargement des modèles et des données
MODELS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib",
    "GBST": "models/gbst.joblib"
}

DATA_PATH = "data/GastricCancerData.xlsx"

FEATURE_CONFIG = {
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
# Fonctions Utilitaires
# ----------------------------------------------------------
@st.cache_data
def load_data():
    """Charge les données depuis le fichier Excel."""
    if os.path.exists(DATA_PATH):
        return pd.read_excel(DATA_PATH)
    else:
        st.error(f"❌ Fichier introuvable : {DATA_PATH}")
        return pd.DataFrame()

@st.cache_resource
def load_model(model_path):
    """Charge un modèle en gérant les erreurs."""
    if not os.path.exists(model_path):
        st.error(f"❌ Modèle introuvable : {model_path}")
        return None
    try:
        if model_path.endswith(".keras"):
            return tf.keras.models.load_model(model_path)
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {e}")
        return None

def encode_features(inputs):
    """Encode les entrées utilisateur sous format numérique."""
    return pd.DataFrame({k: [1 if v == "OUI" else 0] for k, v in inputs.items()})

# ----------------------------------------------------------
# Pages de l'application
# ----------------------------------------------------------
def accueil():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(LOGO_PATH, width=200)
    with col2:
        st.title("🩺 OncoSuite - Plateforme d'Aide à la Décision")
        st.markdown("""
        **Estimation du temps de survie post-traitement du cancer gastrique**
        """)
    
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
        st.write(f"📌 Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")

    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Distribution des variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var, color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🌡 Matrice de corrélation")
        corr_matrix = df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r')
        st.plotly_chart(fig, use_container_width=True)

def modelisation():
    st.title("🤖 Prédiction de Survie")

    with st.expander("📋 Paramètres du patient", expanded=True):
        inputs = {}
        cols = st.columns(3)
        for i, (feature, label) in enumerate(FEATURE_CONFIG.items()):
            with cols[i % 3]:
                inputs[feature] = st.radio(label, ["Non", "Oui"], horizontal=True)
    
    input_df = encode_features(inputs)

    st.markdown("---")
    tabs = st.tabs(list(MODELS.keys()))

    for tab, model_name in zip(tabs, MODELS.keys()):
        with tab:
            model = load_model(MODELS[model_name])
            if model:
                try:
                    prediction = model.predict(input_df)[0]
                    st.metric("📊 Survie médiane estimée", f"{prediction:.1f} mois")
                except Exception as e:
                    st.error(f"❌ Erreur de prédiction : {e}")

def a_propos():
    st.title("📚 À Propos")
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
    **Adresse**: CHU de Dakar, Sénégal  
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
# Navigation avec onglets en haut
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

    for tab, (page_name, page_function) in zip(tabs, PAGES.items()):
        with tab:
            page_function()

if __name__ == "__main__":
    main()
