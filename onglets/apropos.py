import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
            --background: #f8fafc;
        }}
        
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            background: var(--background);
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
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
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
        
        .member-card {{
            background: white;
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }}
        
        .member-card:hover {{
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }}
        
        .member-photo {{
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
            box-shadow: 0 4px 15px rgba(34, 211, 238, 0.2);
        }}
        
        .badge {{
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            background: rgba(34, 211, 238, 0.1);
            color: var(--accent);
            font-weight: 500;
            margin: 1rem 0;
        }}
        
        .timeline {{
            position: relative;
            padding: 2rem 0;
            margin-left: 20px;
        }}
        
        .timeline-item {{
            padding: 1.5rem;
            margin-bottom: 2rem;
            border-left: 3px solid var(--accent);
            position: relative;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
        }}
        
        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -10px;
            top: 20px;
            width: 16px;
            height: 16px;
            background: var(--secondary);
            border-radius: 50%;
            box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.2);
        }}
        
        .stTabs [role="tablist"] {{
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        
        .stTabs [role="tab"] {{
            padding: 1rem 2rem !important;
            border-radius: 10px !important;
            transition: all 0.3s ease !important;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: var(--primary) !important;
            color: white !important;
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
        st.markdown("<h2 class='section-title'>📊 Impact National</h2>", unsafe_allow_html=True)
        stats = [
            {"value": "82%", "label": "Prévalence nationale"},
            {"value": "150k+", "label": "Patients traités"},
            {"value": "92%", "label": "Taux de succès"}
        ]
        st.markdown("<div class='stats-grid'>", unsafe_allow_html=True)
        for stat in stats:
            st.markdown(f"""
            <div class="stat-card">
                <div style="font-size: 2.5rem; font-weight: 700; color: var(--primary);">
                    {stat['value']}
                </div>
                <div style="color: #64748b; font-size: 1rem; margin-top: 0.5rem;">
                    {stat['label']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Causes et image
        st.markdown("<h2 class='section-title'>🔍 Étiologie et Facteurs de Risque</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="stat-card">
                <h3 style="margin-top: 0; color: var(--primary);">Principaux déterminants</h3>
                <ul style="padding-left: 1.5rem; text-align: left;">
                    <li>Conditions socio-économiques</li>
                    <li>Accès à l'eau potable</li>
                    <li>Facteurs génétiques</li>
                </ul>
                <div class="badge">Étude SEN-HPylori 2023</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            try:
                st.image(TEAM_IMG_PATH, use_container_width=True)
            except Exception as e:
                st.error(f"Erreur de chargement de l'image : {str(e)}")
        
        # Processus infectieux
        st.markdown("<h2 class='section-title'>🦠 Cycle Infectieux</h2>", unsafe_allow_html=True)
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
        
        # Protocoles cliniques
        st.markdown("<h2 class='section-title'>🏥 Protocoles Cliniques</h2>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["🚨 Symptômes", "🔍 Diagnostic", "💊 Traitements", "🛡️ Prévention"])
        
        with tab1:
            st.markdown("""
            <div class="stat-card">
                <h3 style="color: var(--primary);">Tableau clinique typique</h3>
                <ul style="text-align: left;">
                    <li>Dyspepsie persistante (>3 mois)</li>
                    <li>Anémie ferriprive inexpliquée</li>
                    <li>Perte de poids progressive</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("""
            <div class="stat-card">
                <h3 style="color: var(--primary);">Arbre décisionnel diagnostique</h3>
                <pre style="background: #f8fafc; padding: 1rem; border-radius: 8px; overflow-x: auto;">
def protocol_diagnostic():
    if patient.age > 50:
        return "Endoscopie obligatoire"
    elif test_serologique.positivity:
        return "Test respiratoire"
    else:
        return "Suivi à 6 mois"
                </pre>
            </div>
            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("""
            <div class="stat-card">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                    <div>
                        <h4 style="color: var(--secondary);">Première ligne</h4>
                        <p>Triple thérapie (14 jours)</p>
                        <div class="badge">Efficacité 85%</div>
                    </div>
                    <div>
                        <h4 style="color: var(--secondary);">Résistance</h4>
                        <p>Quadrithérapie (10 jours)</p>
                        <div class="badge">Efficacité 92%</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with tab4:
            st.markdown("""
            <div class="stat-card">
                <h3 style="color: var(--primary);">Stratégies préventives</h3>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                    <div class="badge">Éducation sanitaire</div>
                    <div class="badge">Dépistage familial</div>
                    <div class="badge">Traitement de l'eau</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Équipe scientifique
        st.markdown("<h2 class='section-title' style='text-align: center;'>👨🔬 Comité Scientifique</h2>", unsafe_allow_html=True)
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        for member in TEAM_MEMBERS:
            try:
                st.markdown(f"""
                <div class="member-card">
                    <img src="{member['photo']}" class="member-photo" alt="{member['name']}">
                    <h3 style="margin: 0.5rem 0; color: var(--primary);">{member['name']}</h3>
                    <p style="color: var(--secondary); margin: 0;">{member['role']}</p>
                    <p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0;">{member['Etablissement']}</p>
                    <div style="margin: 1rem 0;">
                        <a href="mailto:{member['email']}" style="margin: 0 0.5rem; color: var(--primary);">✉️ Email</a>
                        <a href="{member['linkedin']}" style="margin: 0 0.5rem; color: var(--primary);">🔗 LinkedIn</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur d'affichage du membre {member['name']} : {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
