import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown("""
    <style>
        /* Style général de la section */
        .section-title {
            color: #2e77d0;
            border-bottom: 4px solid #2e77d0;
            padding-bottom: 0.4em;
            margin: 2rem 0 !important;
            font-family: 'Poppins', sans-serif;
        }
        
        /* Style du conteneur des textes de présentation */
        .presentation {
            background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(245,245,245,0.9));
            padding: 1.5em;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
        }
        
        /* Style du conteneur d'image */
        .presentation img {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Style des blocs de l'équipe */
        .team-card {
            background: linear-gradient(135deg, #ffffff, #f1f7ff);
            padding: 1.5em;
            border-radius: 15px;
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            margin-bottom: 1.5rem;
        }
        .team-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
        }
        
        /* Style des liens de contact */
        .team-card a {
            text-decoration: none;
            font-size: 1.2rem;
            margin: 0 0.5em;
            color: #2e77d0;
            transition: color 0.3s;
        }
        .team-card a:hover {
            color: #1b5b9e;
        }
    </style>
    """, unsafe_allow_html=True)

    # Section Causes
    st.markdown("<h1 class='section-title'>📚 Causes de l'infection</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="presentation">
            L'infection par la bactérie <em>H. pylori</em> joue un rôle crucial dans le développement de maladies gastriques. 
            <br><br>
            <strong>Principaux facteurs de risque au Sénégal :</strong>
            <ul>
                <li>Conditions socio-économiques difficiles</li>
                <li>Accès limité à l'eau potable</li>
                <li>Densité familiale élevée</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image(TEAM_IMG_PATH, use_container_width=True)
        
    st.markdown("---")
    
    # Section Transmission
    st.markdown("<h1 class='section-title'>🦠 Modes de transmission</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="presentation" style="background: linear-gradient(135deg, #f8f9fa, #e9ecef);">
        <h4 style="color: #dc3545;">Voies principales de contamination :</h4>
        <ul>
            <li>Contact oral-oral (partage d'ustensiles)</li>
            <li>Consommation d'eau contaminée</li>
            <li>Hygiène alimentaire insuffisante</li>
        </ul>
        <p style="color: #6c757d; font-size: 0.9em;">🔍 Prévalence estimée à 80% chez les adultes sénégalais</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Onglets pour les détails supplémentaires
    tab1, tab2, tab3, tab4 = st.tabs(["⚠️ Symptômes", "🔬 Diagnostic", "💊 Traitements", "🛡️ Prévention"])
    with tab1:
        st.markdown("""
        <div class="presentation">
            <strong>Signes cliniques caractéristiques :</strong>
            <ul>
                <li>Douleurs épigastriques récurrentes</li>
                <li>Satiété précoce persistante</li>
                <li>Perte de poids inexpliquée (>10% du poids corporel)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with tab2:
        st.markdown("""
        <div class="presentation">
            <strong>Protocole diagnostique recommandé :</strong>
            <ol>
                <li>Test respiratoire à l'urée marquée</li>
                <li>Recherche d'antigènes fécaux</li>
                <li>Endoscopie avec biopsie (cas complexes)</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    with tab3:
        st.markdown("""
        <div class="presentation">
            <strong>Schéma thérapeutique de 1ère intention :</strong>
            <pre style="background: #f4f4f4; padding: 1em; border-radius: 8px;">
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
            </pre>
        </div>
        """, unsafe_allow_html=True)
    with tab4:
        st.markdown("""
        <div class="presentation">
            <strong>Stratégies préventives validées :</strong>
            <ul>
                <li>Dépistage familial systématique</li>
                <li>Campagnes de sensibilisation communautaires</li>
                <li>Amélioration des infrastructures sanitaires</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='section-title' style='text-align: center;'>👥 Équipe Scientifique</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    for member, col in zip(TEAM_MEMBERS, cols):
        with col:
            st.markdown("<div class='team-card'>", unsafe_allow_html=True)
            st.image(member["photo"], use_container_width=True)
            st.markdown(f"""
            <div style="text-align: center; margin-top: 1em;">
                <h3 style="margin: 0; color: #2e77d0;">{member['name']}</h3>
                <p style="color: #6c757d; font-size: 0.9em;">{member['role']}</p>
                <div style="margin-top: 0.5em;">
                    <a href="mailto:{member['email']}" target="_blank">📧</a>
                    <a href="{member['linkedin']}" target="_blank">🔗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
