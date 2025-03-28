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
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .team-card:hover {{
            transform: translateY(-5px);
        }}
        
        .team-photo {{
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
            box-shadow: 0 4px 15px rgba(34, 211, 238, 0.2);
        }}
        
        .decision-tree {{
            padding: 2rem;
            background: #f8fafc;
            border-radius: 12px;
            margin: 2rem 0;
        }}
        
        .decision-step {{
            display: flex;
            align-items: center;
            margin: 1rem 0;
            padding: 1rem;
            background: white;
            border-radius: 8px;
        }}
        
        .step-icon {{
            font-size: 1.5rem;
            margin-right: 1rem;
            color: var(--primary);
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
            <div style="color: #64748b; font-size: 1.1rem;">
                Programme de recherche clinique - Université Alioune Diop de Bambey
            </div>
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
                <div style="color: #64748b; font-size: 0.9rem; margin-top: 1rem;">
                    Source : Étude SEN-HPylori 2023
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image(TEAM_IMG_PATH, use_container_width=True)
        
        # Arbre décisionnel amélioré
        st.markdown("<h2 class='section-title'>Protocole Diagnostique</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="decision-tree">
            <div class="decision-step">
                <div class="step-icon">1️⃣</div>
                <div>
                    <h4>Patient de plus de 50 ans</h4>
                    <p>Endoscopie digestive haute obligatoire avec biopsies</p>
                </div>
            </div>
            
            <div class="decision-step">
                <div class="step-icon">2️⃣</div>
                <div>
                    <h4>Test sérologique positif</h4>
                    <p>Test respiratoire à l'urée marquée pour confirmation</p>
                </div>
            </div>
            
            <div class="decision-step">
                <div class="step-icon">3️⃣</div>
                <div>
                    <h4>Cas asymptomatique</h4>
                    <p>Suivi clinique et contrôle à 6 mois</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Équipe scientifique
        st.markdown("<h2 class='section-title'>Équipe de Recherche</h2>", unsafe_allow_html=True)
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        for member in TEAM_MEMBERS:
            st.markdown(f"""
            <div class="team-card">
                <img src="{member['photo']}" class="team-photo" alt="{member['name']}">
                <h3 style="margin: 0.5rem 0; color: var(--primary);">{member['name']}</h3>
                <p style="color: #64748b; margin: 0.3rem 0;">{member['role']}</p>
                <p style="color: #94a3b8; font-size: 0.9rem;">{member['Etablissement']}</p>
                <div style="margin: 1rem 0; font-size: 1.2rem;">
                    <a href="mailto:{member['email']}" style="color: var(--primary); margin: 0 0.5rem; text-decoration: none;">✉️</a>
                    <a href="{member['linkedin']}" style="color: var(--primary); margin: 0 0.5rem; text-decoration: none;">🌐</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
