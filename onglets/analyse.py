import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter
from utils import load_data

def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    if df.empty:
        st.error("Les données sont vides !")
        return

    # 1️⃣ Aperçu des données brutes
    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(5))
        st.write(f"Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")
    
    st.markdown("---")
    
    # 2️⃣ Calcul des statistiques de l'âge
    if 'AGE' in df.columns:
        age_min = df['AGE'].min()
        age_median = df['AGE'].median()
        age_max = df['AGE'].max()

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
    
    # 3️⃣ Distribution des variables
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 Distribution des variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var, color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig, use_container_width=True)
    
    # 4️⃣ Matrice de corrélation avec les valeurs affichées
    with col2:
        st.subheader("🌡 Matrice de corrélation")
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r', labels={"color": "Corrélation"})
        
        # Ajouter les valeurs dans la matrice de corrélation
        for i in range(corr_matrix.shape[0]):
            for j in range(corr_matrix.shape[1]):
                fig.add_annotation(
                    x=j, y=i, z=corr_matrix.iloc[i, j],
                    text=f"{corr_matrix.iloc[i, j]:.2f}",
                    showarrow=False,
                    font=dict(size=10, color="white"),
                    align="center"
                )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # 5️⃣ Courbe de Kaplan-Meier
    if 'Deces' in df.columns and 'Tempsdesuivi (Mois)' in df.columns:
        st.subheader("🔬 Courbe de Kaplan-Meier")
        
        kmf = KaplanMeierFitter()
        
        # Menu pour choisir les variables à analyser
        selected_variable = st.selectbox("Sélectionner une variable pour stratifier les courbes de Kaplan-Meier", df.columns)
        if selected_variable != 'Deces' and selected_variable != 'Tempsdesuivi (Mois)':
            kmf.fit(df['Tempsdesuivi (Mois)'], event_observed=df['Deces'], label='Tous les patients')
        else:
            kmf.fit(df['Tempsdesuivi'], event_observed=df['Deces'], label=selected_variable)
        
        # Affichage de la courbe de Kaplan-Meier
        kmf.plot_survival_function()
        st.pyplot(kmf.plot())
        
    else:
        st.warning("Les colonnes nécessaires pour la courbe de Kaplan-Meier ('Deces', 'Tempsdesuivi (Mois)') sont manquantes.")
