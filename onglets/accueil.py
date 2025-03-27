import streamlit as st
import os
from utils import LOGO_PATH  # Assurez-vous que LOGO_PATH pointe vers votre logo

# Injection de CSS pour un design moderne et immersif
st.markdown(
    """
    <style>
    /* Arrière-plan plein écran avec image dynamique */
    .stApp {
        background: url('https://source.unsplash.com/1600x900/?medical,healthcare') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* Conteneur de l'écran héros avec superposition sombre */
    .hero {
        position: relative;
        height: 100vh;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .hero::before {
        content: "";
        position: absolute;
        top: 0; left: 0;
        height: 100%;
        width: 100%;
        background: rgba(0, 0, 0, 0.5);
        z-index: 1;
    }
    
    /* Zone de contenu au centre */
    .hero-content {
        position: relative;
        z-index: 2;
        text-align: center;
        color: white;
        animation: fadeInUp 1.5s ease-in-out;
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Style du logo */
    .hero-logo {
        max-width: 150px;
        margin-bottom: 1rem;
    }
    
    /* Titres et sous-titres */
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 4rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.3);
    }
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        margin-bottom: 2rem;
    }
    
    /* Bouton d'appel à l'action */
    .hero-button {
        background: linear-gradient(45deg, #ed4ba7, #febb52);
        border: none;
        border-radius: 50px;
        padding: 0.8rem 2rem;
        color: white;
        font-size: 1.2rem;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .hero-button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    
    /* Séparateur élégant */
    .separator {
        height: 5px;
        background: linear-gradient(90deg, #ed4ba7 0%, #febb52 100%);
        width: 60%;
        margin: 2rem auto;
        border-radius: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def accueil():
    # Bloc héro pour une immersion totale
    st.markdown(
        """
        <div class="hero">
          <div class="hero-content">
            <!-- Affichage du logo si disponible -->
            {logo}
            <h1 class="hero-title">⚕️ Plateforme MED-AI</h1>
            <p class="hero-subtitle">
                Estimation intelligente du pronostic vital en oncologie digestive
            </p>
            <button class="hero-button" onclick="window.location.href='#menu'">
                Commencez dès maintenant !
            </button>
          </div>
        </div>
        """.format(
            logo=(
                f'<img class="hero-logo" src="{LOGO_PATH}" alt="Logo MED-AI">'
                if os.path.exists(LOGO_PATH)
                else ""
            )
        ),
        unsafe_allow_html=True,
    )
    
    # Séparateur décoratif
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
    
    # Section d'explication interactive sur l'utilisation de la plateforme
    st.markdown(
        """
        <div style="text-align: center; color: white;">
            <h2 style="font-family: 'Poppins', sans-serif;">Comment utiliser la plateforme ?</h2>
            <p style="font-size: 1.1rem; max-width: 800px; margin: auto;">
                <strong>1️⃣ Prédiction personnalisée :</strong> Accédez à l'outil de prédiction via le menu latéral et saisissez les paramètres cliniques du patient.<br><br>
                <strong>2️⃣ Analyse des résultats :</strong> Visualisez les prédictions sous forme graphique 📊 et téléchargez le rapport médical complet 📄.<br><br>
                <strong>3️⃣ Suivi thérapeutique :</strong> Comparez les différentes options de traitement 💊 et planifiez le suivi médical automatisé 🏥.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Message d'invitation à explorer l'application
    st.info("💡 **Explorez notre plateforme** via le menu latéral pour découvrir tous nos outils interactifs.", icon="🚀")

# Pour tester localement, appelez la fonction accueil()
if __name__ == "__main__":
    accueil()
