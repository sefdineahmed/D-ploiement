import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #8b5cf6;
            --glass: rgba(255, 255, 255, 0.15);
        }}

        .section-title {{
            font-family: 'Inter', sans-serif;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding: 0.5rem 0;
            font-size: 2.5rem;
            position: relative;
            margin: 3rem 0 !important;
        }}

        .section-title::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 80px;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
        }}

        .glass-panel {{
            background: {var(--glass)};
            backdrop-filter: blur(16px) saturate(180%);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            padding: 2rem;
            margin: 2rem 0;
            transition: transform 0.3s ease;
        }}

        .glass-panel:hover {{
            transform: translateY(-5px);
        }}

        .risk-factor {{
            padding: 1.5rem;
            border-left: 4px solid var(--primary);
            background: linear-gradient(90deg, rgba(99,102,241,0.1) 0%, rgba(255,255,255,0) 100%);
            margin: 1rem 0;
        }}

        .team-card {{
            background: rgba(255, 255, 255, 0.7);
            border-radius: 15px;
            padding: 1.5rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}

        .team-card::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(99,102,241,0.1), transparent);
            transform: rotate(45deg);
            pointer-events: none;
        }}

        .tab-content {{
            background: none !important;
            border: none !important;
            padding: 0 !important;
        }}

        .stTabs [data-baseweb="tab-list"] {{
            gap: 1rem;
            margin: 2rem 0;
        }}

        .stTabs [data-baseweb="tab"] {{
            background: rgba(255,255,255,0.7) !important;
            border-radius: 10px !important;
            transition: all 0.3s ease !important;
            padding: 1rem 2rem !important;
        }}

        .stTabs [aria-selected="true"] {{
            background: var(--primary) !important;
            color: white !important;
            box-shadow: 0 4px 12px rgba(99,102,241,0.3) !important;
        }}

        .code-block {{
            background: rgba(0,0,0,0.05) !important;
            border-radius: 12px !important;
            padding: 1.5rem !important;
            border: 1px solid rgba(0,0,0,0.1) !important;
        }}

        .avatar {{
            width: 120px !important;
            height: 120px !important;
            border-radius: 50% !important;
            border: 3px solid var(--primary);
            margin: 0 auto 1rem;
            box-shadow: 0 8px 24px rgba(99,102,241,0.15);
        }}
    </style>
    """, unsafe_allow_html=True)

    # Section Causes
    st.markdown("<h1 class='section-title'>📚 Causes de l'infection</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="glass-panel">
            <div class="risk-factor">
                <h3 style="color: var(--primary); margin:0">Facteurs clés au Sénégal</h3>
                <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                    <div style="flex:1; padding:1rem; background: rgba(99,102,241,0.1); border-radius:12px">
                        🏚️ Conditions socio-économiques
                    </div>
                    <div style="flex:1; padding:1rem; background: rgba(99,102,241,0.1); border-radius:12px">
                        💧 Accès à l'eau potable
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image(TEAM_IMG_PATH, use_container_width=True)

    # Section Transmission
    st.markdown("<h1 class='section-title'>🦠 Modes de transmission</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-panel">
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;">
            <div style="text-align: center; padding:1.5rem; background: rgba(99,102,241,0.05); border-radius:12px">
                <div style="font-size:2rem">👄</div>
                Contact oral
            </div>
            <div style="text-align: center; padding:1.5rem; background: rgba(99,102,241,0.05); border-radius:12px">
                <div style="font-size:2rem">💧</div>
                Eau contaminée
            </div>
            <div style="text-align: center; padding:1.5rem; background: rgba(99,102,241,0.05); border-radius:12px">
                <div style="font-size:2rem">🍲</div>
                Hygiène alimentaire
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Onglets
    tab1, tab2, tab3, tab4 = st.tabs(["⚠️ Symptômes", "🔬 Diagnostic", "💊 Traitements", "🛡️ Prévention"])
    with tab1:
        st.markdown("""
        <div class="glass-panel">
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem;">
                <div style="padding:1rem; background: rgba(220,53,69,0.1); border-radius:12px">
                    <h4 style="color:#dc3545; margin:0">Douleurs épigastriques</h4>
                    <p style="font-size:0.9em">Récurrentes et persistantes</p>
                </div>
                <div style="padding:1rem; background: rgba(220,53,69,0.1); border-radius:12px">
                    <h4 style="color:#dc3545; margin:0">Perte de poids</h4>
                    <p style="font-size:0.9em">>10% du poids corporel</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="glass-panel">
            <div class="code-block">
                <pre style="margin:0; font-family: 'JetBrains Mono', monospace;">
pylera_treatment = {{
    "Durée": "10 jours",
    "Composition": [
        "Bismuth subcitrate",
        "Tétracycline",
        "Métronidazole",
        "Oméprazole"
    ],
    "Efficacité": "92% de succès"
}}
                </pre>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Équipe
    st.markdown("<h1 class='section-title' style='text-align:center'>👥 Équipe Scientifique</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    for member, col in zip(TEAM_MEMBERS, cols):
        with col:
            st.markdown(f"""
            <div class="team-card">
                <img class="avatar" src="{member['photo']}">
                <h3 style="text-align:center; margin:0.5rem 0; color: var(--primary)">{member['name']}</h3>
                <p style="text-align:center; color:#6c757d; margin:0">{member['role']}</p>
                <div style="display: flex; justify-content: center; gap:1rem; margin-top:1rem">
                    <a href="mailto:{member['email']}" style="color:var(--primary)">✉️</a>
                    <a href="{member['linkedin']}" style="color:var(--primary)">🔗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
