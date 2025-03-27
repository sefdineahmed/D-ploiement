import streamlit as st
import os
from utils import LOGO_PATH  # Assurez-vous que LOGO_PATH est défini dans utils.py

# Intégration de Google Fonts pour une typographie élégante
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        /* Fond avec image et overlay foncé pour améliorer la lisibilité */
        .stApp {
            background: 
                linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
                url('https://source.unsplash.com/1600x900/?medical,technology') no-repeat center center fixed;
            background-size: cover;
        }
        
        /* Conteneur principal centré et avec effet de flou léger en arrière-plan */
        .header-section {
            padding: 3rem 2rem;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
            margin: 2rem auto;
            max-width: 800px;
            text-align: center;
            animation: fadeIn 1.5s ease-in-out;
        }

        /* Animation d'apparition */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Titre principal */
        .title-text {
            font-family: 'Poppins', sans-serif;
            color: #2e77d0;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        /* Sous-titre élégant */
        .subtitle-text {
            font-family: 'Poppins', sans-serif;
            color: #333;
            font-size: 1.6rem;
            font-weight: 300;
            margin-top: 0;
            margin-bottom: 1.5rem;
        }

        /* Séparateur dégradé élégant */
        .separator {
            height: 5px;
            background: linear-gradient(90deg, #2e77d0 0%, #6c757d 100%);
            margin: 2rem auto;
            width: 60%;
            border-radius: 2px;
        }

        /* Style des expandeurs */
        details summary {
            font-family: 'Poppins', sans-serif;
            font-size: 1.2rem;
            font-weight: 600;
            color: #2e77d0;
            cursor: pointer;
        }
        
        /* Bouton d'appel à l'action */
        .cta {
            font-family: 'Poppins', sans-serif;
            background-color: #2e77d0;
            color: white;
            padding: 0.8rem 1.2rem;
            border: none;
            border-radius: 8px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .cta:hover {
            background-color: #1a5a9c;
        }
    </style>
""", unsafe_allow_html=True)

def accueil():
    with st.container():
        # Affichage du logo à gauche et le texte à droite sur grand écran
        cols = st.columns([1, 3])
        with cols[0]:
            if os.path.exists(LOGO_PATH):
                st.image(LOGO_PATH, use_column_width=True)
        with cols[1]:
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

    # Bouton d'appel à l'action centré
    st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <button class="cta" onclick="window.scrollTo(0, document.body.scrollHeight);">
                💡 Commencez dès maintenant !
            </button>
        </div>
    """, unsafe_allow_html=True)
