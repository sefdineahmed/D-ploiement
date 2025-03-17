import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
import plotly.express as px
from PIL import Image

# Custom loss function for DeepSurv
@tf.keras.utils.register_keras_serializable()
def cox_loss(y_true, y_pred):
    # [Conserver la même implémentation...]

# Configuration
MODELS = {
    "Cox PH": "models/coxph.joblib",
    "Random Survival Forest": "models/rsf.joblib",
    "GBST": "models/gbst.joblib",
    "DeepSurv": "models/deepsurv.keras"
}

FEATURES = { ... }  # Conserver la même configuration

def load_models():
    # [Conserver la même implémentation...]

def user_input_sidebar():
    # [Conserver la même implémentation...]

def display_predictions(models, data):
    # [Conserver la même implémentation...]

def show_model_info():
    # [Conserver la même implémentation...]

def main():
    # --- CONFIGURATION DE LA PAGE EN PREMIER ---
    st.set_page_config(
        page_title="OncoPredict - Cancer Gastrique",
        page_icon="🩺",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # --- Custom CSS après set_page_config ---
    st.markdown("""
    <style>
        .main {background: #f9f9f9;}
        .stButton>button {background-color: #4CAF50; color: white;}
        .stSelectbox label {font-weight: bold;}
        .pred-box {border-radius: 10px; padding: 20px; margin: 10px 0;}
    </style>
    """, unsafe_allow_html=True)
    
    # --- Suite du code original ---
    col1, col2 = st.columns([1, 3])
    with col1:
        img = Image.open("assets/medical-icon.png")
        st.image(img, width=100)
    with col2:
        st.title("OncoPredict - Aide à la Décision")
        st.markdown("**Estimation du temps de survie post-traitement du cancer gastrique**")
    
    models = load_models()
    if not models:
        st.stop()
    
    input_data = user_input_sidebar()
    display_predictions(models, input_data)
    show_model_info()
    
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
