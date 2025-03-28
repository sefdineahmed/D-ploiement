import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2563eb;
            --secondary: #1d40af;
            --accent: #22d3ee;
        }}
        
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
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
        
        .data-card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.3);
            transition: transform 0.3s ease;
        }}
        
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }}
        
        .team-card {{
            background: white;
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }}
        
        .team-card:hover {{
            transform: translateY(-5px);
        }}
        
        .member-photo {{
            width: 160px;
            height: 160px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
            box-shadow: 0 4px 15px rgba(34, 211, 238, 0.2);
        }}
        
        .protocol-diagram {{
            background: white;
            padding: 2rem;
            border-radius: 16px;
            margin: 2rem 0;
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
            <div style="color: var(--secondary); font-size: 1.2rem;">Depuis 2018</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Section Statistiques
        cols = st.columns(3)
        stats = [
            {"value": "82%", "label": "Prévalence nationale"},
            {"value": "150k+", "label": "Patients traités"},
            {"value": "92%", "label": "Taux de succès"}
        ]
        for col, stat in zip(cols, stats):
            with col:
                st.markdown(f"""
                <div class="data-card">
                    <div style="font-size: 2.5rem; font-weight: 700; color: var(--primary);">
                        {stat['value']}
                    </div>
                    <div style="color: #64748b; font-size: 0.9rem;">
                        {stat['label']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Section Causes
        st.markdown("<h2 class='section-title'>Étiologie et Facteurs de Risque</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="data-card">
                <h3 style="margin-top: 0;">Principaux déterminants</h3>
                <ul style="padding-left: 1.5rem;">
                    <li>Conditions socio-économiques</li>
                    <li>Accès à l'eau potable</li>
                    <li>Facteurs génétiques</li>
                </ul>
                <div style="color: var(--accent); margin-top: 1rem;">Étude SEN-HPylori 2023</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            try:
                st.image(TEAM_IMG_PATH, use_container_width=True)
            except Exception as e:
                st.error(f"Erreur de chargement de l'image : {str(e)}")
        
        # Timeline d'infection
        st.markdown("<h2 class='section-title'>Processus Infectieux</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card">
            <div style="padding: 2rem;">
                <div style="display: grid; gap: 1.5rem;">
                    <div style="border-left: 3px solid var(--accent); padding-left: 1.5rem;">
                        <h4>Contamination initiale</h4>
                        <p style="color: #666;">Transmission oro-fécale ou par eau contaminée</p>
                    </div>
                    <div style="border-left: 3px solid var(--accent); padding-left: 1.5rem;">
                        <h4>Colonisation gastrique</h4>
                        <p style="color: #666;">Adhésion à la muqueuse gastrique en 48h</p>
                    </div>
                    <div style="border-left: 3px solid var(--accent); padding-left: 1.5rem;">
                        <h4>Phase clinique</h4>
                        <p style="color: #666;">Apparition des symptômes après 2-3 semaines</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Arbre décisionnel diagnostique amélioré
        st.markdown("<h2 class='section-title'>Protocole Diagnostique</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="protocol-diagram">
            <img src="https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW0JhY2ludMOpIFx1MDBhMyA1MCBhbnNdIC0tPiBCKEFkbWluaXN0cmVyIGxlIHRlc3Qgc1x1MDBjO3JvbG9naXF1ZSlcbiAgICBCIC0tPiBDe1LDqXN1bHRhdCBwb3NpdGlmfVxuICAgIEMgLS0-fE91aXwgRChFbmRvc2NvcGllKVxuICAgIEMgLS0-fE5vbnwgRShTdWl2aSBcdTAwYTIgNiBtb2lzKVxuICAgIEEgLS0-fE5vbnwgRihBZG1pbmlzdHJlciB1biB0ZXN0IHJlc3BpcmF0b2lyZSkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ" 
                     alt="Arbre décisionnel" 
                     style="width:100%; border-radius:8px;">
        </div>
        """, unsafe_allow_html=True)

        # Équipe scientifique avec gestion des erreurs
        st.markdown("<h2 class='section-title'>Comité Scientifique</h2>", unsafe_allow_html=True)
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        for member in TEAM_MEMBERS:
            try:
                st.markdown(f"""
                <div class="team-card">
                    <img src="{member['photo']}" class="member-photo" alt="{member['name']}">
                    <h3 style="margin: 0.5rem 0; color: var(--primary);">{member['name']}</h3>
                    <p style="color: #666; margin: 0.5rem 0;">{member['role']}</p>
                    <p style="color: #999; font-size: 0.9rem;">{member['Etablissement']}</p>
                    <div style="margin: 1rem 0; font-size: 1.2rem;">
                        <a href="mailto:{member['email']}" style="color: var(--accent); margin: 0 0.5rem;">✉️</a>
                        <a href="{member['linkedin']}" style="color: var(--accent); margin: 0 0.5rem;">🔗</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur d'affichage du membre {member['name']} : {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
