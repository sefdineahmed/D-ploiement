import streamlit as st
import numpy as np
import plotly.express as px
from plotly.figure_factory import create_distplot
from lifelines import KaplanMeierFitter
from utils import load_data

def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    if df.empty:
        return

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

    # Matrice de Corrélation
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
        
        # Affichage des valeurs dans la matrice de corrélation
        for i in range(len(corr_matrix.columns)):
            for j in range(len(corr_matrix.columns)):
                fig.add_annotation(
                    x=j, 
                    y=i, 
                    text=f"{corr_matrix.iloc[i, j]:.2f}",
                    showarrow=False,
                    font=dict(size=10, color='white'),
                    align='center'
                )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Courbe de Kaplan-Meier
    st.subheader("📈 Courbes de Kaplan-Meier")
    kmf = KaplanMeierFitter()
    
    # Filtrage des variables 'event' et 'time'
    event_column = 'Deces'  # Changer si nécessaire
    time_column = 'Tempsdesuivi (Mois)'  # Changer si nécessaire
    
    if event_column in df.columns and time_column in df.columns:
        kmf.fit(df[time_column], event_observed=df[event_column])
        
        # Courbe de Kaplan-Meier
        fig = kmf.plot(ci_show=True)
        st.pyplot(fig)
    else:
        st.error("Les colonnes 'Deces' ou 'Tempsdesuivi' ne sont pas présentes dans les données.")

    st.markdown("---")

    # Sélection d'une autre variable pour Kaplan-Meier
    st.subheader("📊 Sélection de variable pour Kaplan-Meier")
    selected_variable = st.selectbox("Choisir une variable pour la distribution Kaplan-Meier", df.columns)
    
    if selected_variable != event_column:  # Éviter d'appliquer Kaplan-Meier à l'event directement
        st.write(f"Analyse de Kaplan-Meier selon la variable **{selected_variable}**.")
        
        # Plot Kaplan-Meier pour les groupes dans la variable sélectionnée
        kmf = KaplanMeierFitter()
        
        for category in df[selected_variable].unique():
            mask = df[selected_variable] == category
            kmf.fit(df[time_column][mask], event_observed=df[event_column][mask], label=str(category))
            kmf.plot(ci_show=True)
        
        st.pyplot()

