import streamlit as st
import os
from utils import LOGO_PATH  # Assurez-vous que LOGO_PATH est défini dans utils.py

# Injecter le CSS pour le design
st.markdown("""
<style>
/* Global styles */
body {
    margin: 0;
    padding: 0;
    font-family: 'Roboto', sans-serif;
}
.stApp {
    background: 
      linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
      url('https://source.unsplash.com/1600x900/?medical,technology') no-repeat center center fixed;
    background-size: cover;
}

/* Header container */
.header-container {
    display: flex;
    align-items: center;
    justify-content: space-around;
    padding: 4rem 2rem;
    background: rgba(255, 255, 255, 0.85);
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    animation: fadeIn 1.5s ease-in-out;
}

/* Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Logo styling */
.logo {
    max-width: 200px;
}

/* Title and subtitle */
.title {
    font-size: 3.5rem;
    color: #2A4EEF;
    margin-bottom: 0.5rem;
}
.subtitle {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 1rem;
}

/* Separator */
.separator {
    height: 5px;
    width: 60%;
    background: linear-gradient(90deg, #2A4EEF, #6c757d);
    margin: 2rem auto;
    border-radius: 2px;
}

/* Call-to-action button */
.cta-button {
    background: linear-gradient(90deg, #2A4EEF, #6c757d);
    color: white;
    padding: 1rem 2rem;
    font-size: 1.25rem;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}
.cta-button:hover {
    transform: scale(1.05);
}

/* Info box */
.info-box {
    background: rgba(255, 255, 255, 0.9);
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    margin-top: 2rem;
    text-align: center;
    font-size: 1.25rem;
}
</style>
""", unsafe_allow_html=True)

def accueil():
    with st.container():
        st.markdown('<div class="header-container">', unsafe_allow_html=True)
        
        # Affichage du logo s'il existe
        if os.path.exists(LOGO_PATH):
            st.markdown(f'<img class="logo" src="{LOGO_PATH}">', unsafe_allow_html=True)
        else:
            st.markdown('<h1 class="title">MED-AI</h1>', unsafe_allow_html=True)
        
        # Titre et call-to-action
        st.markdown("""
        <div style="text-align: center;">
            <h1 class="title">⚕️ Plateforme MED-AI</h1>
            <p class="subtitle">Estimation intelligente du pronostic vital en oncologie digestive</p>
            <button class="cta-button" onclick="window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});">
                Commencez dès maintenant
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
    
    with st.expander("🚀 Comment utiliser la plateforme ?", expanded=True):
        st.markdown("""
        <ul style="font-size: 1.25rem; line-height: 1.6;">
            <li><strong>1️⃣ Prédiction personnalisée :</strong> Accédez à l'outil de prédiction via le menu latéral et saisissez les paramètres cliniques du patient.</li>
            <li><strong>2️⃣ Analyse des résultats :</strong> Visualisez les prédictions sous forme graphique et téléchargez le rapport médical complet.</li>
            <li><strong>3️⃣ Suivi thérapeutique :</strong> Comparez les différentes options de traitement et planifiez le suivi médical automatisé.</li>
        </ul>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="info-box">💡 Découvrez nos outils innovants et transformez votre approche de la santé dès aujourd’hui !</div>', unsafe_allow_html=True)
