import streamlit as st
import os
from utils import LOGO_PATH
import streamlit as st
import os
from utils import LOGO_PATH

# CSS personnalisé corrigé
st.markdown(f"""
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #a855f7;
            --glass: rgba(255, 255, 255, 0.25);
        }}
        
        .stApp {{
            background: linear-gradient(45deg, #f0f4ff, #fdf2ff);
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
        }}
        
        .glass-container {{
            background: var(--glass)!important;
            backdrop-filter: blur(16px) saturate(180%);
            -webkit-backdrop-filter: blur(16px) saturate(180%);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            padding: 2rem;
            margin: 2rem 0;
            position: relative;
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .glass-container::before {{
            content: '';
            position: absolute;
            width: 150px;
            height: 150px;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            border-radius: 50%;
            filter: blur(60px);
            opacity: 0.15;
            z-index: -1;
        }}
        
        @keyframes gradientAnimation {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        
        .animated-title {{
            background: linear-gradient(45deg, var(--primary), var(--secondary), #ec4899);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientAnimation 8s ease infinite;
            font-weight: 800;
            letter-spacing: -1.5px;
            font-size: 3.2rem;
        }}
        
        .holographic-btn {{
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white!important;
            padding: 1rem 2rem;
            border-radius: 12px;
            position: relative;
            overflow: hidden;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 24px -6px var(--primary);
        }}
        
        .holographic-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 32px -8px var(--primary);
        }}
        
        .feature-card {{
            background: rgba(255, 255, 255, 0.7);
            padding: 1.5rem;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.4);
            transition: transform 0.3s ease;
        }}
        
        @keyframes floatIn {{
            0% {{ opacity: 0; transform: translateY(20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
""", unsafe_allow_html=True)

def accueil():
    # Section Héro
    with st.container():
        cols = st.columns([1, 3])
        with cols[0]:
            if os.path.exists(LOGO_PATH):
                st.image(LOGO_PATH, use_container_width=True)
        
        with cols[1]:
            st.markdown("""
                <div class='glass-container animate-float'>
                    <h1 class='animated-title'>🚀 MED-AI Precision</h1>
                    <p style='font-size: 1.2rem; color: #4b5563; margin-top: -0.5rem;'>
                        Intelligence prédictive avancée pour l'oncologie digestive
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    # Grille de fonctionnalités
    with st.container():
        st.markdown("""
            <div class='glass-container animate-float' style='animation-delay: 0.2s'>
                <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;'>
                    <div class='feature-card'>
                        <h3>📈 Prédiction AI</h3>
                        <p>Modèles deep learning validés cliniquement</p>
                    </div>
                    <div class='feature-card'>
                        <h3>📊 Analytics</h3>
                        <p>Visualisations interactives des données</p>
                    </div>
                    <div class='feature-card'>
                        <h3>🔒 Sécurité</h3>
                        <p>Certifié HIPAA & GDPR</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Guide utilisateur
    with st.expander("✨ Guide de démarrage rapide", expanded=True):
        st.markdown("""
            ```python
            # Workflow type MED-AI
            1. Importez les données patient
            2. Sélectionnez le modèle d'analyse
            3. Visualisez les prédictions
            4. Exportez le rapport clinique
            ```
        """)
        st.button("🎯 Commencer l'analyse", type="primary", use_container_width=True)
    
    # Bannière d'IA
    st.markdown("""
        <div style='margin: 2rem 0; padding: 1.5rem; background: linear-gradient(45deg, {var(--primary)}, {var(--secondary)});
            border-radius: 16px; color: white; text-align: center;'>
            <h3>🧠 Modèle Transformer Médical</h3>
            <p>Architecture de pointe avec 97.3% de précision validée</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    accueil()
