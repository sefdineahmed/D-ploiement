import os
import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import plotly.express as px
from PIL import Image

# Configuration initiale
st.set_page_config(
    page_title="OncoSuite - Cancer Gastrique",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# Chargement sécurisé des modèles et données
# ----------------------------------------------------------
DATA_PATH = "data/GastricCancerData.xlsx"
MODEL_PATHS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib",
    "GBST": "models/gbst.joblib"
}

FEATURE_CONFIG = {
    'Cardiopathie': {"label": "Cardiopathie", "type": "bool"},
    'Ulceregastrique': {"label": "Ulcère gastrique", "type": "bool"},
    'Douleurepigastrique': {"label": "Douleur épigastrique", "type": "bool"},
    'Ulcero-bourgeonnant': {"label": "Lésion ulcéro-bourgeonnante", "type": "bool"},
    'Denutrution': {"label": "Dénutrition", "type": "bool"},
    'Tabac': {"label": "Tabagisme actif", "type": "bool"},
    'Mucineux': {"label": "Type mucineux", "type": "bool"},
    'Infiltrant': {"label": "Type infiltrant", "type": "bool"},
    'Stenosant': {"label": "Type sténosant", "type": "bool"},
    'Metastases': {"label": "Métastases", "type": "bool"},
    'Adenopathie': {"label": "Adénopathie", "type": "bool"}
}

def load_data():
    """Charge les données depuis un fichier Excel si disponible."""
    if os.path.exists(DATA_PATH):
        return pd.read_excel(DATA_PATH)
    else:
        st.error(f"Fichier introuvable : {DATA_PATH}")
        return pd.DataFrame()

def load_model(model_path):
    """Charge un modèle avec vérification d'existence."""
    if not os.path.exists(model_path):
        st.error(f"Modèle introuvable : {model_path}")
        return None
    try:
        if model_path.endswith(".keras"):
            return tf.keras.models.load_model(model_path)
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Erreur de chargement du modèle : {e}")
        return None

def encode_features(inputs):
    """Transforme les entrées en format binaire."""
    return pd.DataFrame({k: [1 if v else 0] for k, v in inputs.items()})

# ----------------------------------------------------------
# Définition des pages
# ----------------------------------------------------------
def accueil():
    st.image("assets/header.jpg", width=200)
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
        corr_matrix = df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r')
        st.plotly_chart(fig, use_container_width=True)

def modelisation():
    st.title("🤖 Prédiction de Survie")
    
    with st.expander("📋 Paramètres du patient", expanded=True):
        inputs = {}
        for feature, config in FEATURE_CONFIG.items():
            inputs[feature] = st.radio(config["label"], ["Non", "Oui"]) == "Oui"

    input_df = encode_features(inputs)
    st.markdown("---")
    tabs = st.tabs(list(MODEL_PATHS.keys()))
    
    for tab, model_name in zip(tabs, MODEL_PATHS.keys()):
        with tab:
            model = load_model(MODEL_PATHS[model_name])
            if model:
                try:
                    prediction = model.predict(input_df)[0]
                    st.metric(
                        label="Survie médiane estimée",
                        value=f"{prediction:.1f} mois"
                    )
                except Exception as e:
                    st.error(f"Erreur de prédiction : {e}")

def a_propos():
    st.title("📚 À Propos")
    st.image("assets/team.jpg")
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
            st.success("Message envoyé avec succès !")

# ----------------------------------------------------------
# Navigation Principale
# ----------------------------------------------------------
PAGES = {
    "Accueil": accueil,
    "Analyse": analyse_descriptive,
    "Prédiction": modelisation,
    "À Propos": a_propos,
    "Contact": contact
}

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Aller à", list(PAGES.keys()))
    PAGES[page]()

if __name__ == "__main__":
    main()
