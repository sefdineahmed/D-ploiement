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
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease;
        }}
        
        .team-card:hover {{
            transform: translateY(-5px);
        }}
        
        .team-photo {{
            width: 200px;
            height: 200px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
            box-shadow: 0 4px 15px rgba(34, 211, 238, 0.2);
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
            <div style="color: #64748b; font-size: 1.2rem;">
                Programme de recherche clinique depuis 2018
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
                <div style="text-align: center; padding: 2rem; background: #f8fafc; border-radius: 16px;">
                    <div style="font-size: 2.5rem; font-weight: 700; color: var(--primary);">
                        {stat['value']}
                    </div>
                    <div style="color: #64748b; font-size: 1rem;">
                        {stat['label']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Section Processus clinique
        st.markdown("<h2 class='section-title'>Arbre Décisionnel Diagnostique</h2>", unsafe_allow_html=True)
        
        # Diagramme décisionnel interactif
        decision_tree = """
        graph TD
            A[Patient >50 ans] -->|Oui| B[Endoscopie obligatoire]
            A -->|Non| C{Test sérologique positif}
            C -->|Oui| D[Test respiratoire]
            C -->|Non| E[Suivi à 6 mois]
        """
        
        st.graphviz_chart(decision_tree)
        
        # Équipe scientifique
        st.markdown("<h2 class='section-title' style='text-align: center; margin-top: 4rem;'>Comité Scientifique</h2>", unsafe_allow_html=True)
        
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        for member in TEAM_MEMBERS:
            st.markdown(f"""
            <div class="team-card">
                <img src="{member['photo']}" class="team-photo" alt="{member['name']}">
                <h3 style="margin: 0.5rem 0; color: var(--primary);">{member['name']}</h3>
                <p style="margin: 0; color: #6b7280; font-weight: 500;">{member['role']}</p>
                <p style="margin: 0.5rem 0; color: #6b7280; font-size: 0.9rem;">{member['Etablissement']}</p>
                <div style="margin-top: 1rem;">
                    <a href="mailto:{member['email']}" style="margin: 0 0.5rem; text-decoration: none;">📧</a>
                    <a href="{member['linkedin']}" style="margin: 0 0.5rem; text-decoration: none;">🔗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
