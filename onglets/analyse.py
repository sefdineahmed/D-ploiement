import streamlit as st
import plotly.express as px
import numpy as np
from lifelines import KaplanMeierFitter
from utils import load_data

def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    
    if df.empty:
        st.warning("Les données sont vides ou non chargées.")
        return

    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(5))
        st.write(f"Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")
    
    st.markdown("---")

    # Calcul des statistiques de l'âge
    if 'AGE' in df.columns:
        age_min = np.min(df['AGE'])
        age_median = np.median(df['AGE'])
        age_max = np.max(df['AGE'])

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
    
    # Affichage de la matrice de corrélation avec les valeurs
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 Distribution des variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var, color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🌡 Matrice de corrélation")
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r', labels={"color": "Corrélation"})
        st.plotly_chart(fig, use_container_width=True)
        st.write("Valeurs de la corrélation entre les variables :")
        st.dataframe(corr_matrix)

    st.markdown("---")

    # Analyse de Kaplan-Meier
    if 'Survival' in df.columns and 'Event' in df.columns:  # Vérification si les colonnes existent
        st.subheader("🔍 Analyse de Kaplan-Meier")
        
        kmf = KaplanMeierFitter()
        kmf.fit(df['Survival'], event_observed=df['Event'])

        # Graphique de Kaplan-Meier
        fig = kmf.plot_survival_function()
        st.plotly_chart(fig, use_container_width=True)
    
        # Menu pour sélectionner la variable à analyser
        st.subheader("💬 Distributions de Kaplan-Meier pour les variables")
        selected_var_km = st.selectbox("Choisir une variable pour la distribution de Kaplan-Meier", df.columns)
        
        if selected_var_km in df.columns:
            # Séparation des groupes par variable et affichage de Kaplan-Meier
            kmf = KaplanMeierFitter()
            for group in df[selected_var_km].unique():
                group_data = df[df[selected_var_km] == group]
                kmf.fit(group_data['Survival'], event_observed=group_data['Event'], label=str(group))
                kmf.plot_survival_function()

            st.pyplot()
    else:
        st.warning("Les colonnes nécessaires pour l'analyse de Kaplan-Meier ('Survival', 'Event') sont absentes.")
