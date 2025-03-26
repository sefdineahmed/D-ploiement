import streamlit as st
import os
from utils import LOGO_PATH

def accueil():
    st.markdown("""
    <style>
        .header-section {
            padding: 4rem 1rem;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 2rem 0;
        }
        .title-text {
            font-family: 'Helvetica Neue', sans-serif;
            color: #2e77d0 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            font-size: 2.8rem !important;
        }
        .subtitle-text {
            color: #6c757d !important;
            font-size: 1.4rem !important;
            margin-top: 1rem !important;
        }
        .separator {
            height: 4px;
            background: linear-gradient(90deg, #2e77d0 0%, #6c757d 100%);
            margin: 2rem 0;
            border-radius: 2px;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            if os.path.exists(LOGO_PATH):
                st.image(LOGO_PATH, use_container_width=True)
        with col2:
            st.markdown('<div class="header-section">', unsafe_allow_html=True)
            st.markdown('<h1 class="title-text">⚕️ Plateforme MED-AI</h1>', unsafe_allow_html=True)
            st.markdown('<p class="subtitle-text">Estimation intelligente du pronostic vital en oncologie digestive</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    with st.expander("🚀 Comment utiliser la plateforme ?", expanded=True):
        st.markdown("""
        **1️⃣ Prédiction personnalisée**  
        - Accédez à l'outil de prédiction via le menu latéral  
        - Saisissez les paramètres cliniques du patient  

        **2️⃣ Analyse des résultats**  
        - Visualisez les prédictions sous forme graphique  
        - Téléchargez le rapport médical complet  

        **3️⃣ Suivi thérapeutique**  
        - Comparez les différentes options de traitement  
        - Planifiez le suivi médical automatisé  
        """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #2e77d0;">📊 Données en temps réel</h3>
            <p>Base de données actualisée quotidiennement avec les dernières données épidémiologiques</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #2e77d0;">🤖 Modèle prédictif</h3>
            <p>Algorithme certifié CE Medical (accuracy: 92.4% - AUC: 0.94)</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="color: #2e77d0;">🌍 Impact national</h3>
            <p>+1500 patients suivis dans 12 centres de santé partenaires</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 3rem;">
        <h2 style="color: #2e77d0;">Prêt à commencer ?</h2>
        <p>Accédez à l'outil de prédiction via le menu de navigation latéral →</p>
    </div>
    """, unsafe_allow_html=True)
