import streamlit as st
import os
from utils import LOGO_PATH  # Assurez-vous que LOGO_PATH pointe vers votre logo

# On place le CSS dès le début pour styliser toute l'application
st.markdown(
    """
    <style>
    /* Image de fond en pleine page */
    .stApp {
        background: url('https://source.unsplash.com/1600x900/?health,wellness') no-repeat center center fixed;
        background-size: cover;
    }

    /* Overlay sombre pour améliorer la lisibilité */
    .overlay {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 10px;
    }

    /* Container du header */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
    }

    /* Logo et texte en colonne */
    .header-content {
        text-align: center;
        color: #ffffff;
        animation: fadeInUp 1.5s ease-out;
    }

    /* Animation de fade in */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Style du titre */
    .header-title {
        font-family: 'Poppins', sans-serif;
        font-size: 4rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }

    /* Style du sous-titre */
    .header-subtitle {
        font-size: 1.8rem;
        font-weight: 300;
        margin-top: 1rem;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }

    /* Style des expandeurs et sections d'informations */
    .info-section {
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
        margin-top: 2rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        font-family: 'Roboto', sans-serif;
        color: #333;
    }

    /* Bouton call-to-action */
    .cta-btn {
        background: linear-gradient(135deg, #febb52, #ed4ba7);
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        color: #fff;
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 2rem;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease;
    }
    .cta-btn:hover {
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

def accueil():
    # Conteneur principal centré verticalement
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="overlay">
            <div class="header-content">
                <!-- Affichage du logo si disponible -->
                {"<img src='" + LOGO_PATH + "' style='max-width:200px; margin-bottom: 1rem;'>" if os.path.exists(LOGO_PATH) else ""}
                <h1 class="header-title">⚕️ Plateforme MED-AI</h1>
                <p class="header-subtitle">
                    Estimation intelligente du pronostic vital en oncologie digestive
                </p>
                <button class="cta-btn" onclick="window.scrollTo(0, document.body.scrollHeight)">
                    Commencez dès maintenant !
                </button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Séparateur
    st.markdown('<hr style="border: 2px solid #ffffff; width: 60%; margin: 2rem auto;">', unsafe_allow_html=True)

    # Section d'informations via un expander
    with st.expander("🚀 Comment utiliser la plateforme ?", expanded=True):
        st.markdown(
            """
            <div class="info-section">
                <h3>1️⃣ Prédiction personnalisée</h3>
                <p>
                    Accédez à l'outil de prédiction via le menu latéral et saisissez les paramètres cliniques du patient.
                </p>
                <h3>2️⃣ Analyse des résultats</h3>
                <p>
                    Visualisez les prédictions sous forme graphique 📊 et téléchargez le rapport médical complet 📄.
                </p>
                <h3>3️⃣ Suivi thérapeutique</h3>
                <p>
                    Comparez les différentes options de traitement 💊 et planifiez le suivi médical automatisé 🏥.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Call-to-action final (info) pour guider l'utilisateur
    st.info("💡 **Explorez le menu latéral pour découvrir toutes nos fonctionnalités !**", icon="🚀")

# Pour exécuter l'accueil (n'oubliez pas de l'appeler dans votre fichier principal)
if __name__ == "__main__":
    accueil()
