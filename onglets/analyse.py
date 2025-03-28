import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
from utils import load_data
import matplotlib.pyplot as plt

def analyse_descriptive():
    st.title("🔍 Analyse Médico-Statistique")
    df = load_data()
    if df.empty:
        return st.error("❌ Erreur de chargement des données")

    # Style CSS personnalisé
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .metric-card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            margin: 1rem;
            transition: transform 0.3s;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
        }
        
        .section-title {
            color: var(--primary);
            border-left: 4px solid var(--accent);
            padding-left: 1rem;
            margin: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # Section 1: Aperçu des données
    with st.expander("📂 Exploration des Données Brutes", expanded=True):
        cols = st.columns([2, 1])
        with cols[0]:
            st.dataframe(df.head(10).style.highlight_max(color='#f0faff')
        with cols[1]:
            st.markdown("""
            <div class="metric-card">
                <h3>📦 Dimensions des Données</h3>
                <p style="font-size: 2rem; color: var(--primary);">{0} Patients</p>
                <p>{1} Variables Cliniques</p>
            </div>
            """.format(df.shape[0], df.shape[1]), unsafe_allow_html=True)

    st.markdown("---")

    # Section 2: Statistiques Age
    st.markdown('<h3 class="section-title">📈 Démographie des Patients</h3>', unsafe_allow_html=True)
    age_cols = st.columns(3)
    age_stats = {
        'min': np.min(df['AGE']),
        'median': np.median(df['AGE']),
        'max': np.max(df['AGE'])
    }
    
    age_metrics = [
        ("🌱 Jeune Patient", age_stats['min'], "ans"),
        ("📊 Âge Médian", age_stats['median'], "ans"), 
        ("🧓 Patient Âgé", age_stats['max'], "ans")
    ]
    
    for col, (title, value, unit) in zip(age_cols, age_metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div style="color: #6c757d; margin-bottom: 0.5rem;">{title}</div>
                <div style="font-size: 2.5rem; color: var(--primary);">{value:.1f}</div>
                <div style="color: #6c757d;">{unit}</div>
            </div>
            """, unsafe_allow_html=True)

    # Section 3: Analyse des Variables
    st.markdown('<h3 class="section-title">📊 Profil Clinique des Patients</h3>', unsafe_allow_html=True)
    analysis_cols = st.columns(2)
    
    with analysis_cols[0]:
        with st.expander("📉 Distribution des Variables", expanded=True):
            selected_var = st.selectbox("Sélectionner une variable", df.columns)
            fig = px.histogram(df, x=selected_var, 
                             color_discrete_sequence=['#2e77d0'],
                             template="plotly_white")
            fig.update_layout(bargap=0.1)
            st.plotly_chart(fig, use_container_width=True)
    
    with analysis_cols[1]:
        with st.expander("🔗 Matrice de Corrélation", expanded=True):
            numeric_df = df.select_dtypes(include=["number"])
            corr_matrix = numeric_df.corr()
            fig = px.imshow(corr_matrix, 
                          color_continuous_scale='Blues',
                          labels={"color": "Corrélation"},
                          aspect="auto")
            fig.update_layout(coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)

    # Section 4: Analyse de Survie
    st.markdown('<h3 class="section-title">⏳ Analyse de Survie Kaplan-Meier</h3>', unsafe_allow_html=True)
    kmf = KaplanMeierFitter()
    
    try:
        kmf.fit(df["Tempsdesuivi (Mois)"], event_observed=df["Deces"])
        fig = px.line(x=kmf.timeline, y=kmf.survival_function_['KM_estimate'],
                    labels={'x': 'Temps (mois)', 'y': 'Probabilité de Survie'},
                    color_discrete_sequence=['#dc3545'])
        fig.add_scatter(x=kmf.timeline, y=1 - kmf.confidence_interval_['KM_estimate_lower_0.95'],
                       line=dict(color='rgba(220, 53, 69, 0.2)'), name='IC 95%')
        fig.update_layout(hovermode="x unified", template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
        
        # Statistiques résumées
        with st.expander("📝 Interprétation Clinique"):
            st.markdown(f"""
            - 📅 **Durée médiane de survie** : {kmf.median_survival_time_:.1f} mois
            - ⚠️ **Risque cumulé à 12 mois** : {1 - kmf.predict(12):.1%}
            - 📉 **Taux de décès global** : {df['Deces'].mean():.1%}
            """)
            
    except Exception as e:
        st.error(f"Erreur dans l'analyse de survie : {str(e)}")

    # Section 5: Analyse des Variables Catégorielles
    st.markdown('<h3 class="section-title">📌 Répartition des Facteurs de Risque</h3>', unsafe_allow_html=True)
    cat_vars = [col for col in df.columns if df[col].dtype == 'object' and col not in ['Deces', 'Tempsdesuivi (Mois)']]
    
    if cat_vars:
        cols = st.columns(2)
        for i, var in enumerate(cat_vars):
            with cols[i % 2]:
                fig = px.pie(df, names=var, 
                            color_discrete_sequence=['#2e77d0', '#22d3ee'],
                            title=f"Répartition {var}")
                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Aucune variable catégorielle détectée dans le jeu de données")

if __name__ == "__main__":
    analyse_descriptive()
