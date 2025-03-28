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
    # Style CSS amélioré
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        .metric-box {
            padding: 1.5rem;
            border-radius: 10px;
            background: rgba(46, 119, 208, 0.1);
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("📈 Analyse de Survie Oncologique")
    
    # Chargement des données
    df = load_data()
    if df.empty:
        st.error("Aucune donnée chargée")
        return

    # Nettoyage des colonnes
    try:
        df['Tempsdesuivi (Mois)'] = pd.to_numeric(df['Tempsdesuivi (Mois)'], errors='coerce')
        df = df.dropna(subset=['Tempsdesuivi (Mois)', 'Statut'])
    except KeyError as e:
        st.error(f"Colonne manquante : {e}")
        return

    # Section métriques
    with st.container():
        cols = st.columns(3)
        with cols[0]:
            st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
            st.metric("Patients suivis", f"{len(df):,}")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
            median_survival = df['Tempsdesuivi (Mois)'].median()
            st.metric("Survie médiane", f"{median_survival:.1f} mois")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with cols[2]:
            st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
            event_rate = df['Statut'].mean() * 100
            st.metric("Taux d'événements", f"{event_rate:.1f}%")
            st.markdown("</div>", unsafe_allow_html=True)

    # Courbe de Kaplan-Meier
    st.markdown("---")
    st.subheader("📉 Courbe de Survie de Kaplan-Meier")
    
    kmf = KaplanMeierFitter()
    kmf.fit(df['Tempsdesuivi (Mois)'], df['Statut'])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    kmf.plot_survival_function(ax=ax, ci_show=True)
    ax.set_title('Courbe de Survie Globale')
    ax.set_xlabel('Mois de suivi')
    ax.set_ylabel('Probabilité de survie')
    st.pyplot(fig)

if __name__ == "__main__":
    analyse_descriptive()
