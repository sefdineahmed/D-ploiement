import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
import joblib
import tensorflow as tf

# Configuration initiale - DOIT ÊTRE LA PREMIÈRE COMMANDE STREAMLIT
st.set_page_config(
    page_title="OncoDecision - Cancer Gastrique",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuration des chemins
DATA_PATH = "data/GastricCancerData.xlsx"
MODEL_PATHS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib",
    "GBST": "models/gbst.joblib",
    "DeepSurv": "models/deepsurv.keras"
}

# Configuration des caractéristiques
FEATURE_CONFIG = {
    'AGE': {'label': 'Âge', 'type': 'number', 'min': 18, 'max': 100, 'default': 50},
    'SEXE': {'label': 'Sexe', 'type': 'select', 'options': ['Femme', 'Homme']},
    'Cardiopathie': {'label': 'Cardiopathie', 'type': 'bool'},
    # Ajouter toutes les autres variables selon le même format
}

# Définition de la fonction de perte custom pour DeepSurv
@tf.keras.utils.register_keras_serializable()
def cox_loss(y_true, y_pred):
    event = y_true[:, 0]
    time = y_true[:, 1]
    sorted_idx = tf.argsort(time, direction='DESCENDING')
    event = tf.gather(event, sorted_idx)
    pred = tf.gather(y_pred, sorted_idx)
    hazard_ratio = tf.exp(pred)
    log_risk = tf.math.log(tf.cumsum(hazard_ratio) + 1e-15)
    uncensored_likelihood = (pred - log_risk) * event
    return -tf.reduce_mean(uncensored_likelihood)

# Fonctions de chargement
@st.cache_data
def load_data():
    return pd.read_excel(DATA_PATH)

@st.cache_resource
def load_model(model_name):
    if MODEL_PATHS[model_name].endswith('.keras'):
        return tf.keras.models.load_model(MODEL_PATHS[model_name], custom_objects={'cox_loss': cox_loss})
    return joblib.load(MODEL_PATHS[model_name])

# Sections de l'application
def accueil():
    st.title("Bienvenue dans OncoDecision")
    st.image("assets/header.jpg", use_column_width=True)
    st.markdown("""
    **Outil d'aide à la décision pour le cancer gastrique**
    - 📊 Analyse des données patients
    - 📈 Modèles prédictifs de survie
    - 🎯 Recommandations personnalisées
    """)

def analyse_descriptive():
    st.title("Analyse Exploratoire")
    df = load_data()
    
    with st.expander("Données Brutes"):
        st.dataframe(df.head())
    
    col1, col2 = st.columns(2)
    with col1:
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var)
        st.plotly_chart(fig)
    
    with col2:
        if 'Deces' in df.columns:
            kmf = KaplanMeierFitter()
            kmf.fit(df['Tempsdesuivi (Mois)'], df['Deces'])
            fig = px.line(kmf.survival_function_, title='Courbe de Survie Kaplan-Meier')
            st.plotly_chart(fig)

def prediction():
    st.title("Prédiction de Survie")
    
    with st.sidebar:
        st.header("Informations Patient")
        inputs = {}
        for feature, config in FEATURE_CONFIG.items():
            if config['type'] == 'number':
                inputs[feature] = st.number_input(config['label'], 
                                                 min_value=config['min'],
                                                 max_value=config['max'],
                                                 value=config['default'])
            elif config['type'] == 'bool':
                inputs[feature] = st.selectbox(config['label'], ['Non', 'Oui']) == 'Oui'
                
    # Encodage des entrées
    input_df = pd.DataFrame([inputs])
    
    # Affichage des prédictions
    tabs = st.tabs(list(MODEL_PATHS.keys()))
    for tab, model_name in zip(tabs, MODEL_PATHS.keys()):
        with tab:
            try:
                model = load_model(model_name)
                pred = model.predict(input_df)[0]
                st.metric("Survie Médiane Estimée", f"{pred:.1f} mois")
                
                # Visualisation temporelle
                time_points = np.linspace(0, pred, 100)
                fig = px.line(x=time_points, y=1 - (time_points/pred), 
                             labels={'x': 'Mois', 'y': 'Probabilité de Survie'})
                st.plotly_chart(fig)
                
            except Exception as e:
                st.error(f"Erreur avec {model_name}: {str(e)}")

def a_propos():
    st.title("À Propos")
    st.markdown("""
    **Version:** 2.0  
    **Développé par:** Équipe d'Oncologie CHU Dakar  
    **Contact:** contact@oncodecision.sn
    """)
    st.image("assets/team.jpg", width=600)

def contact():
    st.title("Contact")
    with st.form("form_contact"):
        nom = st.text_input("Nom complet")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Envoyer"):
            st.success("Message envoyé avec succès!")

# Navigation Principale
PAGES = {
    "Accueil": accueil,
    "Analyse": analyse_descriptive,
    "Prédiction": prediction,
    "À Propos": a_propos,
    "Contact": contact
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("", list(PAGES.keys()))
    PAGES[selection]()

if __name__ == "__main__":
    main()
