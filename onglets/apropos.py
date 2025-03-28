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
            background: rgba(255, 255, 255, 0.98);
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
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }}
        
        .member-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            text-align: center;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
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
            box-shadow: 0 4px 15px rgba(34, 211, 238, 0.15);
        }}
        
        .decision-tree {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
            padding: 1.5rem;
            background: #f8faff;
            border-radius: 12px;
            margin: 1rem 0;
        }}
        
        .decision-node {{
            padding: 1rem;
            background: white;
            border-radius: 8px;
            border-left: 4px solid var(--primary);
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
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
                Programme de recherche clinique - Édition 2024
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
        
        # Section Étiologie
        st.markdown("<h2 class='section-title'>Étiologie et Facteurs de Risque</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="data-card">
                <h3 style="margin-top: 0;">Facteurs clés identifiés</h3>
                <ul style="padding-left: 1.5rem;">
                    <li>Conditions socio-économiques précaires</li>
                    <li>Accès limité à l'eau potable</li>
                    <li>Prédispositions génétiques</li>
                    <li>Hygiène alimentaire insuffisante</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            try:
                st.image(TEAM_IMG_PATH, use_container_width=True)
            except Exception as e:
                st.error(f"Erreur de chargement de l'image : {str(e)}")
        
        # Processus infectieux
        st.markdown("<h2 class='section-title'>Cycle Infectieux</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card">
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; text-align: center;">
                <div class="decision-node">
                    <h4>1. Contamination</h4>
                    <p>Transmission oro-fécale<br>ou hydrique</p>
                </div>
                <div style="text-align: center; padding: 1rem;">➔</div>
                <div class="decision-node">
                    <h4>2. Colonisation</h4>
                    <p>Fixation à la muqueuse gastrique<br>(48-72h)</p>
                </div>
                <div style="text-align: center; padding: 1rem;">➔</div>
                <div class="decision-node">
                    <h4>3. Manifestation</h4>
                    <p>Symptômes cliniques<br>(2-3 semaines)</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Protocoles cliniques
st.markdown("<h2 class='section-title'>Stratégies Cliniques</h2>", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["Symptômes", "Diagnostic", "Traitement", "Prévention"])

with tab1:
    st.markdown("""
    <div class="data-card">
        <h3>Principaux Symptômes</h3>
        <ul>
            <li>Douleurs épigastriques récurrentes</li>
            <li>Nausées post-prandiales</li>
            <li>Perte de poids inexpliquée</li>
            <li>Satiété précoce persistante</li>
        </ul>
        <div class="badge">Basé sur 1500 cas cliniques</div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="data-card">
        <h3>Arbre Décisionnel Diagnostique</h3>
        <div class="decision-tree">
            <div class="decision-node">
                <strong>Patient >50 ans ?</strong>
                <div style="margin-left: 1.5rem;">
                    <p>✅ Oui → Endoscopie + Biopsie</p>
                    <p>❌ Non → Test sérologique</p>
                </div>
            </div>
            <div style="text-align: center; margin: 0.5rem 0;">↓</div>
            <div class="decision-node">
                <strong>Résultat sérologique</strong>
                <div style="margin-left: 1.5rem;">
                    <p>➕ Positif → Test respiratoire</p>
                    <p>➖ Négatif → Suivi à 6 mois</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="data-card">
        <h3>Protocoles Thérapeutiques</h3>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
            <div class="decision-node">
                <h4>Première intention</h4>
                <p>Triple thérapie (14 jours)</p>
                <div class="badge">Efficacité 85%</div>
            </div>
            <div class="decision-node">
                <h4>Résistances</h4>
                <p>Quadrithérapie (10 jours)</p>
                <div class="badge">Efficacité 92%</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="data-card">
        <h3>Mesures Préventives</h3>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
            <div class="decision-node">
                <h4>🔬 Dépistage</h4>
                <p>Campagnes de dépistage familial</p>
            </div>
            <div class="decision-node">
                <h4>💧 Hygiène</h4>
                <p>Traitement des sources d'eau</p>
            </div>
            <div class="decision-node">
                <h4>📚 Éducation</h4>
                <p>Programmes de sensibilisation</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
        # Équipe scientifique
        st.markdown("<h2 class='section-title'>Comité Scientifique</h2>", unsafe_allow_html=True)
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        for member in TEAM_MEMBERS:
            try:
                st.markdown(f"""
                <div class="member-card">
                    <img src="{member['photo']}" class="member-photo" alt="{member['name']}">
                    <h3 style="margin: 0.5rem 0; color: var(--primary);">{member['name']}</h3>
                    <p style="color: #64748b; margin-bottom: 0.5rem;">{member['role']}</p>
                    <div style="margin-top: 1rem;">
                        <a href="mailto:{member['email']}" style="margin: 0 0.5rem; text-decoration: none;">📧</a>
                        <a href="{member['linkedin']}" style="margin: 0 0.5rem; text-decoration: none;">🌐</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur d'affichage pour {member['name']}: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
