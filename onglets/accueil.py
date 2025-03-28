import streamlit as st
import os
from utils import LOGO_PATH

# CSS personnalisé
st.markdown(f"""
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #a855f7;
            --accent: #ec4899;
            --glass: rgba(255, 255, 255, 0.25);
        }}
        
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                        url('assets/img1.avif');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Inter', sans-serif;
        }}
        
        .hero-section {{
            min-height: 80vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 4rem 0;
            position: relative;
        }}
        
        .hero-content {{
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            padding: 4rem;
            border-radius: 2rem;
            box-shadow: 0 16px 40px rgba(0,0,0,0.2);
            margin: 2rem;
        }}
        
        .main-title {{
            font-size: 4rem;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            color: transparent;
            line-height: 1.1;
            margin-bottom: 1.5rem;
            animation: fadeIn 1s ease-out;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            margin: 4rem 0;
        }}
        
        .stat-card {{
            background: var(--glass);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 1.5rem;
            border: 1px solid rgba(255,255,255,0.3);
            transition: all 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-10px);
            background: rgba(255,255,255,0.4);
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .news-card {{
            background: rgba(255,255,255,0.9);
            border-radius: 1.5rem;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        
        .partner-carousel {{
            display: flex;
            gap: 2rem;
            overflow-x: auto;
            padding: 2rem 0;
        }}
    </style>
""", unsafe_allow_html=True)

def accueil():
    # Section Héro avec image de fond
    st.markdown("""
        <div class="hero-section">
            <div class="hero-content">
                <h1 class="main-title">L'Innovation Médicale<br>Redéfinie</h1>
                <p style="font-size: 1.5rem; color: #4b5563; margin-bottom: 2rem;">
                    Plateforme IA de pointe pour la lutte contre les cancers digestifs
                </p>
                <button class="holographic-btn" style="font-size: 1.2rem;">
                    Découvrir la Technologie
                </button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Statistiques impactantes
    st.markdown("""
        <div class="stats-grid">
            <div class="stat-card">
                <h3>📈 97.3%</h3>
                <p>Précision diagnostique</p>
            </div>
            <div class="stat-card">
                <h3>⏱ 2.4x</h3>
                <p>Rapidité d'analyse accrue</p>
            </div>
            <div class="stat-card">
                <h3>👨⚕️ 150+</h3>
                <p>Cliniciens partenaires</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Section Actualités
    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
                <div class="news-card">
                    <h2>🚀 Dernières Avancées</h2>
                    <div style="margin-top: 1.5rem;">
                        <div style="padding: 1rem; background: #f8fafc; border-radius: 1rem; margin: 1rem 0;">
                            <h4>Nouveau modèle DeepSurv</h4>
                            <p>Amélioration de 15% des prédictions de survie</p>
                        </div>
                        <div style="padding: 1rem; background: #f8fafc; border-radius: 1rem; margin: 1rem 0;">
                            <h4>Partenariat avec l'OMS</h4>
                            <p>Déploiement mondial prévu pour 2024</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div class="news-card">
                    <h2>📅 Accès Rapide</h2>
                    <div style="margin-top: 1.5rem;">
                        <button class="holographic-btn" style="width: 100%; margin: 0.5rem 0;">
                            📊 Analyse des Données
                        </button>
                        <button class="holographic-btn" style="width: 100%; margin: 0.5rem 0;">
                            📚 Documentation
                        </button>
                        <button class="holographic-btn" style="width: 100%; margin: 0.5rem 0;">
                            👥 Équipe Médicale
                        </button>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Section Partenaires
    st.markdown("""
        <div style="text-align: center; margin: 4rem 0;">
            <h2>Ils Nous Font Confiance</h2>
            <div class="partner-carousel">
                <img src="https://via.placeholder.com/150x60?text=OMS" style="height: 60px;">
                <img src="https://via.placeholder.com/150x60?text=INSERM" style="height: 60px;">
                <img src="https://via.placeholder.com/150x60?text=CHU+Dakar" style="height: 60px;">
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    accueil()
