import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #1e3a8a;
            --secondary: #3b82f6;
            --accent: #10b981;
            --background: #f8fafc;
            --text: #1e293b;
        }}
        
        body {{
            background-color: var(--background);
        }}
        
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            background-color: white;
            border-radius: 16px;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
        }}
        
        .section-title {{
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            color: var(--primary);
            position: relative;
            padding-bottom: 1rem;
            margin: 3rem 0 2rem !important;
        }}
        
        .section-title:after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            border-radius: 2px;
        }}
        
        .data-card {{
            background: white;
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
            transition: transform 0.3s ease;
        }}
        
        .data-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 6px 24px rgba(0, 0, 0, 0.08);
        }}
        
        .data-card h3 {{
            color: var(--primary);
            margin-top: 0;
            font-size: 1.25rem;
        }}
        
        .data-card ul {{
            color: var(--text);
            line-height: 1.8;
        }}
        
        .timeline-item {{
            padding: 1.5rem;
            margin-left: 30px;
            border-left: 3px solid var(--accent);
            position: relative;
            background: #f1f5f9;
            border-radius: 8px;
            margin-bottom: 1rem;
        }}
        
        .team-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            text-align: center;
            border: 1px solid #e2e8f0;
        }}
        
        .team-card h3 {{
            color: var(--text);
            margin: 0.5rem 0;
        }}
        
        .badge {{
            background: rgba(16, 185, 129, 0.1);
            color: var(--accent);
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            display: inline-block;
        }}
        
        .stTabs [role="tablist"] {{
            border-bottom: 2px solid #e2e8f0;
        }}
        
        .stTabs [role="tab"] {{
            color: var(--text) !important;
            font-weight: 500;
            padding: 0.75rem 1.5rem !important;
            border-radius: 8px 8px 0 0 !important;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: var(--primary) !important;
            color: white !important;
            border-color: var(--primary);
        }}
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        # Section En-tête
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0 3rem;">
            <h1 style="font-size: 2rem; color: var(--primary); margin-bottom: 1rem;">
                Initiative Nationale de Lutte Contre H. pylori
            </h1>
            <div class="badge">Programme actif depuis 2018</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Section Statistiques (le reste du code reste similaire avec les ajustements de couleur)
        # ... (le contenu reste inchangé mais bénéficie des nouveaux styles)
        
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
