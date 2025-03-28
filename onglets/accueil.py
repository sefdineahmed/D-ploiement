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
            --glass: rgba(255, 255, 255, 0.2);
        }}
        
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=1920');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            min-height: 100vh;
            font-family: 'Inter', sans-serif;
        }}
        
        .hero-section {{
            backdrop-filter: blur(16px);
            background: var(--glass);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 4rem 2rem;
            margin: 4rem 0;
            position: relative;
            overflow: hidden;
        }}
        
        .hero-section::before {{
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, 
                var(--primary) 0%, 
                var(--secondary) 50%, 
                var(--accent) 100%);
            opacity: 0.1;
            z-index: -1;
            animation: rotate 20s linear infinite;
        }}
        
        @keyframes rotate {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        
        .main-title {{
            font-size: 4.5rem;
            background: linear-gradient(45deg, #fff, #e0e7ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
            text-shadow: 0 4px 12px rgba(0,0,0,0.15);
            margin-bottom: 1.5rem;
        }}
        
        .feature-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 4rem 0;
        }}
        
        .feature-card {{
            background: var(--glass);
            backdrop-filter: blur(8px);
            border-radius: 16px;
            padding: 2rem;
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .feature-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 8px 32px rgba(99, 102, 241, 0.2);
        }}
        
        .cta-button {{
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white !important;
            padding: 1.2rem 2.5rem;
            border-radius: 14px;
            font-size: 1.2rem;
            margin: 2rem auto;
            display: flex;
            align-items: center;
            transition: all 0.3s ease;
        }}
        
        .cta-button:hover {{
            transform: scale(1.05);
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
        }}
        
        .stats-container {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            margin: 4rem 0;
        }}
        
        .stat-card {{
            background: var(--glass);
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            backdrop-filter: blur(8px);
        }}
    </style>
""", unsafe_allow_html=True)

def accueil():
    # Section Héro
    with st.container():
        st.markdown("""
            <div class='hero-section'>
                <div style='text-align: center;'>
                    <h1 class='main-title'>
                        Bienvenue sur MED-AI<br>
                        <span style='font-size: 2.5rem;'>L'Intelligence Artificielle au service de la Santé</span>
                    </h1>
                    <button class='cta-button'>
                        Commencer l'Analyse ➔
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Statistiques impactantes
    st.markdown("""
        <div class='stats-container'>
            <div class='stat-card'>
                <h3 style='font-size: 2.5rem; margin: 0;'>+150k</h3>
                <p>Patients analysés</p>
            </div>
            <div class='stat-card'>
                <h3 style='font-size: 2.5rem; margin: 0;'>97.3%</h3>
                <p>Précision validée</p>
            </div>
            <div class='stat-card'>
                <h3 style='font-size: 2.5rem; margin: 0;'>24h</h3>
                <p>Support médical</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Grille de fonctionnalités
    st.markdown("""
        <div class='feature-grid'>
            <div class='feature-card'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>🧠</div>
                <h3>Diagnostic Intelligent</h3>
                <p>Algorithmes d'IA certifiés par l'OMS</p>
            </div>
            <div class='feature-card'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>📊</div>
                <h3>Analytique Avancée</h3>
                <p>Visualisations interactives en temps réel</p>
            </div>
            <div class='feature-card'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>🔒</div>
                <h3>Sécurité Totale</h3>
                <p>Certifications RGPD & HIPAA</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Section workflow
    with st.expander("🚀 Comment ça marche ?", expanded=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(LOGO_PATH, use_container_width=True)
        with col2:
            st.markdown("""
                ```python
                # Workflow MED-AI
                1. Import des données patient
                2. Analyse par intelligence artificielle
                3. Génération de rapports détaillés
                4. Recommandations thérapeutiques
                ```
            """)
            st.button("📥 Télécharger la documentation", use_container_width=True)

if __name__ == "__main__":
    accueil()
