import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2563eb;
            --secondary: #1d4ed8;
            --accent: #3b82f6;
            --text: #1e293b;
        }}
        
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .section-header {{
            font-family: 'Inter', sans-serif;
            font-size: 2.5rem;
            color: var(--primary);
            position: relative;
            padding-bottom: 1rem;
            margin: 3rem 0 2rem;
        }}
        
        .section-header:after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 70px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border-radius: 2px;
        }}
        
        .data-card {{
            background: white;
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 4px 24px -6px rgba(37, 99, 235, 0.1);
            transition: transform 0.3s ease;
            border: 1px solid #e2e8f0;
        }}
        
        .data-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 32px -8px rgba(37, 99, 235, 0.15);
        }}
        
        .biography-card {{
            background: linear-gradient(135deg, #f8fafc, #f1f5f9);
            border-left: 4px solid var(--primary);
            padding: 1.5rem;
            border-radius: 8px;
        }}
        
        .stat-badge {{
            background: var(--primary);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 50px;
            font-size: 0.9rem;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        .timeline {{
            position: relative;
            padding-left: 30px;
            margin: 2rem 0;
        }}
        
        .timeline:before {{
            content: '';
            position: absolute;
            left: 6px;
            top: 0;
            height: 100%;
            width: 2px;
            background: #cbd5e1;
        }}
        
        .timeline-item {{
            position: relative;
            margin-bottom: 2rem;
            padding-left: 2rem;
        }}
        
        .timeline-marker {{
            position: absolute;
            left: -8px;
            top: 5px;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: var(--primary);
            border: 3px solid white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }}
        
        .code-block {{
            background: #1e293b;
            color: #f8fafc;
            padding: 1.5rem;
            border-radius: 8px;
            font-family: 'Fira Code', monospace;
            position: relative;
        }}
        
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }}
        
        .member-card {{
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 16px;
            transition: all 0.3s ease;
        }}
        
        .member-card img {{
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
            margin: 0 auto 1rem;
            border: 3px solid var(--primary);
        }}
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        # Section Épidémiologie
        st.markdown("<h2 class='section-header'>📊 Épidémiologie Régionale</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class='data-card'>
                <h3 style='margin-top:0;color:var(--text)'>Répartition des Cas</h3>
                <div class='timeline'>
                    <div class='timeline-item'>
                        <div class='timeline-marker'></div>
                        <h4>Dakar</h4>
                        <div class='stat-badge'>📌 Prévalence: 82%</div>
                        <p style='color:#64748b'>Population urbaine à risque élevé</p>
                    </div>
                    <div class='timeline-item'>
                        <div class='timeline-marker'></div>
                        <h4>Thiès</h4>
                        <div class='stat-badge'>📌 Prévalence: 78%</div>
                        <p style='color:#64748b'>Facteurs environnementaux dominants</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class='data-card' style='height:100%'>
                <h3 style='margin-top:0;color:var(--text)'>Démographie Clinique</h3>
                <div class='biography-card'>
                    <p>🏥 <strong>Population étudiée:</strong> 2 450 patients</p>
                    <p>📅 <strong>Période:</strong> 2019-2023</p>
                    <p>🔍 <strong>Méthodologie:</strong> Étude multicentrique randomisée</p>
                </div>
                <img src='{TEAM_IMG_PATH}' style='width:100%;border-radius:12px;margin-top:1rem;'>
            </div>
            """, unsafe_allow_html=True)
        
        # Section Protocole Clinique
        st.markdown("<h2 class='section-header'>🩺 Protocole Médical</h2>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["Diagnostic", "Thérapie", "Suivi", "Statistiques"])
        
        with tab1:
            st.markdown("""
            <div class='data-card'>
                <h4>Arbre Décisionnel</h4>
                <div class='biography-card'>
                    <p>1. Test non invasif primaire</p>
                    <p>2. Endoscopie si facteurs de risque</p>
                    <p>3. Biopsie selon protocole Sydney</p>
                </div>
                <div class='stat-badge' style='background:#3b82f6'>🎯 Sensibilité: 98%</div>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("""
            <div class='data-card'>
                <div class='code-block'>
                    protocol = {{
                        "phase": "Traitement Triple",
                        "durée": "14 jours",
                        "composition": [
                            "Oméprazole 20mg",
                            "Amoxicilline 1g",
                            "Clarithromycine 500mg"
                        ],
                        "succès": "89% (2023)"
                    }}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("""
            <div class='data-card'>
                <h4>Suivi Post-Thérapie</h4>
                <div class='timeline'>
                    <div class='timeline-item'>
                        <div class='timeline-marker'></div>
                        <h4>J30</h4>
                        <p>Contrôle sérologique</p>
                    </div>
                    <div class='timeline-item'>
                        <div class='timeline-marker'></div>
                        <h4>M6</h4>
                        <p>Endoscopie de contrôle</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with tab4:
            st.markdown("""
            <div class='data-card'>
                <div style='display:grid;gap:1rem;'>
                    <div class='stat-badge' style='background:#10b981'>✅ Succès: 92%</div>
                    <div class='stat-badge' style='background:#ef4444'>⚠️ Résistance: 18%</div>
                    <div class='stat-badge' style='background:#f59e0b'>🔄 Réinfection: 5%</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Section Équipe
        st.markdown("<h2 class='section-header'>👨⚕️ Équipe de Recherche</h2>", unsafe_allow_html=True)
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        for member in TEAM_MEMBERS:
            st.markdown(f"""
            <div class='member-card'>
                <img src='{member["photo"]}'>
                <h3 style='margin:0.5rem 0;color:var(--text)'>{member['name']}</h3>
                <p style='color:#64748b;margin:0'>{member['role']}</p>
                <div style='margin-top:1rem;display:flex;gap:0.5rem;justify-content:center'>
                    <a href='mailto:{member['email']}' style='color:var(--primary)'>📧</a>
                    <a href='{member['linkedin']}' style='color:var(--primary)'>🔗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
