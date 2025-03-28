import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Style CSS personnalisé
st.markdown("""
<style>
    :root {
        --primary: #2e77d0;
        --secondary: #1d5ba6;
        --accent: #22d3ee;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f8faff, #ffffff);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border-left: 4px solid var(--primary);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .analysis-section {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.05);
    }
    
    .stPlotlyChart {
        border-radius: 15px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

def analyse_descriptive():
    st.title("🔍 Exploration des Données Médicales")
    df = load_data()
    if df.empty:
        return

    # Section Aperçu des données
    with st.expander("📂 Aperçu du Jeu de Données", expanded=True):
        st.markdown("""
        <div class='analysis-section'>
            <h3 style='color: var(--primary); margin-top: 0;'>Données Brutes</h3>
            <div style='max-height: 300px; overflow: auto;'>
        """, unsafe_allow_html=True)
        st.dataframe(df.style.format(precision=2).highlight_null(color='#ffcccc')
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='margin-top: 1rem; color: #666;'>
            🔢 Dimensions : {df.shape[0]} patients × {df.shape[1]} variables
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section Statistiques d'âge
    AGE = df['AGE']
    age_stats = {
        'Min': np.min(AGE),
        'Médiane': np.median(AGE),
        'Max': np.max(AGE),
        'Moyenne': np.mean(AGE),
        'Écart-type': np.std(AGE)
    }
    
    cols = st.columns(5)
    stats_icons = ['👶', '📊', '👴', '📐', '📈']
    for (label, value), icon, col in zip(age_stats.items(), stats_icons, cols):
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>{icon}</div>
                <div style='color: var(--primary); font-weight: 600;'>{label}</div>
                <div style='font-size: 1.5rem; color: #333;'>{value:.1f} ans</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section Analyse Univariée/Bivariée
    col1, col2 = st.columns([1, 2])
    
    with col1:
        with st.container():
            st.markdown("<div class='analysis-section'>", unsafe_allow_html=True)
            st.subheader("📌 Distribution des Variables")
            
            selected_var = st.selectbox("Sélectionner une variable", df.columns, key='var_select')
            
            # Analyse de distribution
            fig = make_subplots(rows=2, cols=1, 
                               vertical_spacing=0.1,
                               row_heights=[0.7, 0.3])
            
            # Histogramme
            fig.add_trace(go.Histogram(
                x=df[selected_var],
                name='Distribution',
                marker_color='#2e77d0',
                opacity=0.8
            ), row=1, col=1)
            
            # Boxplot
            fig.add_trace(go.Box(
                x=df[selected_var],
                name='Distribution',
                marker_color='#1d5ba6'
            ), row=2, col=1)
            
            fig.update_layout(
                height=500,
                showlegend=False,
                margin=dict(t=0, b=0),
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown("<div class='analysis-section'>", unsafe_allow_html=True)
            st.subheader("🔗 Analyse des Corrélations")
            
            # Matrice de corrélation améliorée
            numeric_df = df.select_dtypes(include=["number"])
            corr_matrix = numeric_df.corr()
            
            fig = go.Figure()
            fig.add_trace(go.Heatmap(
                z=corr_matrix,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale='RdBu',
                zmin=-1,
                zmax=1,
                hoverongaps=False,
                text=np.round(corr_matrix.values, 2),
                texttemplate="%{text}",
                textfont={"size": 10}
            )
            
            fig.update_layout(
                width=800,
                height=600,
                xaxis_showgrid=False,
                yaxis_showgrid=False,
                xaxis={'side': 'top'},
                yaxis_autorange='reversed',
                coloraxis_colorbar={
                    'title': 'Coefficient',
                    'tickvals': [-1, -0.5, 0, 0.5, 1]
                }
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section Analyse des valeurs manquantes
    with st.expander("🔎 Analyse des Valeurs Manquantes", expanded=True):
        st.markdown("<div class='analysis-section'>", unsafe_allow_html=True)
        missing_data = df.isnull().sum().sort_values(ascending=False)
        missing_percent = (missing_data / len(df)) * 100
        
        fig = px.bar(
            x=missing_percent.index,
            y=missing_percent.values,
            labels={'x': 'Variables', 'y': 'Pourcentage (%)'},
            color=missing_percent.values,
            color_continuous_scale='Reds'
        )
        
        fig.update_layout(
            title='Répartition des Valeurs Manquantes par Variable',
            xaxis_tickangle=45,
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

def load_data():
    # Implémentez votre chargement de données ici
    return pd.DataFrame()

if __name__ == "__main__":
    analyse_descriptive()
