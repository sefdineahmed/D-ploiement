import streamlit as st
from utils import TEAM_MEMBERS, TEAM_IMG_PATH

def a_propos():
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }}
        
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .hero-section {{
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 20px;
            color: white;
            margin-bottom: 3rem;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }}
        
        .stat-card {{
            background: rgba(255, 255, 255, 0.95);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            text-align: center;
        }}
        
        .team-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }}
        
        .member-card {{
            position: relative;
            overflow: hidden;
            border-radius: 15px;
            padding: 1.5rem;
            background: white;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s;
        }}
        
        .member-card:hover {{
            transform: translateY(-5px);
        }}
        
        .member-photo {{
            width: 160px;
            height: 160px;
            border-radius: 50%;
            margin: 0 auto 1rem;
            object-fit: cover;
            border: 3px solid var(--accent);
        }}
        
        .badge {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: var(--accent);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8em;
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
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        # Section Héro
        st.markdown(f"""
            <div class='hero-section'>
                <h1 style="font-size: 2.8rem; margin-bottom: 1rem;">Initiative Nationale Contre H. pylori</h1>
                <div class="badge">Depuis 2018</div>
                <img src="{TEAM_IMG_PATH}" style="width: 100%; border-radius: 15px; margin-top: 2rem;">
            </div>
        """, unsafe_allow_html=True)
        
        # Statistiques
        st.markdown("""
            <div class='stats-grid'>
                <div class='stat-card'>
                    <div style="font-size: 2.2rem; color: var(--primary); font-weight: 700;">82%</div>
                    <div style="color: #64748b;">Prévalence nationale</div>
                </div>
                <div class='stat-card'>
                    <div style="font-size: 2.2rem; color: var(--primary); font-weight: 700;">150k+</div>
                    <div style="color: #64748b;">Patients traités</div>
                </div>
                <div class='stat-card'>
                    <div style="font-size: 2.2rem; color: var(--primary); font-weight: 700;">92%</div>
                    <div style="color: #64748b;">Taux de succès</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Section Équipe
        st.markdown("<h2 style='text-align: center; color: var(--primary); margin: 3rem 0;'>Notre Équipe Scientifique</h2>", unsafe_allow_html=True)
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        for member in TEAM_MEMBERS:
            st.markdown(f"""
                <div class='member-card'>
                    <div class='badge'>Expert</div>
                    <img class='member-photo' src='{member["photo"]}' alt='{member["name"]}'>
                    <h3 style='margin: 0.5rem 0; color: var(--primary);'>{member['name']}</h3>
                    <p style='color: #6c757d; margin: 0;'>{member['role']}</p>
                    <div style='margin: 1rem 0;'>
                        <a href='mailto:{member['email']}' style='margin: 0 0.5rem; color: var(--primary);'>📧</a>
                        <a href='{member['linkedin']}' style='margin: 0 0.5rem; color: var(--primary);'>🌐</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section Protocoles
        st.markdown("<h2 style='color: var(--primary); margin: 3rem 0; text-align: center;'>Protocoles Cliniques</h2>", unsafe_allow_html=True)
        tab1, tab2, tab3 = st.tabs(["📋 Diagnostic", "💊 Traitements", "🛡️ Prévention"])
        
        with tab1:
            st.markdown("""
                <div style='background: white; padding: 2rem; border-radius: 15px;'>
                    <h3 style='color: var(--secondary);'>Arbre décisionnel</h3>
                    <pre style='background: #f8fafc; padding: 1rem; border-radius: 8px;'>
if patient.age > 50:
    → Endoscopie + Biopsie
elif test_serologie_positive:
    → Test respiratoire à l'urée
else:
    → Suivi à 3 mois
                    </pre>
                </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("""
                <div style='display: grid; gap: 1rem;'>
                    <div style='background: #f0faff; padding: 1.5rem; border-radius: 12px;'>
                        <h4 style='color: var(--primary);'>Première ligne</h4>
                        <p>Triple thérapie (14 jours)</p>
                        <div class='badge'>Efficacité 85%</div>
                    </div>
                    <div style='background: #f0faff; padding: 1.5rem; border-radius: 12px;'>
                        <h4 style='color: var(--primary);'>Cas résistants</h4>
                        <p>Quadrithérapie (10 jours)</p>
                        <div class='badge'>Efficacité 92%</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown("""
                <div style='display: flex; gap: 1rem; flex-wrap: wrap;'>
                    <div style='background: var(--accent); color: white; padding: 0.5rem 1rem; border-radius: 20px;'>
                        Éducation sanitaire
                    </div>
                    <div style='background: var(--accent); color: white; padding: 0.5rem 1rem; border-radius: 20px;'>
                        Dépistage familial
                    </div>
                    <div style='background: var(--accent); color: white; padding: 0.5rem 1rem; border-radius: 20px;'>
                        Traitement de l'eau
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    a_propos()
