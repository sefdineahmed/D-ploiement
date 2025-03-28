import streamlit as st
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from utils import load_data
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

def analyse_descriptive():
    # Style CSS personnalisé
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 1rem;
        }
        
        .data-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(46, 119, 208, 0.1);
        }
        
        .metric-card {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            transition: transform 0.3s;
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
        }
        
        .section-title {
            font-family: 'Inter', sans-serif;
            color: var(--primary);
            border-left: 4px solid var(--accent);
            padding-left: 1rem;
            margin: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        # Titre principal
        st.markdown("""
            <h1 style="color: var(--primary); text-align: center; margin-bottom: 2rem;">
                📈 Analyse Exploratoire des Données Médicales
            </h1>
        """, unsafe_allow_html=True)

        # Section aperçu des données
        with st.expander("🔍 Aperçu des Données Brutes", expanded=True):
            df = load_data()
            if df.empty:
                return
                
            st.markdown("""
                <div class='data-card'>
                    <div style="max-height: 300px; overflow: auto;">
            """, unsafe_allow_html=True)
            st.dataframe(df.head(10).style.set_properties(**{'background-color': '#f8f9fa'})
            st.markdown("</div></div>", unsafe_allow_html=True)
            st.caption(f"Dimensions du jeu de données : {df.shape[0]} patients, {df.shape[1]} variables")

        # Section statistiques d'âge
        st.markdown("<h2 class='section-title'>📊 Démographie des Patients</h2>", unsafe_allow_html=True)
        AGE = df['AGE']
        
        cols = st.columns(3)
        stats = [
            {"title": "Âge Minimum", "value": np.min(AGE), "icon": "👶"},
            {"title": "Âge Médian", "value": np.median(AGE), "icon": "🎯"},
            {"title": "Âge Maximum", "value": np.max(AGE), "icon": "👴"}
        ]
        
        for col, stat in zip(cols, stats):
            with col:
                st.markdown(f"""
                    <div class='metric-card'>
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{stat['icon']}</div>
                        <h3 style="margin: 0 0 0.5rem; color: white;">{stat['title']}</h3>
                        <p style="font-size: 1.5rem; margin: 0; font-weight: bold;">{stat['value']:.1f} ans</p>
                    </div>
                """, unsafe_allow_html=True)

        # Distribution d'âge interactive
        st.markdown("<h2 class='section-title'>📅 Distribution des Âges</h2>", unsafe_allow_html=True)
        fig = px.histogram(
            df, 
            x='AGE', 
            nbins=20,
            color_discrete_sequence=['#2e77d0'],
            marginal='rug',
            template='plotly_white'
        )
        fig.update_layout(
            title="Répartition par Tranche d'Âge",
            xaxis_title="Âge",
            yaxis_title="Nombre de Patients",
            hoverlabel=dict(bgcolor="white", font_size=16)
        st.plotly_chart(fig, use_container_width=True)

        # Analyse des variables
        st.markdown("<h2 class='section-title'>🔍 Analyse des Variables</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            selected_var = st.selectbox(
                "Sélectionner une Variable", 
                df.columns,
                help="Choisissez une variable pour analyser sa distribution"
            )
            
        with col2:
            st.markdown("<div class='data-card'>", unsafe_allow_html=True)
            fig = px.histogram(
                df, 
                x=selected_var, 
                color_discrete_sequence=['#1d5ba6'],
                template='ggplot2'
            )
            fig.update_layout(
                title=f"Distribution de {selected_var}",
                xaxis_title=selected_var,
                yaxis_title="Fréquence",
                bargap=0.1
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # Matrice de corrélation améliorée
        st.markdown("<h2 class='section-title'>🔗 Analyse de Corrélation</h2>", unsafe_allow_html=True)
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        
        fig = px.imshow(
            corr_matrix,
            color_continuous_scale='RdBu',
            aspect="auto",
            labels=dict(color="Corrélation"),
            template='seaborn'
        )
        fig.update_layout(
            title="Matrice de Corrélation des Variables Numériques",
            xaxis_showgrid=False,
            yaxis_showgrid=False,
            coloraxis_colorbar=dict(title="Coefficient", thickness=20)
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)
