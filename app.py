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
    "Random Survival Forest": "models/rsf.joblib",
    "GBST": "models/gbst.joblib"
}

FEATURE_CONFIG = {
    'Cardiopathie': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Ulceregastrique': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Douleurepigastrique': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Ulcero-bourgeonnant': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Denutrution': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Tabac': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Mucineux': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Infiltrant': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Stenosant': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Metastases': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}},
    'Adenopathie': {"type": "categorical", "options": ["Non", "Oui"], "encoding": {"Non": 0, "Oui": 1}}
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
            return tf.keras.models.load_model(model_path, custom_objects={'cox_loss': cox_loss})
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Erreur de chargement du modèle: {str(e)}")
        return None

@tf.keras.utils.register_keras_serializable()
def cox_loss(y_true, y_pred):
    """Fonction de perte personnalisée pour DeepSurv"""
    event = tf.cast(y_true[:, 0], tf.bool)
    time = tf.cast(y_true[:, 1], tf.float32)
    pred = tf.reshape(tf.cast(y_pred, tf.float32), [-1])
    sort_idx = tf.argsort(time, direction='DESCENDING')
    event = tf.gather(event, sort_idx)
    pred = tf.gather(pred, sort_idx)
    time = tf.gather(time, sort_idx)
    hazard_ratio = tf.exp(pred)
    log_risk = tf.math.log(tf.cumsum(hazard_ratio) + 1e-15)
    uncensored_likelihood = pred - log_risk
    likelihood = uncensored_likelihood * tf.cast(event, tf.float32)
    return -tf.reduce_mean(likelihood)

# ----------------------------------------------------------
# Sections de l'application
# ----------------------------------------------------------
def accueil():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("assets/header.jpg", width=150)
    with col2:
        st.title("OncoSuite - Plateforme d'Aide à la Décision")
    
    st.markdown("""
    **Bienvenue dans l'interface de prédiction du temps de survie des patients atteints de cancer gastrique.**
    """)
    
    with st.expander("📌 Instructions d'utilisation"):
        st.markdown("""
        1. Naviguez entre les onglets en haut de la page
        2. Utilisez le formulaire dans la sidebar pour saisir les données
        3. Consultez les prédictions dans l'onglet Modélisation
        """)

def analyse_descriptive():
    st.header("📊 Analyse Exploratoire des Données")
    df = load_data()
    
    tab1, tab2, tab3 = st.tabs(["Données Brutes", "Statistiques", "Visualisation"])
    
    with tab1:
        st.dataframe(df.head(10), use_container_width=True)
    
    with tab2:
        st.subheader("Statistiques Descriptives")
        st.dataframe(df.describe(), use_container_width=True)
    
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            var = st.selectbox("Choisir une variable", df.columns)
            fig = px.histogram(df, x=var, title=f"Distribution de {var}")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.box(df, y=var, title=f"Boîte à moustaches de {var}")
            st.plotly_chart(fig, use_container_width=True)

def modelisation():
    st.header("🤖 Modélisation Prédictive")
    
    with st.sidebar:
        st.subheader("📋 Formulaire Patient")
        inputs = {}
        for feature, config in FEATURE_CONFIG.items():
            inputs[feature] = st.radio(
                label=feature,
                options=config["options"],
                horizontal=True
            )
        
        if st.button("Générer la Prédiction"):
            input_df = pd.DataFrame({
                k: [v["encoding"][inputs[k]] for k, v in FEATURE_CONFIG.items()
            })
            st.session_state.input_df = input_df
    
    if 'input_df' in st.session_state:
        tab1, tab2, tab3 = st.tabs(list(MODELS.keys()))
        
        for model_name, tab in zip(MODELS.keys(), [tab1, tab2, tab3]):
            with tab:
                model = load_model(MODELS[model_name])
                if model:
                    try:
                        prediction = model.predict(st.session_state.input_df)[0]
                        st.metric(
                            label="Survie Médiane Estimée",
                            value=f"{prediction:.1f} mois",
                            help="Prédiction basée sur les données cliniques saisies"
                        )
                        fig = px.scatter(
                            x=[prediction],
                            y=[model_name],
                            labels={'x': 'Mois', 'y': 'Modèle'},
                            title="Comparaison des Prédictions"
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    except Exception as e:
                        st.error(f"Erreur de prédiction: {str(e)}")

def a_propos():
    st.header("📚 À Propos")
    cols = st.columns([1, 3])
    with cols[0]:
        st.image("assets/team.jpg", use_container_width=True)
    with cols[1]:
        st.markdown("""
        **Version :** 2.1.0  
        **Dernière mise à jour :** 2024-05-20  
        **Équipe :**
        - Dr. Alioune Diop (Oncologie)
        - Pr. Aminata Ndiaye (Chirurgie)
        - Data Science Team
        """)

def contact():
    st.header("📩 Contact")
    with st.form("contact_form"):
        st.write("**Formulaire de contact**")
        name = st.text_input("Nom complet")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Envoyer"):
            st.success("Message envoyé avec succès!")

# ----------------------------------------------------------
# Navigation Principale
# ----------------------------------------------------------
PAGES = {
    "Accueil": accueil,
    "Analyse des Données": analyse_descriptive,
    "Modélisation": modelisation,
    "À Propos": a_propos,
    "Contact": contact
}

def main():
    st.sidebar.image("assets/logo.png", use_column_width=True)
    selection = st.sidebar.radio("Navigation", list(PAGES.keys()))
    PAGES[selection]()

if __name__ == "__main__":
    main()
