import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils import load_data
changer moi le style et donne moi quelque chose très beaux a voir avec une professionnalisme 
ajoute les bibliotheque necessaire

def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    if df.empty:
        return

    # Affichage des premières lignes et dimensions du DataFrame
    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(5))
        st.write(f"Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")
        
    st.markdown("---")
    
    # Calcul des statistiques de l'âge
    AGE = df['AGE']  # Assurez-vous que la colonne AGE existe dans le DataFrame
    age_min = np.min(AGE)
    age_median = np.median(AGE)
    age_max = np.max(AGE)

    # Affichage dans trois colonnes
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Âge minimum")
        st.write(f"{age_min} ans")
    with col2:
        st.subheader("Âge médian")
        st.write(f"{age_median} ans")
    with col3:
        st.subheader("Âge maximum")
        st.write(f"{age_max} ans")
    
    st.markdown("---")
    
    # Matrice de Corrélation et Histogramme de distribution
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 Distribution des variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig_hist = px.histogram(df, x=selected_var, color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with col2:
        st.subheader("🌡 Matrice de corrélation")
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        fig_corr = px.imshow(corr_matrix, color_continuous_scale='RdBu_r', labels={"color": "Corrélation"})
        
        # Annotation des valeurs dans la matrice
        for i in range(len(corr_matrix.columns)):
            for j in range(len(corr_matrix.columns)):
                fig_corr.add_annotation(
                    x=j, 
                    y=i, 
                    text=f"{corr_matrix.iloc[i, j]:.3f}",
                    showarrow=False,
                    font=dict(size=10, color='white'),
                    align='center'
                )
        st.plotly_chart(fig_corr, use_container_width=True)
    
    st.markdown("---")

