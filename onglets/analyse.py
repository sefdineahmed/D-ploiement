import streamlit as st
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from utils import load_data
import matplotlib.pyplot as plt

def analyse_descriptive():
    # Configuration du style
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .metric-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border-left: 4px solid var(--primary);
        }
        
        .section-title {
            color: var(--primary);
            border-bottom: 3px solid var(--accent);
            padding-bottom: 0.5rem;
            margin: 2rem 0 !important;
        }
        
        .stPlotlyChart {
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("🔬 Analyse Médicale Avancée")
    df = load_data()
    if df.empty:
        return

    # Section Aperçu des données
    with st.expander("📂 Exploration des Données Brutes", expanded=True):
        cols = st.columns([2, 1])
        with cols[0]:
            st.dataframe(df.head(5).style.set_properties(**{'background-color': '#f8f9fa'})
        with cols[1]:
            st.markdown(f"""
                <div class="metric-card">
                    <h3>Dimensions des Données</h3>
                    <p style="font-size: 1.5rem; color: var(--primary); margin: 0;">
                        {df.shape[0]} patients<br>
                        {df.shape[1]} variables
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")

    # Analyse de Survie
    st.markdown("<h2 class='section-title'>📈 Analyse de Survie Kaplan-Meier</h2>", unsafe_allow_html=True)
    kmf = KaplanMeierFitter()
    
    if 'event' in df.columns and 'time' in df.columns:
        kmf.fit(df['time'], event_observed=df['event'])
        fig_km = px.line(
            x=kmf.timeline,
            y=kmf.survival_function_['KM_estimate'],
            labels={'x': 'Temps de suivi (mois)', 'y': 'Probabilité de survie'},
            color_discrete_sequence=['#2e77d0']
        )
        fig_km.update_layout(
            hovermode="x unified",
            title="Courbe de Survie Globale",
            xaxis_title="Temps (mois)",
            yaxis_title="Probabilité de Survie",
            plot_bgcolor='rgba(240, 242, 246, 0.8)'
        )
        st.plotly_chart(fig_km, use_container_width=True)
    else:
        st.warning("⚠️ Colonnes manquantes pour l'analyse de survie")

    # Section Statistiques d'Âge
    st.markdown("<h2 class='section-title'>📊 Démographie des Patients</h2>", unsafe_allow_html=True)
    if 'AGE' in df.columns:
        age_stats = df['AGE'].describe()
        cols = st.columns(3)
        stats = [
            ("Âge Minimum", age_stats['min'], "#22d3ee"),
            ("Âge Médian", age_stats['50%'], "#2e77d0"),
            ("Âge Maximum", age_stats['max'], "#1d5ba6")
        ]
        for col, (title, value, color) in zip(cols, stats):
            with col:
                st.markdown(f"""
                    <div class="metric-card" style="border-color: {color};">
                        <h4>{title}</h4>
                        <div style="font-size: 2rem; color: {color}; font-weight: bold;">
                            {value:.1f} ans
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        
        # Distribution de l'âge
        fig_age = px.histogram(
            df, 
            x='AGE', 
            nbins=20,
            color_discrete_sequence=['#2e77d0'],
            title="Distribution des Âges"
        )
        fig_age.update_layout(
            bargap=0.1,
            xaxis_title="Âge",
            yaxis_title="Nombre de Patients",
            plot_bgcolor='rgba(240, 242, 246, 0.8)'
        )
        st.plotly_chart(fig_age, use_container_width=True)
    else:
        st.error("❌ Colonne 'AGE' non trouvée")

    st.markdown("---")

    # Analyse Multivariée
    st.markdown("<h2 class='section-title'>📉 Analyse des Corrélations</h2>", unsafe_allow_html=True)
    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty:
        corr_matrix = numeric_df.corr()
        fig_corr = px.imshow(
            corr_matrix,
            color_continuous_scale='RdBu_r',
            labels={"color": "Corrélation"},
            aspect="auto"
        )
        fig_corr.update_layout(
            title="Matrice de Corrélation des Paramètres Cliniques",
            xaxis_showgrid=False,
            yaxis_showgrid=False,
            margin=dict(l=50, r=50, b=50, t=50)
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    else:
        st.warning("⚠️ Aucune donnée numérique pour la matrice de corrélation")

    # Analyse des Variables Catégorielles
    st.markdown("<h2 class='section-title'>📌 Répartition des Variables Cliniques</h2>", unsafe_allow_html=True)
    categorical_vars = df.select_dtypes(include=["object", "category"]).columns
    if len(categorical_vars) > 0:
        selected_cat_var = st.selectbox("Choisir une variable catégorielle", categorical_vars)
        fig_pie = px.pie(
            df, 
            names=selected_cat_var,
            hole=0.3,
            color_discrete_sequence=px.colors.sequential.Blues_r,
            title=f"Répartition de {selected_cat_var}"
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("ℹ️ Aucune variable catégorielle trouvée")

    # Section Analyse de Qualité des Données
    st.markdown("<h2 class='section-title'>🔍 Qualité des Données</h2>", unsafe_allow_html=True)
    missing_data = df.isnull().sum().sort_values(ascending=False)
    fig_missing = px.bar(
        missing_data,
        x=missing_data.values,
        y=missing_data.index,
        orientation='h',
        color_discrete_sequence=['#dc3545'],
        title="Valeurs Manquantes par Variable"
    )
    fig_missing.update_layout(
        xaxis_title="Nombre de valeurs manquantes",
        yaxis_title="Variables",
        showlegend=False
    )
    st.plotly_chart(fig_missing, use_container_width=True)

if __name__ == "__main__":
    analyse_descriptive()
