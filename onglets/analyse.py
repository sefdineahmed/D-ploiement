import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils import load_data

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
        
        .data-card {
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            margin: 1rem 0;
        }
        
        .metric-card {
            background: #f8faff;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            border-left: 4px solid var(--primary);
            transition: transform 0.3s;
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
        }
        
        .st-ae {
            border-radius: 12px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='header-card'><h1 style='margin:0;'>📊 Analyse Exploratoire des Données</h1></div>", unsafe_allow_html=True)
    
    df = load_data()
    if df.empty:
        st.error("Aucune donnée disponible")
        return

    # Section Aperçu des données
    with st.expander("🔍 Exploration des Données Brutes", expanded=True):
        st.markdown("<div class='data-card'>", unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.dataframe(df.head(5).style.highlight_max(color='#2e77d030')
        with col2:
            st.metric("Patients", df.shape[0])
            st.metric("Variables", df.shape[1])
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # Statistiques d'âge
    st.markdown("<h2 style='color: var(--primary);'>📈 Distribution des Âges</h2>", unsafe_allow_html=True)
    AGE = df['AGE']
    cols = st.columns(3)
    stats = [
        ("Âge Minimum", np.min(AGE)),
        ("Âge Médian", np.median(AGE)),
        ("Âge Maximum", np.max(AGE))
    ]
    
    for col, (title, value) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: var(--secondary); margin:0 0 1rem 0;'>{title}</h3>
                <div style='font-size: 2rem; color: var(--primary); font-weight: bold;'>
                    {value:.1f} ans
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")

    # Analyses avancées
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("<div class='data-card'>", unsafe_allow_html=True)
        st.markdown("### 📉 Distribution des Variables")
        selected_var = st.selectbox("Sélectionnez une variable", df.columns, key='var_select')
        fig = px.histogram(df, x=selected_var, 
                         color_discrete_sequence=['#2e77d0'],
                         template='plotly_white')
        fig.update_layout(
            bargap=0.1,
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='data-card'>", unsafe_allow_html=True)
        st.markdown("### 🔗 Matrice de Corrélation")
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        fig = px.imshow(corr_matrix,
                      color_continuous_scale='Blues',
                      labels=dict(color="Corrélation"),
                      template='plotly_white')
        
        fig.update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            xaxis_showgrid=False,
            yaxis_showgrid=False
        )
        
        # Ajout des annotations
        annotations = []
        for i, row in enumerate(corr_matrix.values):
            for j, value in enumerate(row):
                annotations.append(
                    dict(
                        x=j,
                        y=i,
                        text=f"{value:.2f}",
                        font=dict(color="white" if abs(value) > 0.5 else "#2e77d0"),
                        showarrow=False
                    )
                )
        fig.update_layout(annotations=annotations)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    analyse_descriptive()
