import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        /* ... (le reste du CSS reste inchangé) ... */
        
        .team-card img {{
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid var(--accent);
            display: block; /* Ajout pour forcer l'affichage */
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

            
                # Section Équipe Scientifique corrigée
                st.markdown("<h2 class='section-title' style='text-align: center;'>Comité Scientifique</h2>", unsafe_allow_html=True)
                
                cols = st.columns(len(TEAM_MEMBERS))
                for member, col in zip(TEAM_MEMBERS, cols):
                    with col:
                        try:
                            # Chemin corrigé depuis la racine du projet
                            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
                            photo_path = os.path.join(base_dir, member['photo'])
                            
                            if not os.path.exists(photo_path):
                                raise FileNotFoundError(f"Fichier introuvable: {photo_path}")
                            
                            st.markdown(f"""
                            <div class="team-card">
                                <img src="{photo_path}" alt="{member['name']}">
                                <h3 style="margin: 0.5rem 0;">{member['name']}</h3>
                                <p style="color: #4b5563; font-size: 0.9em;">{member['role']}</p>
                                <p style="color: var(--primary); font-weight: 500;">{member['Etablissement']}</p>
                                <div style="margin: 1rem 0;">
                                    <a href="mailto:{member['email']}" target="_blank" style="margin: 0 0.5rem; color: var(--primary);">✉️</a>
                                    <a href="{member['linkedin']}" target="_blank" style="margin: 0 0.5rem; color: var(--primary);">🔗</a>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Erreur de chargement du profil: {str(e)}")
                            st.markdown(f"""
                            <div class="team-card">
                                <div style="text-align: center; padding: 1rem;">
                                    <div style="width: 120px; height: 120px; background: #f0f0f0; border-radius: 50%; margin: 0 auto 1rem;"></div>
                                    <h3>{member['name']}</h3>
                                    <p>{member['role']}</p>
                                    <p>{member['Etablissement']}</p>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
            
                st.markdown("</div>", unsafe_allow_html=True)
            
            if __name__ == "__main__":
                a_propos()
