import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #10b8b8;
            --neon: #00ff88;
        }}

        .cyber-section {{
            background: linear-gradient(145deg, rgba(18,18,31,0.9), rgba(25,25,45,0.9));
            border: 2px solid var(--neon);
            border-radius: 20px;
            box-shadow: 0 0 25px rgba(0,255,136,0.2);
            padding: 2rem;
            margin: 2rem 0;
            position: relative;
            overflow: hidden;
        }}

        .cyber-section::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, var(--neon), transparent);
            animation: rotate 8s linear infinite;
            opacity: 0.1;
        }}

        @keyframes rotate {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}

        .neon-title {{
            font-family: 'Orbitron', sans-serif;
            color: var(--neon);
            text-shadow: 0 0 10px rgba(0,255,136,0.5);
            position: relative;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid var(--neon);
        }}

        .hologram-card {{
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(12px);
            border-radius: 15px;
            padding: 1.5rem;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            border: 1px solid rgba(0,255,136,0.2);
        }}

        .hologram-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 0 30px rgba(0,255,136,0.3);
            background: rgba(0,255,136,0.05);
        }}

        .cyber-tab {{
            background: rgba(16,184,184,0.1)!important;
            border: 1px solid var(--secondary)!important;
            border-radius: 8px!important;
            transition: all 0.3s ease!important;
        }}

        .cyber-tab:hover {{
            background: rgba(16,184,184,0.3)!important;
        }}

        [data-testid="stImage"] {{
            border-radius: 15px;
            border: 2px solid var(--neon)!important;
            box-shadow: 0 0 20px rgba(0,255,136,0.2);
        }}

        .neon-list li {{
            position: relative;
            padding-left: 1.5rem;
            margin: 1rem 0;
        }}

        .neon-list li::before {{
            content: "⮞";
            color: var(--neon);
            position: absolute;
            left: 0;
        }}

        .cyber-code {{
            background: rgba(0,0,0,0.7)!important;
            border: 1px solid var(--neon)!important;
            border-radius: 8px;
            padding: 1rem!important;
            font-family: 'Fira Code', monospace!important;
            color: var(--neon)!important;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Section Causes
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
            <div class='cyber-section'>
                <h1 class='neon-title'>📡 Transmission Pathogens</h1>
                <ul class='neon-list'>
                    <li><strong>Oral-Oral Contamination</strong> (Utensil sharing)</li>
                    <li><em>H2O Contaminated Sources</em></li>
                    <li>Food Safety Protocol Breach</li>
                </ul>
                <div style='color: var(--neon); margin-top: 1rem;'>
                    🔥 82% Adult Infection Rate (2024 Data)
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image(TEAM_IMG_PATH, use_container_width=True)

    # Section Diagnostic
    with st.container():
        st.markdown("""
        <div class='cyber-section' style='background: linear-gradient(145deg, rgba(16,184,184,0.1), rgba(25,25,45,0.9));'>
            <h1 class='neon-title'>🔍 Diagnostic Protocol</h1>
            <div class='hologram-card'>
                <h3 style='color: var(--neon);'>STEP 1 → Urea Breath Test</h3>
                <p style='color: #aaa;'>Sensitivity: 98.4%</p>
            </div>
            <div class='hologram-card'>
                <h3 style='color: var(--neon);'>STEP 2 → Fecal Antigen</h3>
                <p style='color: #aaa;'>Specificity: 95.2%</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Onglets Cyber
    tab1, tab2, tab3, tab4 = st.tabs(["⚡ Symptômes", "💉 Traitements", "🛡️ Prévention", "👥 Équipe"])
    with tab1:
        st.markdown("""
        <div class='cyber-section'>
            <h3 style='color: var(--secondary);'>Critical Manifestations:</h3>
            <ul class='neon-list'>
                <li>Epigastric Pain Matrix</li>
                <li>Weight Loss Anomaly</li>
                <li>Early Satiety Loop</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with tab2:
        st.markdown("""
        <div class='cyber-section'>
            <pre class='cyber-code'>
pylera_matrix = {{
    "duration": "10d",
    "components": [
        BioSubcitrate(240mg),
        Tetracycline(500mg),
        MetroNidazole(500mg)
    ],
    "efficacy": 92.7%
}}
            </pre>
        </div>
        """, unsafe_allow_html=True)
    with tab3:
        st.markdown("""
        <div class='cyber-section'>
            <div style='display: grid; gap: 1rem;'>
                <div class='hologram-card'>🔒 Family Screening Protocol</div>
                <div class='hologram-card'>💧 Water Safety Initiative</div>
                <div class='hologram-card'>🦠 Community Education Program</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with tab4:
        cols = st.columns(3)
        for member, col in zip(TEAM_MEMBERS, cols):
            with col:
                st.markdown(f"""
                <div class='hologram-card' style='text-align: center;'>
                    <img src='{member["photo"]}' style='width: 100%; border-radius: 50%; border: 2px solid var(--neon);'>
                    <h3 style='color: var(--primary); margin: 1rem 0;'>{member['name']}</h3>
                    <div style='color: var(--secondary);'>{member['role']}</div>
                    <div style='margin-top: 1rem;'>
                        <a href='{member['linkedin']}' target='_blank' style='color: var(--neon)!important;'>🖧</a>
                        <a href='mailto:{member['email']}' style='color: var(--neon)!important; margin: 0 1rem;'>✉️</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
