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
# Configuration des données et modèles
# ----------------------------------------------------------
MODELS = {
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

# ----------------------------------------------------------
# Fonctions utilitaires
# ----------------------------------------------------------
def load_data():
    """Charge les données depuis le fichier Excel"""
    return pd.read_excel("data/GastricCancerData.xlsx")

def load_model(model_path):
    """Charge un modèle avec gestion d'erreur"""
    try:
        if model_path.endswith(".keras"):
            return tf.keras.models.load_model(model_path)
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Erreur de chargement du modèle: {str(e)}")
        return None

def encode_features(inputs):
    """Encode les entrées utilisateur en format numérique"""
    return pd.DataFrame({k: [1 if v else 0] for k, v in inputs.items()})

# ----------------------------------------------------------
# Sections de l'application
# ----------------------------------------------------------
def accueil():
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
    
    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(10))
        st.write(f"Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Distribution des variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var, color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌡 Matrice de corrélation")
        corr_matrix = df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r', labels=dict(color="Corrélation"))
        st.plotly_chart(fig, use_container_width=True)

def modelisation():
    st.title("🤖 Prédiction de Survie")
    
    with st.expander("📋 Paramètres du patient", expanded=True):
        inputs = {}
        for feature, config in FEATURE_CONFIG.items():
            inputs[feature] = st.selectbox(label=config["label"], options=("Non", "Oui"), key=feature)
    
    input_df = encode_features({k: v == "Oui" for k, v in inputs.items()})
    
    st.markdown("---")
    for model_name, model_path in MODELS.items():
        model = load_model(model_path)
        if model:
            try:
                prediction = model.predict(input_df)[0]
                st.metric(label=f"{model_name} - Survie médiane estimée", value=f"{prediction:.1f} mois")
            except Exception as e:
                st.error(f"Erreur de prédiction : {str(e)}")

def main():
    pages = {
        "Accueil": accueil,
        "Analyse": analyse_descriptive,
        "Prédiction": modelisation
    }
    
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Aller à", list(pages.keys()))
    pages[selection]()

if __name__ == "__main__":
    main()
