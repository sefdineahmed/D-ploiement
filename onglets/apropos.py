import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2563eb;
            --secondary: #1e40af;
            --accent: #22d3ee;
            --background: #f8fafc;
            --container: rgba(255, 255, 255, 0.95);
            --text: #1e293b;
        }}
        
        body {{
            background-color: var(--background);
        }}
        
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            background-color: var(--background);
        }}
        
        .data-card {{
            background: var(--container);
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #e2e8f0;
            color: var(--text);
            transition: transform 0.3s ease;
        }}
        
        .data-card h3, .data-card h4 {{
            color: var(--primary);
        }}
        
        .timeline-item {{
            background: var(--container);
            padding: 1.5rem;
            margin-left: 30px;
            border-left: 3px solid var(--accent);
            position: relative;
        }}
        
        .team-card {{
            background: var(--container);
            padding: 1.5rem;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid #e2e8f0;
            color: var(--text);
        }}
        
        .badge {{
            background: rgba(34, 211, 238, 0.1);
            color: var(--secondary);
            border: 1px solid var(--accent);
        }}
        
        .stTabs [role="tab"] {{
            background: #e2e8f0 !important;
            color: var(--text) !important;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: var(--primary) !important;
            color: white !important;
        }}
        
        ul, ol {{
            color: var(--text);
        }}
        
        pre {{
            background: #f1f5f9 !important;
            border: 1px solid #cbd5e1 !important;
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
