import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import plotly.express as px
from PIL import Image

# Configuration initiale DEVEUT ÊTRE EN PREMIER
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
    "Random Survival Forest": "models/rsf.joblib",
    "GBST": "models/gbst.joblib"
}

FEATURES = {
    'Cardiopathie': "Cardiopathie",
    'Ulceregastrique': "Ulcère gastrique",
    'Douleurepigastrique': "Douleur épigastrique",
    'Ulcero-bourgeonnant': "Lésion ulcéro-bourgeonnante",
    'Denutrution': "Dénutrition",
    'Tabac': "Tabagisme actif",
    'Mucineux': "Type mucineux",
    'Infiltrant': "Type infiltrant",
    'Stenosant': "Type sténosant",
    'Metastases': "Métastases",
    'Adenopathie': "Adénopathie"
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

# ----------------------------------------------------------
# Sections de l'application
# ----------------------------------------------------------
def accueil():
    st.title("🩺 OncoSuite - Plateforme d'Aide à la Décision")
    st.image("assets/header.jpg", use_column_width=True)
    st.markdown("""
    **Bienvenue dans l'interface de prédiction du temps de survie des patients atteints de cancer gastrique.**
    
    Naviguez via le menu latéral pour :
    - 📊 Explorer les données cliniques
    - 🔍 Analyser les statistiques descriptives
    - 🤖 Utiliser les modèles prédictifs
    - 📩 Nous contacter
    """)

def analyse_descriptive():
    st.title("📊 Analyse Descriptive")
    df = load_data()
    
    with st.expander("Aperçu des données brutes"):
        st.dataframe(df.head())
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Distribution des Variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var)
        st.plotly_chart(fig)
    
    with col2:
        st.subheader("Corrélations Cliniques")
        corr_matrix = df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r')
        st.plotly_chart(fig)

def modelisation():
    st.title("🤖 Interface de Prédiction")
    
    # Formulaire patient
    with st.sidebar:
        st.header("📋 Paramètres du Patient")
        inputs = {feature: st.radio(label, ["Non", "Oui"]) 
                for feature, label in FEATURES.items()}
        input_df = pd.DataFrame({k: [1 if v == "Oui" else 0] 
                               for k, v in inputs.items()})
    
    # Affichage résultats
    tab1, tab2, tab3 = st.tabs(list(MODELS.keys()))
    
    for model_name, tab in zip(MODELS.keys(), [tab1, tab2, tab3]):
        with tab:
            model = load_model(MODELS[model_name])
            if model:
                try:
                    prediction = model.predict(input_df)[0]
                    st.metric("Survie médiane estimée", 
                            f"{prediction:.1f} mois",
                            help="Prédiction basée sur les données cliniques actuelles")
                    st.progress(min(int(prediction/120*100), 100))
                except Exception as e:
                    st.error(f"Erreur de prédiction: {str(e)}")

def a_propos():
    st.title("📚 À Propos")
    st.markdown("""
    **Version**: 1.0.0  
    **Dernière mise à jour**: 15 mai 2024  
    **Équipe Médicale**:
    - Dr. Alioune Diop (Oncologue)
    - Pr. Aminata Ndiaye (Chirurgien Digestif)
    - M. Jean Dupont (Data Scientist)
    """)
    st.image("assets/team.jpg", width=600)

def contact():
    st.title("📩 Nous Contacter")
    with st.form("contact_form"):
        name = st.text_input("Nom complet")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Envoyer"):
            st.success("Message envoyé avec succès!")

# ----------------------------------------------------------
# Navigation Principale
# ----------------------------------------------------------
def main():
    pages = {
        "Accueil": accueil,
        "Analyse des Données": analyse_descriptive,
        "Modélisation": modelisation,
        "À Propos": a_propos,
        "Contact": contact
    }
    
    # Menu latéral
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("", list(pages.keys()))
    
    # Affichage de la page sélectionnée
    pages[selection]()

if __name__ == "__main__":
    main()
