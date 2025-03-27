import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2563eb;
            --secondary: #4f46e5;
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
        
        .section-title:after {{
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
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.3);
            transition: transform 0.3s ease;
        }}
        
        .data-card:hover {{
            transform: translateY(-5px);
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
        }}
        
        .timeline-item:before {{
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
        
        .team-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            text-align: center;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        
        .team-card img {{
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
        }}
        
        .badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            background: rgba(34, 211, 238, 0.1);
            color: var(--accent);
            font-size: 0.85rem;
            margin: 0.5rem 0;
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
        }}
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        # Section En-tête
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0;">
            <h1 style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                Initiative Nationale de Lutte Contre H. pylori
            </h1>
            <div class="badge">Depuis 2018</div>
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
                <div class="badge">Étude SEN-HPylori 2023</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image(TEAM_IMG_PATH, use_container_width=True)
        
        # Timeline d'infection
        st.markdown("<h2 class='section-title'>Processus Infectieux</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card">
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
        
        # Onglets cliniques
        st.markdown("<h2 class='section-title'>Protocoles Cliniques</h2>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["🚨 Symptomatologie", "🔍 Diagnostic", "💊 Thérapeutique", "🛡️ Prévention"])
        
        with tab1:
            st.markdown("""
            <div class="data-card">
                <h3 style="margin-top: 0;">Tableau clinique typique</h3>
                <ul>
                    <li>Dyspepsie persistante (>3 mois)</li>
                    <li>Anémie ferriprive inexpliquée</li>
                    <li>Perte de poids progressive</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("""
            <div class="data-card">
                <h3>Arbre décisionnel diagnostique</h3>
                <pre style="background: #f8fafc; padding: 1rem; border-radius: 8px;">
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
            <div class="data-card">
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
                    <div>
                        <h4>Première ligne</h4>
                        <p>Triple thérapie (14 jours)</p>
                        <div class="badge">Efficacité 85%</div>
                    </div>
                    <div>
                        <h4>Résistance</h4>
                        <p>Quadrithérapie (10 jours)</p>
                        <div class="badge">Efficacité 92%</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with tab4:
            st.markdown("""
            <div class="data-card">
                <h3>Stratégies préventives</h3>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                    <div class="badge">Éducation sanitaire</div>
                    <div class="badge">Dépistage familial</div>
                    <div class="badge">Traitement de l'eau</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Équipe scientifique
        st.markdown("<h2 class='section-title' style='text-align: center;'>Comité Scientifique</h2>", unsafe_allow_html=True)
        cols = st.columns(3)
        for member, col in zip(TEAM_MEMBERS, cols):
            with col:
                st.markdown(f"""
                <div class="team-card">
                    <img src="{member['photo']}" alt="{member['name']}">
                    <h3 style="margin: 0.5rem 0;">{member['name']}</h3>
                    <p style="color: var(--primary); font-weight: 500;">{member['role']}</p>
                    <div style="margin: 1rem 0;">
                        <a href="mailto:{member['email']}" style="margin: 0 0.5rem;">✉️</a>
                        <a href="{member['linkedin']}" style="margin: 0 0.5rem;">🔗</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
