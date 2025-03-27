import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #8b5cf6;
            --accent: #ec4899;
            --glass: rgba(255, 255, 255, 0.7);
        }}

        .section-title {{
            font-family: 'Inter', sans-serif;
            font-weight: 800;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding-bottom: 0.5rem;
            margin: 3rem 0 !important;
            position: relative;
            font-size: 2.5rem;
        }}

        .section-title::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border-radius: 2px;
        }}

        .glass-card {{
            background: var(--glass);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .glass-card:hover {{
            transform: translateY(-5px);
        }}

        .floating-badge {{
            background: linear-gradient(45deg, var(--primary), var(--accent));
            color: white !important;
            padding: 0.5rem 1.2rem;
            border-radius: 50px;
            display: inline-block;
            margin: 0.5rem 0;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }}

        .hover-zoom {{
            transition: transform 0.3s ease;
            border-radius: 12px;
            overflow: hidden;
        }}

        .hover-zoom:hover {{
            transform: scale(1.03);
        }}

        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0px); }}
        }}

        .team-card {{
            background: var(--glass);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }}

        .team-card::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(99, 102, 241, 0.1));
            transform: rotate(45deg);
        }}

        .tab-content {{
            background: var(--glass) !important;
            backdrop-filter: blur(8px);
            border-radius: 12px !important;
            margin-top: 1rem;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Section Causes
    st.markdown("<h1 class='section-title'>📚 Étiologie de l'infection</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='glass-card'>
            <div class='floating-badge'>Facteurs de risque clés</div>
            <p style='font-size: 1.1rem; line-height: 1.6;'>
                L'infection à <strong style='color: var(--primary);'>H. pylori</strong> présente une prévalence alarmante au Sénégal, avec des déterminants complexes :
            </p>
            <ul style='list-style: none; padding-left: 1rem;'>
                <li>🌍 <strong>Environnementaux :</strong> Accès limité à l'eau potable</li>
                <li>🏠 <strong>Sociaux :</strong> Promiscuité familiale</li>
                <li>🥦 <strong>Nutritionnels :</strong> Régime pauvre en antioxydants</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='hover-zoom'>{st.image(TEAM_IMG_PATH, use_container_width=True)}</div>", unsafe_allow_html=True)

    # Section Transmission
    st.markdown("<h1 class='section-title'>🦠 Dynamique de transmission</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='glass-card'>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;'>
            <div style='padding: 1rem; border-left: 4px solid var(--primary);'>
                <h4 style='margin: 0;'>Voie oro-fécale</h4>
                <p style='color: #666;'>Eau contaminée<br>Hygiène alimentaire</p>
            </div>
            <div style='padding: 1rem; border-left: 4px solid var(--secondary);'>
                <h4 style='margin: 0;'>Transmission intrafamiliale</h4>
                <p style='color: #666;'>Partage d'ustensiles<br>Contact rapproché</p>
            </div>
        </div>
        <div class='floating-badge' style='margin-top: 1rem;'>Prévalence : 82% (IC 95% : 76-88%)</div>
    </div>
    """, unsafe_allow_html=True)

    # Onglets interactifs
    tab1, tab2, tab3, tab4 = st.tabs(["🚨 Symptomatologie", "🔍 Diagnostic", "💊 Protocoles", "🛡️ Prévention"])
    with tab1:
        st.markdown("""
        <div class='tab-content'>
            <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;'>
                <div>
                    <h4 style='color: var(--primary);'>Manifestations typiques</h4>
                    <ul>
                        <li>Dyspepsie persistante</li>
                        <li>Pyrosis récurrent</li>
                        <li>Anémie ferriprive</li>
                    </ul>
                </div>
                <div>
                    <h4 style='color: var(--secondary);'>Signes d'alarme</h4>
                    <ul>
                        <li>Hématémèse</li>
                        <li>Perte de poids >10%</li>
                        <li>Dysphagie progressive</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ... (les autres onglets avec un style similaire)

    # Section Équipe
    st.markdown("<h1 class='section-title' style='text-align: center;'>👥 Équipe de Recherche</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    for member, col in zip(TEAM_MEMBERS, cols):
        with col:
            st.markdown(f"""
            <div class='team-card'>
                <div class='hover-zoom' style='border-radius: 12px;'>
                    {st.image(member["photo"], use_container_width=True)}
                </div>
                <h3 style='margin: 0.5rem 0; color: var(--primary);'>{member['name']}</h3>
                <p style='color: var(--secondary); margin: 0;'>{member['role']}</p>
                <div style='margin: 1rem 0;'>
                    <a href='mailto:{member['email']}' style='text-decoration: none; margin: 0 0.5rem;'>
                        <span style='padding: 0.5rem; background: rgba(99, 102, 241, 0.1); border-radius: 50%;'>📧</span>
                    </a>
                    <a href='{member['linkedin']}' style='text-decoration: none; margin: 0 0.5rem;'>
                        <span style='padding: 0.5rem; background: rgba(139, 92, 246, 0.1); border-radius: 50%;'>🔗</span>
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)
