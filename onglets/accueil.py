import streamlit as st
import os
from utils import LOGO_PATH  # Assurez-vous que LOGO_PATH est défini dans utils.py

# CSS personnalisé pour un design moderne et interactif
st.markdown("""
    <style>
        /* Arrière-plan en pleine page avec overlay dégradé */
        .stApp {
            background: 
                linear-gradient(135deg, rgba(42, 78, 239, 0.6), rgba(255, 189, 105, 0.6)),
                url('https://source.unsplash.com/1600x900/?medical,technology');
            background-size: cover;
            background-position: center;
        }
        
        /* Conteneur central pour le header */
        .header-container {
            margin: 5rem auto;
            padding: 2rem 3rem;
            background: rgba(255,255,255,0.95);
            border-radius: 20px;
            text-align: center;
            max-width: 800px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            animation: fadeIn 1.5s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .title-text {
            font-family: 'Poppins', sans-serif;
            font-size: 3.5rem;
            color: #2a4eef;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        }

        .subtitle-text {
            font-family: 'Roboto', sans-serif;
            font-size: 1.5rem;
            color: #333;
            margin-bottom: 2rem;
        }

        /* Bouton d'appel à l'action stylé */
        .cta-button {
            background: linear-gradient(45deg, #fe7f00, #ffbd69);
            border: none;
            border-radius: 50px;
            color: white;
            font-size: 1.2rem;
            padding: 0.8rem 2rem;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .cta-button:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        }

        .separator {
            height: 4px;
            width: 50%;
            background: linear-gradient(90deg, #2a4eef, #ffbd69);
            margin: 2rem auto;
            border-radius: 2px;
        }

        /* Boîte d'informations sous le header */
        .info-box {
            background: rgba(255,255,255,0.9);
            padding: 1.5rem 2rem;
            border-radius: 15px;
            margin: 2rem auto;
            max-width: 700px;
            text-align: left;
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
    </style>
""", unsafe_allow_html=True)

def accueil():
    # Affichage du logo en haut (si disponible)
    with st.container():
        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, width=150)

    # Section principale avec le titre, sous-titre et bouton d'appel à l'action
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="title-text">⚕️ Bienvenue sur MED-AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Estimation intelligente du pronostic vital en oncologie digestive</p>', unsafe_allow_html=True)
    st.markdown(
        '<button class="cta-button" onclick="window.location.href=\'#\'">Commencez dès maintenant</button>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Séparateur décoratif
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # Boîte d'informations présentant les points forts de la plateforme
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("<strong>Prédiction personnalisée :</strong> Accédez à l'outil de prédiction via le menu latéral et saisissez les paramètres cliniques du patient.", unsafe_allow_html=True)
    st.markdown("<br><br><strong>Analyse des résultats :</strong> Visualisez les prédictions sous forme graphique et téléchargez un rapport médical complet.", unsafe_allow_html=True)
    st.markdown("<br><br><strong>Suivi thérapeutique :</strong> Comparez les différentes options de traitement et planifiez le suivi médical automatisé.", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
