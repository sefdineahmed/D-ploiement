import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #a855f7;
            --glass: rgba(255, 255, 255, 0.15);
        }}
        
        /* Section title avec icône flottante */
        .section-title {{
            position: relative;
            padding-left: 3rem;
            margin: 3rem 0 2rem !important;
            font-family: 'Inter', sans-serif;
            color: transparent;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            background-clip: text;
        }}
        
        .section-title::before {{
            content: '📌';
            position: absolute;
            left: 0;
            top: -3px;
            font-size: 2rem;
            filter: drop-shadow(0 2px 4px rgba(99, 102, 241, 0.3));
        }}
        
        /* Conteneur glassmorphism */
        .glass-card {{
            background: var(--glass);
            backdrop-filter: blur(16px) saturate(180%);
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.3);
            box-shadow: 0 4px 24px -6px rgba(31, 38, 135, 0.1);
            padding: 1.5rem;
            margin-bottom: 2rem;
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .glass-card:hover {{
            transform: translateY(-5px);
        }}
        
        /* Style des onglets */
        .stTabs [role="tablist"] {{
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        
        .stTabs [role="tab"] {{
            background: rgba(255,255,255,0.7)!important;
            border: 1px solid rgba(255,255,255,0.4)!important;
            border-radius: 12px!important;
            transition: all 0.3s ease!important;
        }}
        
        .stTabs [role="tab"][aria-selected="true"] {{
            background: linear-gradient(45deg, var(--primary), var(--secondary))!important;
            color: white!important;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
        }}
        
        /* Carte équipe améliorée */
        .team-card {{
            position: relative;
            padding: 1.5rem;
            border-radius: 16px;
            background: rgba(255,255,255,0.7);
            border: 1px solid rgba(255,255,255,0.4);
            transition: all 0.3s ease;
            overflow: hidden;
        }}
        
        .team-card::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: conic-gradient(
                transparent 20deg,
                rgba(99, 102, 241, 0.1) 180deg,
                transparent 200deg
            );
            animation: rotate 6s linear infinite;
        }}
        
        @keyframes rotate {{
            100% {{ transform: rotate(360deg); }}
        }}
        
        .team-card:hover {{
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        
        /* Style du code */
        .custom-pre {{
            background: rgba(0,0,0,0.05)!important;
            border: 1px solid rgba(0,0,0,0.1)!important;
            border-radius: 12px!important;
            padding: 1.5rem!important;
            font-family: 'Fira Code', monospace!important;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Section Causes
    st.markdown("<h1 class='section-title'>Causes de l'infection</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        <div class="glass-card">
            <div style="font-size: 1.1rem; line-height: 1.7; color: #4b5563;">
                <span style="font-size: 1.3rem; color: var(--primary);">🔍 Helicobacter pylori</span><br><br>
                Joue un rôle clé dans 80% des ulcères gastriques au Sénégal.<br><br>
                <strong style="color: var(--secondary);">Facteurs de risque :</strong>
                <ul style="margin-top: 0.5rem;">
                    <li>Accès limité à l'eau potable</li>
                    <li>Densité familiale élevée</li>
                    <li>Hygiène alimentaire précaire</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image(TEAM_IMG_PATH, use_container_width=True)

    # Section Transmission
    st.markdown("<h1 class='section-title'>Modes de transmission</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="glass-card" style="background: rgba(248, 250, 252, 0.6);">
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem;">
            <div>
                <h4 style="margin: 0 0 1rem; color: var(--primary);">🦠 Voies principales</h4>
                <ul style="color: #4b5563;">
                    <li>Contact oral-oral</li>
                    <li>Eau contaminée</li>
                    <li>Aliments crus</li>
                </ul>
            </div>
            <div>
                <h4 style="margin: 0 0 1rem; color: var(--primary);">📊 Statistiques</h4>
                <div style="background: rgba(99, 102, 241, 0.1); padding: 1rem; border-radius: 12px;">
                    <div style="color: var(--secondary); font-weight: bold;">Prévalence</div>
                    <div style="font-size: 2rem; color: var(--primary);">82%</div>
                    <div style="font-size: 0.9em; color: #6b7280;">chez les adultes</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Onglets interactifs
    tab1, tab2, tab3, tab4 = st.tabs(["⚠️ Symptômes", "🔬 Diagnostic", "💊 Traitements", "🛡️ Prévention"])
    with tab1:
        st.markdown(f"""
        <div class="glass-card">
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem;">
                <div>
                    <h4 style="color: var(--primary); margin: 0 0 1rem;">Signes cliniques</h4>
                    <ul style="color: #4b5563;">
                        <li>Douleurs épigastriques</li>
                        <li>Satiété précoce</li>
                        <li>Perte de poids</li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: var(--primary); margin: 0 0 1rem;">Complications</h4>
                    <ul style="color: #4b5563;">
                        <li>Ulcère gastrique</li>
                        <li>Adénocarcinome</li>
                        <li>Lymphome MALT</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Section Équipe
    st.markdown("<h1 class='section-title' style='text-align: center; margin-top: 4rem;'>👥 Équipe Scientifique</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    for member, col in zip(TEAM_MEMBERS, cols):
        with col:
            st.markdown(f"""
            <div class="team-card">
                <div style="position: relative; z-index: 1; background: white; border-radius: 12px; padding: 1rem;">
                    {st.image(member["photo"], use_container_width=True)}
                    <h3 style="text-align: center; margin: 1rem 0 0.5rem; color: var(--primary);">{member['name']}</h3>
                    <div style="text-align: center; color: var(--secondary); font-size: 0.9em;">{member['role']}</div>
                    <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 1rem;">
                        <a href="mailto:{member['email']}" style="color: var(--primary);">✉️</a>
                        <a href="{member['linkedin']}" style="color: var(--primary);">🌐</a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
