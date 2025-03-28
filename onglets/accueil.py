import streamlit as st
import os
from utils import LOGO_PATH

# CSS personnalisé
st.markdown(f"""
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #a855f7;
            --glass: rgba(255, 255, 255, 0.25);
        }}
        
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                        url('assets/img1.avif');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
        }}
        
        .hero-section {{
            min-height: 80vh;
            display: flex;
            align-items: center;
            padding: 4rem 2rem;
            position: relative;
        }}
        
        .hero-content {{
            backdrop-filter: blur(16px) saturate(180%);
            background: {var(--glass)};
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            padding: 4rem;
        }}
        
        .main-title {{
            font-size: 4.5rem;
            background: linear-gradient(45deg, #fff, #e0e7ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }}
        
        .feature-card {{
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 16px;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.4);
            text-align: center;
        }}
        
        .feature-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
        }}
        
        .feature-icon {{
            font-size: 3rem;
            margin-bottom: 1rem;
        }}
        
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-20px); }}
            100% {{ transform: translateY(0px); }}
        }}
        
        .floating {{
            animation: float 3s ease-in-out infinite;
        }}
    </style>
""", unsafe_allow_html=True)

def accueil():
    # Section Héro
    with st.container():
        st.markdown("<div class='hero-section'>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if os.path.exists(LOGO_PATH):
                st.image(LOGO_PATH, use_container_width=True)
        
        with col2:
            st.markdown("""
                <div class='hero-content'>
                    <h1 class='main-title'>
                        Bienvenue sur<br>
                        <span style="color: #6366f1">MED-AI Precision</span>
                    </h1>
                    <p style='font-size: 1.5rem; color: #e0e7ff; margin-bottom: 3rem;'>
                        L'innovation au service de la santé digestive
                    </p>
                    <div class='floating'>
                        <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-down">
                            <line x1="12" y1="5" x2="12" y2="19"></line>
                            <polyline points="19 12 12 19 5 12"></polyline>
                        </svg>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Section Fonctionnalités
    with st.container():
        st.markdown("<div style='padding: 4rem 2rem;'>", unsafe_allow_html=True)
        cols = st.columns(3)
        features = [
            {"icon": "🧠", "title": "Diagnostic Intelligent", "text": "Algorithmes certifiés par l'OMS"},
            {"icon": "📊", "title": "Analytique Avancée", "text": "Visualisations interactives en temps réel"},
            {"icon": "🔒", "title": "Sécurité Maximale", "text": "Certifications HIPAA & GDPR"}
        ]
        
        for col, feature in zip(cols, features):
            with col:
                st.markdown(f"""
                    <div class='feature-card'>
                        <div class='feature-icon'>{feature['icon']}</div>
                        <h3>{feature['title']}</h3>
                        <p>{feature['text']}</p>
                    </div>
                """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Section Appel à l'action
    with st.container():
        st.markdown("""
            <div style='text-align: center; padding: 6rem 2rem; background: rgba(255, 255, 255, 0.9);'>
                <h2 style='font-size: 2.5rem; margin-bottom: 2rem;'>Prêt à révolutionner votre pratique médicale ?</h2>
                <div style='display: inline-block;'>
                    <button style='
                        background: linear-gradient(45deg, #6366f1, #a855f7);
                        color: white;
                        padding: 1.5rem 3rem;
                        border: none;
                        border-radius: 50px;
                        font-size: 1.2rem;
                        cursor: pointer;
                        transition: all 0.3s ease;
                        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.3);
                    '>
                        Commencer maintenant
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    accueil()
