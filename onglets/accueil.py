import streamlit as st
import os
from utils import LOGO_PATH  # Assurez-vous que LOGO_PATH est défini dans utils.py

# CSS pour améliorer le design
st.markdown("""
    <style>
        /* Arrière-plan en mode full screen */
        .stApp {
            background: url('https://source.unsplash.com/1600x900/?medical,technology') no-repeat center center fixed;
            background-size: cover;
        }
        
        /* Conteneur principal */
        .header-section {
            padding: 3rem 2rem;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
            margin: 2rem 0;
            text-align: center;
            animation: fadeIn 1.5s ease-in-out;
        }

        /* Animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Titre stylé */
        .title-text {
            font-family: 'Poppins', sans-serif;
            color: #2e77d0;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
            font-size: 3rem;
            font-weight: bold;
        }

        /* Sous-titre */
        .subtitle-text {
            color: #333;
            font-size: 1.4rem;
            margin-top: 1rem;
            font-weight: 300;
        }

        /* Séparateur dégradé */
        .separator {
            height: 5px;
            background: linear-gradient(90deg, #2e77d0 0%, #6c757d 100%);
            margin: 2rem auto;
            width: 60%;
            border-radius: 2px;
        }

        /* Style des expandeurs */
        details summary {
            font-size: 1.2rem;
            font-weight: bold;
            color: #2e77d0;
        }
    </style>
""", unsafe_allow_html=True)

def accueil():
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
        - Visualisez les prédictions sous forme graphique 📊  
        - Téléchargez le rapport médical complet 📄  

        **3️⃣ Suivi thérapeutique**  
        - Comparez les différentes options de traitement 💊  
        - Planifiez le suivi médical automatisé 🏥  
        """)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # Ajout d'un call-to-action
    st.info("💡 **Commencez dès maintenant !** Sélectionnez une option dans le menu latéral.", icon="🚀")
