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
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        
        .team-card img {{
            width: 160px;
            height: 160px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
            box-shadow: 0 4px 15px rgba(34, 211, 238, 0.2);
        }}
        
        .decision-tree {{
            background: #f8fafc;
            border-radius: 12px;
            padding: 2rem;
            margin: 1rem 0;
            font-family: 'Courier New', monospace;
        }}
        
        .badge {{
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            background: rgba(34, 211, 238, 0.1);
            color: var(--accent);
            font-weight: 500;
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
            st.image(TEAM_IMG_PATH, use_container_width=True, caption="Répartition géographique des cas")
        
        # Timeline d'infection
        st.markdown("<h2 class='section-title'>Processus Infectieux</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card">
            <div style="padding: 2rem;">
                <div style="display: grid; gap: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <div style="width: 40px; height: 40px; background: var(--accent); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center;">1</div>
                        <div>
                            <h4>Contamination initiale</h4>
                            <p style="color: #64748b;">Transmission oro-fécale ou par eau contaminée</p>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <div style="width: 40px; height: 40px; background: var(--accent); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center;">2</div>
                        <div>
                            <h4>Colonisation gastrique</h4>
                            <p style="color: #64748b;">Adhésion à la muqueuse gastrique en 48h</p>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <div style="width: 40px; height: 40px; background: var(--accent); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center;">3</div>
                        <div>
                            <h4>Phase clinique</h4>
                            <p style="color: #64748b;">Apparition des symptômes après 2-3 semaines</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Onglets cliniques
        st.markdown("<h2 class='section-title'>Protocoles Cliniques</h2>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["🚨 Symptomatologie", "🔍 Diagnostic", "💊 Thérapeutique", "🛡️ Prévention"])
        
        with tab2:
            st.markdown("""
            <div class="data-card">
                <h3>Arbre décisionnel diagnostique</h3>
                <div class="decision-tree">
                    <div style="margin-bottom: 1rem;">📌 Démarche diagnostique :</div>
                    <div style="padding-left: 1.5rem;">
                        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                            <span style="color: var(--primary); margin-right: 0.5rem;">►</span>
                            Si âge > 50 ans → Endoscopie obligatoire
                        </div>
                        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                            <span style="color: var(--primary); margin-right: 0.5rem;">►</span>
                            Si sérologie positive → Test respiratoire à l'urée marquée
                        </div>
                        <div style="display: flex; align-items: center;">
                            <span style="color: var(--primary); margin-right: 0.5rem;">►</span>
                            Autres cas → Suivi à 6 mois avec test antigène fécal
                        </div>
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
                <img src="{member['photo']}" alt="{member['name']}">
                <h3 style="margin: 0.5rem 0; color: var(--primary);">{member['name']}</h3>
                <p style="color: #64748b; margin-bottom: 1rem;">{member['role']}</p>
                <div style="display: flex; gap: 1rem; justify-content: center;">
                    <a href="mailto:{member['email']}" style="color: var(--primary); text-decoration: none;">📧 Email</a>
                    <a href="{member['linkedin']}" style="color: var(--primary); text-decoration: none;">🔗 LinkedIn</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
