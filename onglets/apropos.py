import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #dc3545;
        }}
        
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .section-title {{
            font-family: 'Roboto Condensed', sans-serif;
            color: var(--primary);
            font-size: 2.5rem;
            position: relative;
            padding-bottom: 0.5rem;
            margin: 3rem 0 2rem !important;
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
        
        .data-card {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(46, 119, 208, 0.1);
            transition: transform 0.3s ease;
        }}
        
        .data-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
        }}
        
        .highlight {{
            color: var(--accent);
            font-weight: 700;
            font-size: 1.1em;
        }}
        
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }}
        
        .member-card {{
            position: relative;
            overflow: hidden;
            border-radius: 15px;
            padding: 1.5rem;
            background: white;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }}
        
        .member-photo {{
            width: 120px;
            height: 120px;
            border-radius: 50%;
            margin: 0 auto 1rem;
            object-fit: cover;
            border: 3px solid var(--primary);
        }}
        
        .badge {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: var(--accent);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8em;
        }}
        
        .stat-box {{
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1.5rem;
            background: rgba(46, 119, 208, 0.05);
            border-radius: 12px;
            margin: 1rem 0;
        }}
        
        .stat-icon {{
            font-size: 2rem;
            color: var(--primary);
        }}
    </style>
    """, unsafe_allow_html=True)

    # Section Épidémiologie
    with st.container():
        st.markdown("<h1 class='section-title'>📊 Épidémiologie Nationale</h1>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class='data-card'>
                <h3 style='color: var(--primary); margin-top:0;'>Répartition Géographique</h3>
                <div class='stat-box'>
                    <div class='stat-icon'>🌍</div>
                    <div>
                        <h4 style='margin:0;'>Prévalence Régionale</h4>
                        <p style='margin:0;'>Dakar: <span class='highlight'>82%</span> | Thiès: <span class='highlight'>78%</span><br>
                        Saint-Louis: <span class='highlight'>75%</span> | Ziguinchor: <span class='highlight'>68%</span></p>
                    </div>
                </div>
                <div class='stat-box'>
                    <div class='stat-icon'>👥</div>
                    <div>
                        <h4 style='margin:0;'>Démographie</h4>
                        <p style='margin:0;'>Âge moyen: <span class='highlight'>34 ans</span><br>
                        Ratio H/F: <span class='highlight'>1.2:1</span></p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.image(TEAM_IMG_PATH, use_container_width=True)

    # Section Stratégies
    st.markdown("<h1 class='section-title'>🛡️ Stratégies de Contrôle</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Prévention", "Diagnostic", "Traitement"])
    with tab1:
        st.markdown("""
        <div class='data-card'>
            <h4 style='color: var(--primary);'>Plan de Prévention National</h4>
            <ul>
                <li>🚰 Programme d'accès à l'eau potable</li>
                <li>🏫 Éducation sanitaire dans les écoles</li>
                <li>🏥 Dépistage communautaire gratuit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class='data-card'>
            <h4 style='color: var(--primary);'>Protocole Diagnostique</h4>
            <ol>
                <li>🔍 Test respiratoire (sensibilité 95%)</li>
                <li>🧪 Analyse sérologique</li>
                <li>📋 Évaluation endoscopique</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class='data-card'>
            <h4 style='color: var(--primary);'>Schéma Thérapeutique</h4>
            <div style='background: #f8f9fa; padding: 1rem; border-radius: 10px;'>
                <pre style='margin:0;'>
Thérapie Quadruple (14 jours):
  - Oméprazole 20mg ×2/j
  - Clarithromycine 500mg ×2/j
  - Amoxicilline 1g ×2/j
  - Métronidazole 500mg ×3/j
                </pre>
            </div>
            <p style='color: var(--accent); margin: 1rem 0 0;'>Taux de succès: 92%</p>
        </div>
        """, unsafe_allow_html=True)

    # Équipe Scientifique
    st.markdown("<h1 class='section-title'>🧑🔬 Équipe de Recherche</h1>", unsafe_allow_html=True)
    st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
    cols = st.columns(3)
    for member, col in zip(TEAM_MEMBERS, cols):
        with col:
            st.markdown(f"""
            <div class='member-card'>
                <div class='badge'>⭐ Expert</div>
                <img src='{member["photo"]}' class='member-photo'>
                <h3 style='margin: 0.5rem 0; color: var(--primary);'>{member['name']}</h3>
                <p style='color: #6c757d; margin:0;'>{member['role']}</p>
                <div style='margin: 1rem 0;'>
                    <a href='mailto:{member['email']}' target='_blank' style='color: var(--primary); margin: 0 0.5rem;'>📧</a>
                    <a href='{member['linkedin']}' target='_blank' style='color: var(--primary); margin: 0 0.5rem;'>🌐</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0; color: #6c757d;'>
        <p>© 2024 Institut National de Gastro-Entérologie du Sénégal</p>
        <div style='display: flex; justify-content: center; gap: 1rem;'>
            <a href='#' style='color: var(--primary); text-decoration: none;'>Politique de Confidentialité</a>
            <a href='#' style='color: var(--primary); text-decoration: none;'>Mentions Légales</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
