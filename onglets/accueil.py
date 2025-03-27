import streamlit as st
import os
from utils import LOGO_PATH

# CSS personnalisé avec design premium
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
        
        /* Fond dégradé dynamique */
        .stApp {{
            background: linear-gradient(135deg, #f3f9ff 0%, #e6f4fe 50%, #d5edff 100%);
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
        }}
        
        /* Effet de verre (glassmorphisme) */
        .glass-container {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            padding: 2rem;
            margin: 2rem 0;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }}
        
        .glass-container:before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 200%;
            height: 100%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(255, 255, 255, 0.4),
                transparent
            );
            animation: shimmer 8s infinite;
        }}
        
        @keyframes shimmer {{
            0% {{ transform: translateX(-100%); }}
            100% {{ transform: translateX(100%); }}
        }}
        
        /* Titre avec effet dégradé */
        .gradient-title {{
            background: linear-gradient(45deg, #2563eb, #7c3aed);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-weight: 700;
            font-size: 2.8rem;
            letter-spacing: -1px;
            margin-bottom: 0.5rem;
            position: relative;
            display: inline-block;
        }}
        
        .gradient-title:after {{
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: linear-gradient(45deg, #2563eb, #7c3aed);
            border-radius: 2px;
        }}
        
        /* Carte interactive */
        .feature-card {{
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(221, 221, 221, 0.3);
            cursor: pointer;
        }}
        
        .feature-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(37, 99, 235, 0.1);
        }}
        
        /* Bouton holographique */
        .holographic-button {{
            background: linear-gradient(45deg, #2563eb, #7c3aed);
            color: white !important;
            padding: 1rem 2rem;
            border-radius: 12px;
            position: relative;
            overflow: hidden;
            border: none;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-weight: 500;
        }}
        
        .holographic-button:before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                45deg,
                transparent,
                rgba(255, 255, 255, 0.3),
                transparent
            );
            transform: rotate(45deg);
            animation: hologram 3s infinite;
        }}
        
        @keyframes hologram {{
            0% {{ transform: translateX(-100%) rotate(45deg); }}
            100% {{ transform: translateX(100%) rotate(45deg); }}
        }}
        
        /* Section en retrait */
        .feature-section {{
            background: rgba(245, 248, 255, 0.6);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid rgba(37, 99, 235, 0.1);
        }}
        
        /* Animation d'icône */
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0px); }}
        }}
        
        .floating-icon {{
            animation: float 3s ease-in-out infinite;
            filter: drop-shadow(0 5px 5px rgba(37, 99, 235, 0.2));
        }}
    </style>
""", unsafe_allow_html=True)

def accueil():
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            if os.path.exists(LOGO_PATH):
                st.image(LOGO_PATH, use_container_width=True)
        
        with col2:
            st.markdown('<div class="glass-container">', unsafe_allow_html=True)
            st.markdown('<h1 class="gradient-title">🔮 MED-AI Intelligence</h1>', unsafe_allow_html=True)
            st.markdown('<p style="font-size: 1.2rem; color: #4b5563; line-height: 1.7;">Plateforme d\'intelligence artificielle médicale de nouvelle génération pour l\'oncologie digestive</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown("""
            <div class="feature-section">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
                    <div class="feature-card">
                        <h3 style="color: #2563eb; margin-bottom: 0.5rem;">🎯 Prédiction intelligente</h3>
                        <p style="color: #6b7280;">Algorithmes d'apprentissage profond entraînés sur +10M de données cliniques</p>
                    </div>
                    <div class="feature-card">
                        <h3 style="color: #7c3aed; margin-bottom: 0.5rem;">📊 Analyse visuelle</h3>
                        <p style="color: #6b7280;">Visualisations interactives et rapports personnalisés</p>
                    </div>
                    <div class="feature-card">
                        <h3 style="color: #2563eb; margin-bottom: 0.5rem;">🔒 Sécurité absolue</h3>
                        <p style="color: #6b7280;">Certification HIPAA & RGPD - Chiffrement de bout en bout</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            with st.expander("🚀 Guide de démarrage rapide", expanded=True):
                st.markdown("""
                ```python
                # Workflow type MED-AI
                1. Importez les données patient
                2. Sélectionnez le modèle d'IA
                3. Analysez les prédictions
                4. Exportez les résultats
                ```
                """)
                st.markdown('<a href="#" class="holographic-button" style="margin-top: 1rem;">📁 Télécharger le manuel</a>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div style="text-align: center; padding: 2rem;">
                    <div class="floating-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 2v20M2 12h20"/>
                        </svg>
                    </div>
                    <h3 style="color: #2563eb; margin-top: 1rem;">Nouveautés v2.1</h3>
                    <p style="color: #6b7280;">Module de suivi temps réel</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: center; margin: 3rem 0;">
            <div class="holographic-button" onclick="location.href='#'" style="margin: 0 auto;">
                🚀 Commencer l'analyse
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    accueil()
