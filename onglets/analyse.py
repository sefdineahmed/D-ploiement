import pandas as pd

import numpy as np
import streamlit as st
import plotly.express as px
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from utils import load_data
import matplotlib.pyplot as plt

def analyse_descriptive():
    st.title("🔍 Analyse Médico-Statistique")
    df = load_data()
    if df.empty:
        return

    # Style CSS personnalisé
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .data-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.05);
            border: 1px solid rgba(46, 119, 208, 0.1);
        }
        
        .metric-card {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
        }
        
        .hover-card {
            transition: transform 0.3s ease;
        }
        
        .hover-card:hover {
            transform: translateY(-5px);
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        # Section Aperçu des données
        with st.expander("📂 Exploration des Données Brutes", expanded=True):
            st.markdown("<div class='data-card hover-card'>", unsafe_allow_html=True)
            col1, col2 = st.columns([1, 3])
            with col1:
                st.metric("Patients", df.shape[0])
                st.metric("Variables", df.shape[1])
            with col2:
                st.dataframe(df.head(5), height=200)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Section Analyse Démographique
        st.header("📊 Profil Démographique")
        cols = st.columns(3)
        age_stats = {
            "min": np.min(df['AGE']),
            "med": np.median(df['AGE']),
            "max": np.max(df['AGE'])
        }
        
        with cols[0]:
            st.markdown("<div class='metric-card hover-card'>", unsafe_allow_html=True)
            st.metric("Âge Minimum", f"{age_stats['min']} ans")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown("<div class='metric-card hover-card'>", unsafe_allow_html=True)
            st.metric("Âge Médian", f"{age_stats['med']} ans")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with cols[2]:
            st.markdown("<div class='metric-card hover-card'>", unsafe_allow_html=True)
            st.metric("Âge Maximum", f"{age_stats['max']} ans")
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Section Analyse Survie
        st.header("📈 Analyse de Survie")
        kmf = KaplanMeierFitter()
        kmf.fit(df["Tempsdesuivi (Mois)"], df["Deces"])
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='data-card hover-card'>", unsafe_allow_html=True)
            st.subheader("Courbe de Kaplan-Meier")
            fig = px.line(
                kmf.survival_function_,
                x=kmf.survival_function_.index,
                y=kmf.survival_function_['KM_estimate'],
                labels={'x': 'Mois', 'y': 'Probabilité de Survie'},
                color_discrete_sequence=['#2e77d0']
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='data-card hover-card'>", unsafe_allow_html=True)
            st.subheader("Statistiques Clés")
            st.metric("Survie Médiane", f"{kmf.median_survival_time_:.1f} mois")
            st.write(f"**Patients à risque à 12 mois:** {kmf.predict(12):.0%}")
            st.write(f"**Patients à risque à 24 mois:** {kmf.predict(24):.0%}")
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Section Analyse Multivariée
        st.header("🧮 Analyse Multidimensionnelle")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div class='data-card hover-card'>", unsafe_allow_html=True)
            st.subheader("Distribution des Variables")
            selected_var = st.selectbox("Sélectionner une variable", df.columns)
            fig = px.histogram(
                df, 
                x=selected_var, 
                color_discrete_sequence=['#2e77d0'],
                nbins=20
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='data-card hover-card'>", unsafe_allow_html=True)
            st.subheader("Interactions Variables")
            numeric_df = df.select_dtypes(include=["number"])
            corr_matrix = numeric_df.corr()
            fig = px.imshow(
                corr_matrix,
                color_continuous_scale='RdBu_r',
                labels={"color": "Corrélation"},
                aspect="auto"
            )
            fig.update_layout(coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Section Analyse Comparative
        st.header("📌 Analyse Comparative par Sous-Groupes")
        group_var = st.selectbox("Variable de stratification", df.columns)
       
        if group_var in df.columns:
            groups = df[group_var].unique()
            plt.figure(figsize=(10, 6))
            
            for group in groups:
                mask = df[group_var] == group
                kmf.fit(df[mask]["Tempsdesuivi (Mois)"], df[mask]["Deces"])
                plt.step(kmf.timeline, kmf.survival_function_, 
                        label=f"{group_var} = {group}")
            
            plt.xlabel("Temps (Mois)")
            plt.ylabel("Probabilité de Survie")
            plt.title("Courbes de Survie Comparées")
            plt.legend()
            st.pyplot(plt)
            
            # Test du Log-Rank
            results = logrank_test(
                df[df[group_var]==groups[0]]["Tempsdesuivi (Mois)"],
                df[df[group_var]==groups[1]]["Tempsdesuivi (Mois)"],
                df[df[group_var]==groups[0]]["Deces"],
                df[df[group_var]==groups[1]]["Deces"]
            )
            st.write(f"**Test du Log-Rank:** p-value = {results.p_value:.4f}")

if __name__ == "__main__":
    analyse_descriptive()
