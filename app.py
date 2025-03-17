import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
import plotly.express as px
from PIL import Image

# --- Configuration de base DOIT ÊTRE LA PREMIÈRE COMMANDE STREAMLIT ---
def main():
    st.set_page_config(
        page_title="OncoPredict - Cancer Gastrique",
        page_icon="🩺",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # --- Le reste du code après set_page_config ---
    # Custom CSS
    st.markdown("""
    <style>
        .main {background: #f9f9f9;}
        .stButton>button {background-color: #4CAF50; color: white;}
        .stSelectbox label {font-weight: bold;}
        .pred-box {border-radius: 10px; padding: 20px; margin: 10px 0;}
    </style>
    """, unsafe_allow_html=True)
    
    # En-tête
    col1, col2 = st.columns([1, 3])
    with col1:
        img = Image.open("assets/medical-icon.png")
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

# --- Les autres fonctions doivent être DÉFINIES AVANT main() ---
@tf.keras.utils.register_keras_serializable()
def cox_loss(y_true, y_pred):
    # ... (même implémentation que précédemment)

def load_models():
    # ... (même implémentation que précédemment)

def user_input_sidebar():
    # ... (même implémentation que précédemment)

def display_predictions(models, data):
    # ... (même implémentation que précédemment)

def show_model_info():
    # ... (même implémentation que précédemment)

if __name__ == "__main__":
    main()  # L'appel principal DOIT ÊTRE LA DERNIÈRE LIGNE
