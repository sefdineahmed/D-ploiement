import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown("""
    <style>
        .section-title {
            color: #2e77d0;
            border-bottom: 3px solid #2e77d0;
            padding-bottom: 0.3em;
            margin: 2rem 0 !important;
        }
        .team-card {
            padding: 1.5em;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        .team-card:hover {
            transform: translateY(-5px);
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='section-title'>📚 Causes de l'infection</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        L'infection par la bactérie *H. pylori* est un facteur majeur dans le développement des maladies gastriques. 
        
        **Principaux facteurs de risque au Sénégal :**
        - Conditions socio-économiques difficiles
        - Accès limité à l'eau potable
        - Densité familiale élevée
        """)
    with col2:
        st.image(TEAM_IMG_PATH, use_container_width=True)

    st.markdown("---")
    st.markdown("<h1 class='section-title'>🦠 Modes de transmission</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 1.5em; border-radius: 10px;">
        <h4 style="color: #dc3545;">Voies principales de contamination :</h4>
        <ul>
            <li>Contact oral-oral (partage d'ustensiles)</li>
            <li>Consommation d'eau contaminée</li>
            <li>Hygiène alimentaire insuffisante</li>
        </ul>
        <div style="color: #6c757d; font-size: 0.9em;">
        🔍 Prévalence estimée à 80% chez les adultes sénégalais
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["⚠️ Symptômes", "🔬 Diagnostic", "💊 Traitements", "🛡️ Prévention"])
    with tab1:
        st.markdown("""
        **Signes cliniques caractéristiques :**
        - Douleurs épigastriques récurrentes
        - Satiété précoce persistante
        - Perte de poids inexpliquée (>10% du poids corporel)
        """)
    with tab2:
        st.markdown("""
        **Protocole diagnostique recommandé :**
        1. Test respiratoire à l'urée marquée
        2. Recherche d'antigènes fécaux
        3. Endoscopie avec biopsie (cas complexes)
        """)
    with tab3:
        st.markdown("""
        **Schéma thérapeutique de 1ère intention :**
        ```python
        pylera_treatment = {
            "Durée": "10 jours",
            "Composition": [
                "Bismuth subcitrate",
                "Tétracycline",
                "Métronidazole",
                "Oméprazole"
            ],
            "Efficacité": "92% de succès (étude Dakar 2023)"
        }
        ```
        """)
    with tab4:
        st.markdown("""
        **Stratégies préventives validées :**
        - Dépistage familial systématique
        - Campagnes de sensibilisation communautaires
        - Amélioration des infrastructures sanitaires
        """)

    st.markdown("<h1 class='section-title' style='text-align: center;'>👥 Équipe Scientifique</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    for member, col in zip(TEAM_MEMBERS, cols):
        with col:
            st.markdown("<div class='team-card'>", unsafe_allow_html=True)
            st.image(member["photo"], use_container_width=True)
            st.markdown(f"""
            <div style="text-align: center; margin: 1em 0;">
                <h3 style="margin: 0; color: #2e77d0;">{member['name']}</h3>
                <p style="color: #6c757d; font-size: 0.9em;">{member['role']}</p>
                <div style="margin-top: 1em;">
                    <a href="{member['email']}" target="_blank" style="margin: 0 0.5em;">📧</a>
                    <a href="{member['linkedin']}" target="_blank" style="margin: 0 0.5em;">🔗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
