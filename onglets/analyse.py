import streamlit as st
import plotly.express as px
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
