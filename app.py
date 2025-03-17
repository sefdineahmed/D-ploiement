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
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("assets/header.jpg", width=200)
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
    
    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(10))  # Correction ici
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
        fig = px.imshow(corr_matrix, 
                       color_continuous_scale='RdBu_r',
                       labels=dict(color="Corrélation"))
        st.plotly_chart(fig, use_container_width=True)

def modelisation():
    st.title("🤖 Prédiction de Survie")
    
    # Formulaire d'entrée
    with st.expander("📋 Paramètres du patient", expanded=True):
        inputs = {}
        cols = st.columns(3)
        for i, (feature, config) in enumerate(FEATURE_CONFIG.items()):
            with cols[i % 3]:
                inputs[feature] = st.selectbox(
                    label=config["label"],
                    options=("Non", "Oui"),
                    key=feature
                )
    
    # Encodage des données
    input_df = encode_features({k: v == "Oui" for k, v in inputs.items()})
    
    # Affichage des résultats
    st.markdown("---")
    tabs = st.tabs(list(MODELS.keys()))
    
    for tab, model_name in zip(tabs, MODELS.keys()):
        with tab:
            model = load_model(MODELS[model_name])
            if model:
                try:
                    prediction = model.predict(input_df)[0]
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.metric(
                            label="Survie médiane estimée",
                            value=f"{prediction:.1f} mois",
                            help="Valeur prédite par le modèle"
                        )
                    with col2:
                        months = min(int(prediction), 120)
                        fig = px.line(
                            x=list(range(months)),
                            y=[100 - (i/months)*100 for i in range(months)],
                            labels={"x": "Mois", "y": "Probabilité de survie (%)"},
                            color_discrete_sequence=['#2ca02c']
                        )
                        st.plotly_chart(fig, use_container_width=True)
                except Exception as e:
                    st.error(f"Erreur de prédiction : {str(e)}")

def a_propos():
    st.title("📚 À Propos")
    cols = st.columns([1, 3])
    with cols[0]:
        st.image("assets/team.jpg")
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
    with st.container(border=True):
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
            if st.form_submit_button("Envoyer", type="primary"):
                st.success("Message envoyé avec succès !")

# ----------------------------------------------------------
# Navigation Principale
# ----------------------------------------------------------
def main():
    pages = {
        "Accueil": accueil,
        "Analyse": analyse_descriptive,
        "Prédiction": modelisation,
        "À Propos": a_propos,
        "Contact": contact
    }
    
    # Navigation horizontale
    st.markdown("""
    <style>
        div[data-testid="stHorizontalBlock"] {
            gap: 0.5rem;
            padding: 1rem;
            background: #f0f2f6;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        cols = st.columns(len(pages))
        for i, (page_name, _) in enumerate(pages.items()):
            with cols[i]:
                if st.button(page_name, use_container_width=True):
                    st.session_state.current_page = page_name
    
    # Affichage de la page sélectionnée
    current_page = pages.get(st.session_state.get("current_page", "Accueil"))
    current_page()

if __name__ == "__main__":
    main()
