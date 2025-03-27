import streamlit as st
import os
from utils import LOGO_PATH  # Assurez-vous que LOGO_PATH est défini dans utils.py

# CSS pour améliorer le design
st.markdown("""
    <style>
        /* Arrière-plan avec un effet de parallax */
        .stApp {
            background: url('https://source.unsplash.com/1600x900/?medical,technology') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Poppins', sans-serif;
            position: relative;
            height: 100vh;
        }
        
        /* Conteneur principal */
        .header-section {
            padding: 3rem 2rem;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
            margin: 2rem 0;
            text-align: center;
            animation: fadeIn 1.5s ease-in-out;
        }

        /* Animation d'apparition */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Titre créatif */
        .title-text {
            font-family: 'Poppins', sans-serif;
            color: #2e77d0;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.15);
            font-size: 3.5rem;
            font-weight: bold;
            animation: slideIn 1s ease-out;
        }

        /* Animation du titre */
        @keyframes slideIn {
            from { transform: translateX(-30px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        /* Sous-titre avec effet de texte dégradé */
        .subtitle-text {
            color: #333;
            font-size: 1.5rem;
            margin-top: 1rem;
            font-weight: 300;
            background: linear-gradient(90deg, #2e77d0, #6c757d);
            -webkit-background-clip: text;
            color: transparent;
        }

        /* Séparateur dégradé moderne */
        .separator {
            height: 5px;
            background: linear-gradient(90deg, #2e77d0, #6c757d);
            margin: 2rem auto;
            width: 60%;
            border-radius: 50px;
        }

        /* Expandeur interactif avec un design moderne */
        details summary {
            font-size: 1.3rem;
            font-weight: bold;
            color: #2e77d0;
            cursor: pointer;
            transition: color 0.3s ease;
        }

        details summary:hover {
            color: #1d5ba6;
        }

        /* Call-to-action button */
        .cta-button {
            padding: 1rem 2rem;
            background-color: #2e77d0;
            color: white;
            font-size: 1.3rem;
            border-radius: 30px;
            text-align: center;
            margin-top: 20px;
            display: inline-block;
            text-decoration: none;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s ease;
        }

        .cta-button:hover {
            background-color: #1d5ba6;
            cursor: pointer;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        }

        /* Design du message d'encouragement */
        .info-message {
            background-color: #f7f7f7;
            border-left: 5px solid #2e77d0;
            padding: 1rem 2rem;
            font-size: 1.1rem;
            margin-top: 2rem;
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

    # Call-to-action button
    st.markdown('<a href="#" class="cta-button">💡 Commencez dès maintenant !</a>', unsafe_allow_html=True)

    # Message d'encouragement
    st.markdown('<div class="info-message">💡 **Commencez dès maintenant !** Sélectionnez une option dans le menu latéral.</div>', unsafe_allow_html=True)
