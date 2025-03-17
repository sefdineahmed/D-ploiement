import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
import plotly.express as px
from PIL import Image

# Custom CSS
st.markdown("""
<style>
    .main {background: #f9f9f9;}
    .stButton>button {background-color: #4CAF50; color: white;}
    .stSelectbox label {font-weight: bold;}
    .pred-box {border-radius: 10px; padding: 20px; margin: 10px 0;}
</style>
""", unsafe_allow_html=True)

# Configuration
MODELS = {
    "Cox PH": "models/coxph.joblib",
    "Random Survival Forest": "models/rsf.joblib",
    "GBST": "models/gbst.joblib",
    "DeepSurv": "models/deepsurv.keras"
}

FEATURES = {
    'Cardiopathie': "Présence de cardiopathie",
    'Ulceregastrique': "Antécédents d'ulcère gastrique",
    'Douleurepigastrique': "Douleur épigastrique",
    'Ulcero-bourgeonnant': "Lésion ulcero-bourgeonnante",
    'Denutrution': "État de dénutrition",
    'Tabac': "Consommation de tabac",
    'Mucineux': "Type mucineux",
    'Infiltrant': "Type infiltrant",
    'Stenosant': "Type sténosant",
    'Metastases': "Présence de métastases",
    'Adenopathie': "Adénopathie"
}

# Custom loss function for DeepSurv
@tf.keras.utils.register_keras_serializable()
def cox_loss(y_true, y_pred):
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

def load_models():
    """Charge les modèles avec gestion d'erreur"""
    models = {}
    try:
        for name, path in MODELS.items():
            if "keras" in path:
                models[name] = tf.keras.models.load_model(
                    path, custom_objects={'cox_loss': cox_loss})
            else:
                models[name] = joblib.load(path)
        return models
    except Exception as e:
        st.error(f"Erreur de chargement des modèles: {str(e)}")
        return None

def user_input_sidebar():
    """Formulaire interactif dans la sidebar"""
    st.sidebar.header("📋 Paramètres du Patient")
    inputs = {}
    for feature, label in FEATURES.items():
        inputs[feature] = st.sidebar.radio(
            label=label,
            options=("Non", "Oui"),
            horizontal=True
        )
    return pd.DataFrame({k: [1 if v == "Oui" else 0] for k, v in inputs.items()})

def display_predictions(models, data):
    """Affiche les prédictions de manière visuelle"""
    st.header("📈 Résultats des Prédictions")
    
    predictions = {}
    for name, model in models.items():
        try:
            if "DeepSurv" in name:
                pred = model.predict(data).flatten()[0]
            else:
                pred = model.predict(data)[0]
            predictions[name] = max(round(pred, 1), 0)
        except Exception as e:
            st.error(f"Erreur avec {name}: {str(e)}")
    
    # Affichage des résultats
    cols = st.columns(4)
    colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"]
    
    for (name, pred), col, color in zip(predictions.items(), cols, colors):
        with col:
            st.markdown(
                f"<div class='pred-box' style='background-color: {color}20; border-left: 5px solid {color}'>"
                f"<h3 style='color: {color}; margin:0'>{name}</h3>"
                f"<h1 style='margin:0'>{pred} mois</h1></div>", 
                unsafe_allow_html=True
            )
    
    # Courbe de survie
    time_points = np.linspace(0, max(predictions.values())*1.2, 100)
    fig = px.line(
        x=time_points, 
        y=1 - np.exp(-0.1*time_points),
        title="Courbe de Survie Estimée",
        labels={"x": "Mois", "y": "Probabilité de Survie"}
    )
    st.plotly_chart(fig, use_container_width=True)

def show_model_info():
    """Section d'information sur les modèles"""
    with st.expander("ℹ️ À propos des modèles utilisés"):
        st.markdown("""
        **Cox PH**  
        Modèle de régression des risques proportionnels  
        *Avantages*: Interprétabilité des coefficients
        
        **Random Survival Forest**  
        Méthode ensembliste basée sur les arbres de décision  
        *Avantages*: Capture des relations non-linéaires
        
        **DeepSurv**  
        Réseau de neurones profond spécialisé en survie  
        *Avantages*: Modélisation complexe des interactions
        """)

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="OncoPredict - Cancer Gastrique",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # En-tête
    col1, col2 = st.columns([1, 3])
    with col1:
        img = Image.open("assets/medical-icon.png")  # Ajouter une icône médicale
        st.image(img, width=100)
    with col2:
        st.title("OncoPredict - Aide à la Décision")
        st.markdown("**Estimation du temps de survie post-traitement du cancer gastrique**")
    
    # Chargement des modèles
    models = load_models()
    if not models:
        st.stop()
    
    # Formulaire
    input_data = user_input_sidebar()
    
    # Affichage principal
    display_predictions(models, input_data)
    show_model_info()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        Système développé par [Votre Équipe] - 
        <a href="mailto:contact@oncopredict.sn">Contact</a> | 
        Version 1.0.0
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
