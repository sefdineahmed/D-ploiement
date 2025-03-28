import streamlit as st
import numpy as np
import pandas as pd
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
        
        .header-card {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 2rem;
            border-radius: 16px;
            margin-bottom: 2rem;
        }
        
        .metric-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-left: 4px solid var(--primary);
            transition: transform 0.3s;
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
        }
        
        .viz-card {
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.05);
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='header-card'><h1 style='color:white; margin:0;'>📈 Exploration des Données Médicales</h1></div>", unsafe_allow_html=True)
    
    df = load_data()
    if df.empty:
        return

    # Section Aperçu des données
    with st.expander("🔍 Exploration des Données Brutes", expanded=True):
        st.dataframe(df.head(8).style.highlight_max(color='#f0f4ff').highlight_min(color='#fff0f0')
        st.caption(f"🔢 Dimensions du jeu de données : {df.shape[0]} patients | {df.shape[1]} variables")

    st.markdown("---")
    
    # Métriques d'âge
    AGE = df['AGE']
    age_stats = {
        "min": np.min(AGE),
        "med": np.median(AGE),
        "max": np.max(AGE)
    }

    cols = st.columns(3)
    stats_config = {
        "min": {"title": "Âge Minimum", "icon": "👶", "color": "#22d3ee"},
        "med": {"title": "Âge Médian", "icon": "🎯", "color": "#2e77d0"},
        "max": {"title": "Âge Maximum", "icon": "👴", "color": "#1d5ba6"}
    }

    for (col, stat), key in zip(zip(cols, age_stats.values()), stats_config.keys()):
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="font-size: 2rem; color: {stats_config[key]['color']};">{stats_config[key]['icon']}</div>
                    <div>
                        <h3 style="margin: 0; color: #6c757d;">{stats_config[key]['title']}</h3>
                        <p style="font-size: 2rem; margin: 0; color: {stats_config[key]['color']};">{stat} ans</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Analyse multivariée
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        with st.container():
            st.markdown("<div class='viz-card'>", unsafe_allow_html=True)
            st.subheader("📊 Distribution des Variables")
            selected_var = st.selectbox("Sélectionner une variable", df.columns, key='var_select')
            
            fig = px.histogram(df, x=selected_var, 
                             color_discrete_sequence=[var(--primary)], 
                             nbins=20,
                             template='plotly_white')
            
            fig.update_layout(
                hoverlabel=dict(
                    bgcolor="white",
                    font_size=14,
                    font_family="Arial"
                ),
                xaxis_title_font=dict(size=14),
                yaxis_title_font=dict(size=14)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown("<div class='viz-card'>", unsafe_allow_html=True)
            st.subheader("🌐 Matrice de Corrélation")
            numeric_df = df.select_dtypes(include=["number"])
            corr_matrix = numeric_df.corr()
            
            fig = px.imshow(corr_matrix,
                          color_continuous_scale='RdBu',
                          zmin=-1,
                          zmax=1,
                          labels=dict(color="Corrélation"),
                          aspect="auto")
            
            fig.update_xaxes(side="top")
            fig.update_layout(coloraxis_colorbar=dict(
                title="Coefficient",
                thickness=15,
                len=0.5
            ))
            
            # Ajout des annotations
            annotations = []
            for i, row in enumerate(corr_matrix.values):
                for j, value in enumerate(row):
                    annotations.append(
                        dict(
                            x=j,
                            y=i,
                            text=f"{value:.2f}",
                            font=dict(color="white" if abs(value) > 0.5 else "black"),
                            showarrow=False
                        )
                    )
            fig.update_layout(annotations=annotations)
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
