import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
import plotly.express as px
from PIL import Image

# Configuration initiale OBLIGATOIRE en première commande
st.set_page_config(
    page_title="OncoPredict - Cancer Gastrique",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (après set_page_config)
st.markdown("""
<style>
    .main {background: #f8f9fa;}
    .stButton>button {border-radius: 8px;}
    .stTabs [role="tab"] {font-size: 16px; padding: 12px;}
    .pred-value {font-size: 24px !important; color: #2e86c1;}
</style>
""", unsafe_allow_html=True)

# Configuration des modèles
MODELS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib", 
    "GBST": "models/gbst.joblib",
    "DeepSurv": "models/deepsurv.keras"
}

VARIABLES = {
    'Cardiopathie': "Cardiopathie associée",
    'Ulceregastrique': "Antécédent d'ulcère",
    'Douleurepigastrique': "Douleur épigastrique",
    'Ulcero-bourgeonnant': "Lésion ulcéro-bourgeonnante",
    'Denutrution': "Dénutrition sévère",
    'Tabac': "Consommation tabagique",
    'Mucineux': "Type mucineux",
    'Infiltrant': "Type infiltrant",
    'Stenosant': "Type sténosant", 
    'Metastases': "Métastases avérées",
    'Adenopathie': "Adénopathie"
}

@tf.keras.utils.register_keras_serializable()
def cox_loss(y_true, y_pred):
    """Fonction de perte custom pour DeepSurv"""
    # (Conserver l'implémentation existante)
    return ...  

def load_models():
    """Charge les modèles avec gestion d'erreur"""
    models = {}
    try:
        for name, path in MODELS.items():
            if path.endswith('.keras'):
                models[name] = tf.keras.models.load_model(
                    path, custom_objects={'cox_loss': cox_loss})
            else:
                models[name] = joblib.load(path)
        return models
    except Exception as e:
        st.error(f"Erreur de chargement des modèles: {str(e)}")
        return None

def create_sidebar():
    """Crée la sidebar avec formulaire"""
    with st.sidebar:
        st.title("📋 Formulaire Patient")
        inputs = {}
        for var, label in VARIABLES.items():
            inputs[var] = st.selectbox(label, ["Non", "Oui"])
        return pd.DataFrame({k: [1 if v == "Oui" else 0] for k, v in inputs.items()})

def display_predictions(models, data):
    """Affiche les résultats dans des onglets"""
    tabs = st.templates.Tabs(MODELS.keys())
    
    for i, (name, model) in enumerate(models.items()):
        with tabs[i]:
            st.header(f"Modèle {name}")
            
            try:
                if name == "DeepSurv":
                    pred = model.predict(data).flatten()[0]
                else:
                    pred = model.predict(data)[0]
                
                st.markdown(f"<div class='pred-value'>{pred:.1f} mois</div>", 
                           unsafe_allow_html=True)
                
                # Visualisation supplémentaire
                fig = px.bar(x=[pred], labels={'x':'Mois', 'y':'Survie'}, 
                            title="Prédiction de survie")
                st.plotly_chart(fig, use_container_width=True)
                
            except Exception as e:
                st.error(f"Erreur de prédiction: {str(e)}")

def main():
    """Point d'entrée principal de l'application"""
    st.title("🩺 OncoPredict - Aide à la décision clinique")
    st.markdown("---")
    
    # Chargement des données et modèles
    data = create_sidebar()
    models = load_models()
    
    if not models:
        st.stop()
    
    # Affichage principal
    display_predictions(models, data)
    
    # Section d'information
    with st.expander("📚 Documentation technique"):
        st.markdown("""
        ### Configuration technique
        - **Version**: 1.2.0
        - **Environnement** : Python 3.12
        - **Dépendances** : Voir requirements.txt
        """)

if __name__ == "__main__":
    main()
