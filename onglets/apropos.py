import streamlit as st
import os
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
            font-family: 'Roboto', sans-serif;
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
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            border-radius: 2px;
        }}
        
        .data-card {{
            background: white;
            border-radius: 16px;
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
        
        .timeline {{
            position: relative;
            padding: 2rem 0;
        }}
        
        .timeline-item {{
            padding: 1.5rem;
            margin-left: 30px;
            border-left: 3px solid var(--accent);
            position: relative;
            background: rgba(34, 211, 238, 0.05);
            border-radius: 8px;
            margin-bottom: 1rem;
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
            box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1);
        }}
        
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }}
        
        .member-card {{
            background: white;
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(46, 119, 208, 0.1);
        }}
        
        .member-photo {{
            width: 160px;
            height: 160px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
            box-shadow: 0 4px 12px rgba(34, 211, 238, 0.2);
        }}
        
        .badge {{
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 24px;
            background: rgba(34, 211, 238, 0.1);
            color: var(--accent);
            font-size: 0.9rem;
            font-weight: 500;
            margin: 0.5rem 0;
        }}
        
        .stTabs [role="tablist"] {{
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        
        .stTabs [role="tab"] {{
            padding: 1rem 2rem !important;
            border-radius: 12px !important;
            transition: all 0.3s ease !important;
            background: rgba(46, 119, 208, 0.1) !important;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: var(--primary) !important;
            color: white !important;
            box-shadow: 0 4px 12px rgba(46, 119, 208, 0.2);
        }}
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        # Section En-tête
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0;">
            <h1 style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                🦠 Initiative Nationale Contre H. pylori
            </h1>
            <div class="badge">Depuis 2018 • Programme certifié OMS</div>
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
        st.markdown("<h2 class='section-title'>Facteurs de Risque</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="data-card">
                <h3 style="margin-top: 0;">Principaux déterminants épidémiologiques</h3>
                <ul style="padding-left: 1.5rem; line-height: 2;">
                    <li>🏚 Conditions socio-économiques précaires</li>
                    <li>🚰 Accès limité à l'eau potable</li>
                    <li>🧬 Prédispositions génétiques</li>
                </ul>
                <div class="badge">Étude SEN-HPylori 2023</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if os.path.exists(TEAM_IMG_PATH):
                st.image(TEAM_IMG_PATH, use_container_width=True)
            else:
                st.error("Image non trouvée")
        
        # Processus infectieux
        st.markdown("<h2 class='section-title'>Cycle Infectieux</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card">
            <div class="timeline">
                <div class="timeline-item">
                    <h4>🦠 Contamination initiale</h4>
                    <p>Transmission oro-fécale ou par eau contaminée</p>
                </div>
                <div class="timeline-item">
                    <h4>🔬 Colonisation gastrique</h4>
                    <p>Adhésion à la muqueuse gastrique en 48h</p>
                </div>
                <div class="timeline-item">
                    <h4>🩺 Manifestation clinique</h4>
                    <p>Apparition des symptômes après 2-3 semaines</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Protocoles cliniques
        st.markdown("<h2 class='section-title'>Stratégies Médicales</h2>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["🚨 Symptômes", "🔍 Diagnostic", "💊 Traitements", "🛡️ Prévention"])
        
        with tab1:
            st.markdown("""
            <div class="data-card">
                <h3 style="margin-top: 0;">Tableau clinique caractéristique</h3>
                <ul style="line-height: 2;">
                    <li>🤢 Dyspepsie persistante (>3 mois)</li>
                    <li>🩸 Anémie ferriprive inexpliquée</li>
                    <li>📉 Perte de poids progressive (>10% masse corporelle)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("""
            <div class="data-card">
                <h3>Arbre décisionnel diagnostique</h3>
                <div style="background: #f8fafc; padding: 1rem; border-radius: 8px;">
                    <pre style="margin: 0; font-family: 'Roboto Mono', monospace;">
def protocol_diagnostic():
    if patient.age > 50:
        return "Endoscopie obligatoire"
    elif test_serologique.positivity:
        return "Test respiratoire"
    else:
        return "Suivi à 6 mois"
                    </pre>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("""
            <div class="data-card">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;">
                    <div style="padding: 1rem; background: rgba(46, 119, 208, 0.05); border-radius: 8px;">
                        <h4>Première intention</h4>
                        <p>Triple thérapie (14 jours)</p>
                        <div class="badge">Efficacité 85%</div>
                    </div>
                    <div style="padding: 1rem; background: rgba(46, 119, 208, 0.05); border-radius: 8px;">
                        <h4>Cas résistants</h4>
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
                    <div class="badge">📚 Éducation sanitaire</div>
                    <div class="badge">👨👩👧👦 Dépistage familial</div>
                    <div class="badge">💧 Traitement de l'eau</div>
                    <div class="badge">🏥 Campagnes de vaccination</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

                    

            
                # Équipe scientifique dans 3 colonnes
                    st.markdown("<h2 class='section-title' style='text-align: center;'>Équipe Scientifique</h2>", unsafe_allow_html=True)
                    
                    cols = st.columns(3)
                    for idx, member in enumerate(TEAM_MEMBERS):
                        with cols[idx % 3]:
                            if os.path.exists(member['photo']):
                                st.markdown(f"""
                                <div class="member-card">
                                    <img src="{member['photo']}" class="member-photo" alt="Photo de {member['name']}">
                                    <h3 style="margin: 0.5rem 0; color: var(--primary);">{member['name']}</h3>
                                    <p style="color: #64748b; margin: 0.5rem 0; font-weight: 500;">{member['role']}</p>
                                    <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 1rem;">{member['Etablissement']}</p>
                                    <div style="margin: 1rem 0;">
                                        <a href="mailto:{member['email']}" 
                                           style="margin: 0 0.5rem; 
                                                  color: white; 
                                                  background: var(--primary); 
                                                  padding: 0.5rem 1rem; 
                                                  border-radius: 8px; 
                                                  text-decoration: none;">
                                           ✉️ Contact
                                        </a>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                            else:
                                st.error(f"Photo non trouvée : {member['photo']}")
            
                    st.markdown("</div>", unsafe_allow_html=True)
            
            if __name__ == "__main__":
                a_propos()
