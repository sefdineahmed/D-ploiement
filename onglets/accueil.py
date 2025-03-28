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
                        url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80');
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
        }}
        
        .main-title {{
            font-size: 4.5rem;
            background: linear-gradient(45deg, var(--primary), var(--secondary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientAnimation 8s ease infinite;
            margin-bottom: 1.5rem;
            letter-spacing: -2px;
        }}
        
        @keyframes gradientAnimation {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        
        .feature-card {{
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(255, 255, 255, 0.3);
            min-height: 300px;
        }}
        
        .feature-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }}
        
        .cta-button {{
            background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
            padding: 1rem 3rem !important;
            font-size: 1.2rem !important;
            border-radius: 50px !important;
            transition: 0.3s all !important;
        }}
        
        .stats-banner {{
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            border-radius: 20px;
            padding: 2rem;
            margin: 4rem 0;
            position: relative;
            overflow: hidden;
        }}
    </style>
""", unsafe_allow_html=True)

def accueil():
    # Section Héro
    with st.container():
        st.markdown("""
            <div class='hero-section'>
                <div>
                    <h1 class='main-title'>Révolution Médicale par l'IA</h1>
                    <p style='font-size: 1.5rem; color: white; margin-bottom: 3rem;'>
                        Découvrez l'avenir du diagnostic oncologique avec notre plateforme intelligente
                    </p>
                    <div class='cta-button-container'>
                        <button class='cta-button'>Commencer l'analyse gratuite</button>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Section Fonctionnalités
    with st.container():
        cols = st.columns(3)
        features = [
            {"icon": "🧠", "title": "Diagnostic Prédictif", "text": "Algorithmes certifiés par l'OMS"},
            {"icon": "📊", "title": "Analytique Avancée", "text": "Visualisations interactives en temps réel"},
            {"icon": "🔒", "title": "Sécurité Maximale", "text": "Certifications HIPAA & GDPR"}
        ]
        
        for col, feature in zip(cols, features):
            with col:
                st.markdown(f"""
                    <div class='feature-card'>
                        <div style='font-size: 4rem; margin-bottom: 1rem;'>{feature['icon']}</div>
                        <h3 style='color: var(--primary); margin-bottom: 1rem;'>{feature['title']}</h3>
                        <p style='color: #4b5563;'>{feature['text']}</p>
                    </div>
                """, unsafe_allow_html=True)
    
    # Section Statistiques
    st.markdown("""
        <div class='stats-banner'>
            <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; color: white; text-align: center;'>
                <div>
                    <div style='font-size: 2.5rem; font-weight: bold;'>97.3%</div>
                    <div>Précision Validée</div>
                </div>
                <div>
                    <div style='font-size: 2.5rem; font-weight: bold;'>150K+</div>
                    <div>Patients Analysés</div>
                </div>
                <div>
                    <div style='font-size: 2.5rem; font-weight: bold;'>24h</div>
                    <div>Support Réactif</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Guide Utilisateur
    with st.expander("🚀 Comment ça marche ?", expanded=True):
        st.markdown("""
            <div style='padding: 2rem; background: rgba(255,255,255,0.9); border-radius: 15px;'>
                <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem;'>
                    <div style='text-align: center;'>
                        <div style='font-size: 2rem;'>1️⃣</div>
                        <h3>Import des Données</h3>
                        <p>Connectez vos sources de données médicales</p>
                    </div>
                    <div style='text-align: center;'>
                        <div style='font-size: 2rem;'>2️⃣</div>
                        <h3>Analyse Automatisée</h3>
                        <p>Notre IA traite les informations en temps réel</p>
                    </div>
                    <div style='text-align: center;'>
                        <div style='font-size: 2rem;'>3️⃣</div>
                        <h3>Résultats Intelligents</h3>
                        <p>Visualisations interactives et prédictions</p>
                    </div>
                    <div style='text-align: center;'>
                        <div style='font-size: 2rem;'>4️⃣</div>
                        <h3>Export Sécurisé</h3>
                        <p>Générez des rapports médicaux détaillés</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    accueil()
