import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2563eb;
            --secondary: #1d4ed8;
            --accent: #22d3ee;
            --background: #f8fafc;
        }}
        
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            background-color: var(--background);
        }}
        
        .section-title {{
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            color: var(--primary);
            position: relative;
            padding-bottom: 1rem;
            margin: 3rem 0 2rem !important;
        }}
        
        .section-title::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            border-radius: 2px;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin: 2rem 0;
        }}
        
        .stat-card {{
            background: white;
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            text-align: center;
            transition: transform 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }}
        
        .team-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }}
        
        .team-card:hover {{
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
        }}
        
        .member-photo {{
            width: 160px;
            height: 160px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        
        .badge {{
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            background: rgba(34, 211, 238, 0.1);
            color: var(--accent);
            font-size: 0.9rem;
            margin: 0.5rem 0;
        }}
        
        .timeline {{
            position: relative;
            padding: 2rem 0;
        }}
        
        .timeline-item {{
            padding: 1.5rem;
            margin-left: 30px;
            border-left: 3px solid var(--accent);
            position: relative;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            margin-bottom: 1rem;
        }}
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        # En-tête
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0;">
            <h1 style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                Initiative Nationale de Lutte Contre H. pylori
            </h1>
            <div class="badge">Depuis 2018</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Statistiques
        st.markdown("<div class='stats-grid'>", unsafe_allow_html=True)
        stats = [
            {"value": "82%", "label": "Prévalence nationale"},
            {"value": "150k+", "label": "Patients traités"},
            {"value": "92%", "label": "Taux de succès"}
        ]
        for stat in stats:
            st.markdown(f"""
            <div class="stat-card">
                <div style="font-size: 2.5rem; font-weight: 700; color: var(--primary);">
                    {stat['value']}
                </div>
                <div style="color: #64748b; font-size: 1rem;">
                    {stat['label']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section Causes
        st.markdown("<h2 class='section-title'>Étiologie et Facteurs de Risque</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="stat-card">
                <h3 style="margin-top: 0;">Principaux déterminants</h3>
                <ul style="padding-left: 1.5rem; text-align: left;">
                    <li>Conditions socio-économiques</li>
                    <li>Accès à l'eau potable</li>
                    <li>Facteurs génétiques</li>
                </ul>
                <div class="badge">Étude SEN-HPylori 2023</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image(TEAM_IMG_PATH, use_container_width=True)
        
        # Timeline
        st.markdown("<h2 class='section-title'>Processus Infectieux</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="stat-card">
            <div class="timeline">
                <div class="timeline-item">
                    <h4>Contamination initiale</h4>
                    <p>Transmission oro-fécale ou par eau contaminée</p>
                </div>
                <div class="timeline-item">
                    <h4>Colonisation gastrique</h4>
                    <p>Adhésion à la muqueuse gastrique en 48h</p>
                </div>
                <div class="timeline-item">
                    <h4>Phase clinique</h4>
                    <p>Apparition des symptômes après 2-3 semaines</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Équipe scientifique
        st.markdown("<h2 class='section-title' style='text-align: center;'>Comité Scientifique</h2>", unsafe_allow_html=True)
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        for member in TEAM_MEMBERS:
            st.markdown(f"""
            <div class="team-card">
                <img src="{member['photo']}" class="member-photo" alt="{member['name']}">
                <h3 style="margin: 0.5rem 0; color: var(--primary);">{member['name']}</h3>
                <p style="color: #64748b; margin: 0.3rem 0;">{member['Etablissement']}</p>
                <p style="color: var(--secondary); font-weight: 500;">{member['role']}</p>
                <div style="margin: 1rem 0; font-size: 1.5rem;">
                    <a href="mailto:{member['email']}" style="color: var(--primary); margin: 0 0.5rem;">✉️</a>
                    <a href="{member['linkedin']}" style="color: var(--primary); margin: 0 0.5rem;">🔗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
