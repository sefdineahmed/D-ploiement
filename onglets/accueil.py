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
            font-family: 'Poppins', sans-serif;
        }
        
        /* Conteneur principal */
        .header-section {
            padding: 3rem 2rem;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
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
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.15);
            font-size: 3.5rem;
            font-weight: 700;
        }

        /* Sous-titre */
        .subtitle-text {
            color: #333;
            font-size: 1.5rem;
            margin-top: 1rem;
            font-weight: 400;
            line-height: 1.5;
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
            font-size: 1.3rem;
            font-weight: bold;
            color: #2e77d0;
        }

        /* Call-to-action button */
        .cta-button {
            padding: 1rem 2.5rem;
            background-color: #2e77d0;
            color: white;
            font-size: 1.3rem;
            border-radius: 30px;
            text-align: center;
            margin-top: 30px;
            display: inline-block;
            text-decoration: none;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease-in-out;
        }

        .cta-button:hover {
            background-color: #1d5ba6;
            cursor: pointer;
            transform: translateY(-5px);
        }

        .cta-button:active {
            background-color: #154b7b;
            transform: translateY(2px);
        }

        /* Effet de survol pour l'image du logo */
        .logo-img:hover {
            transform: scale(1.05);
            transition: transform 0.3s ease-in-out;
        }

        /* Style de la section "Comment utiliser" */
        .usage-section {
            padding: 1.5rem;
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
        }

        .usage-section h4 {
            font-size: 1.6rem;
            font-weight: 600;
            color: #2e77d0;
        }

        .usage-section ul {
            margin-left: 1.5rem;
            font-size: 1.1rem;
            line-height: 1.8;
        }

        .usage-section li {
            color: #333;
        }

        /* Message d'encouragement */
        .info-message {
            background-color: #f1f8ff;
            color: #2e77d0;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            font-size: 1.1rem;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

def accueil():
    with st.container():
        col1, col2 = st.columns([1, 3])

        with col1:
            if os.path.exists(LOGO_PATH):
                st.image(LOGO_PATH, use_container_width=True, class_="logo-img")

        with col2:
            st.markdown('<div class="header-section">', unsafe_allow_html=True)
            st.markdown('<h1 class="title-text">⚕️ Plateforme MED-AI</h1>', unsafe_allow_html=True)
            st.markdown('<p class="subtitle-text">Estimation intelligente du pronostic vital en oncologie digestive</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    with st.expander("🚀 Comment utiliser la plateforme ?", expanded=True):
        st.markdown("""
        <div class="usage-section">
            <h4>1️⃣ Prédiction personnalisée</h4>
            <ul>
                <li>Accédez à l'outil de prédiction via le menu latéral</li>
                <li>Saisissez les paramètres cliniques du patient</li>
            </ul>

            <h4>2️⃣ Analyse des résultats</h4>
            <ul>
                <li>Visualisez les prédictions sous forme graphique 📊</li>
                <li>Téléchargez le rapport médical complet 📄</li>
            </ul>

            <h4>3️⃣ Suivi thérapeutique</h4>
            <ul>
                <li>Comparez les différentes options de traitement 💊</li>
                <li>Planifiez le suivi médical automatisé 🏥</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # Call-to-action button
    st.markdown('<a href="#" class="cta-button">💡 Commencez dès maintenant !</a>', unsafe_allow_html=True)

    # Message d'encouragement
    st.markdown('<div class="info-message">💡 **Commencez dès maintenant !** Sélectionnez une option dans le menu latéral.</div>', unsafe_allow_html=True)
