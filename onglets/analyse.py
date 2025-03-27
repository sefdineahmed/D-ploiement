import streamlit as st
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from utils import load_data
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

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
                    text=f"{corr_matrix.iloc[i, j]:.2f}",
                    showarrow=False,
                    font=dict(size=10, color='white'),
                    align='center'
                )
        st.plotly_chart(fig_corr, use_container_width=True)
    
    st.markdown("---")
    
    # Encodage des variables catégoriques pour Kaplan-Meier
    cat_cols = df.select_dtypes(include=['object']).columns
    label_encoder = LabelEncoder()
    for col in cat_cols:
        df[col] = label_encoder.fit_transform(df[col].astype(str))
    
    # Courbe de Kaplan-Meier globale
    st.subheader("📈 Courbe de Kaplan-Meier Globale")
    kmf = KaplanMeierFitter()
    if 'Tempsdesuivi (Mois)' in df.columns and 'Deces' in df.columns:
        kmf.fit(df['Tempsdesuivi (Mois)'], event_observed=df['Deces'])
        fig_km = kmf.plot_survival_function(ci_show=True)
        
        # Ajout des points de censure (Deces = 0)
        censored_times = df.loc[df['Deces'] == 0, 'Tempsdesuivi (Mois)']
        survival_probabilities = [float(kmf.survival_function_at_times(time).iloc[0]) for time in censored_times]
        plt.scatter(censored_times, survival_probabilities, color='red', label='Censures', alpha=0.7)
        plt.title('Fonction de survie avec intervalles de confiance et censures')
        plt.xlabel('Mois')
        plt.ylabel('Probabilité de survie')
        plt.legend()
        st.pyplot(plt.gcf())
        plt.clf()
    else:
        st.error("Les colonnes 'Tempsdesuivi (Mois)' et/ou 'Deces' sont absentes.")
    
    st.markdown("---")
    
    # Sélection interactive d'une variable pour Kaplan-Meier
    st.subheader("📊 Analyse Kaplan-Meier par variable")
    km_variables = ['Cardiopathie', 'Ulceregastrique', 'Douleurepigastrique', 'Ulcero-bourgeonnant', 
                    'Denitrution', 'Tabac', 'Mucineux', 'Infiltrant', 'Stenosant', 'Metastases', 'Adenopathie']
    selected_variable = st.selectbox("Choisir une variable pour l'analyse Kaplan-Meier", km_variables)
    
    def plot_kaplan_meier(variable):
        fig, ax = plt.subplots(figsize=(8, 4))
        kmf_local = KaplanMeierFitter()
        # Tracer pour chaque groupe de la variable
        for group in sorted(df[variable].unique()):
            mask = (df[variable] == group)
            kmf_local.fit(df.loc[mask, 'Tempsdesuivi (Mois)'], event_observed=df.loc[mask, 'Deces'], label=str(group))
            kmf_local.plot(ax=ax, ci_show=True)
        ax.set_xlabel("Temps (mois)", fontsize=10)
        ax.set_ylabel("Probabilité de survie", fontsize=10)
        ax.legend(fontsize=10)
        ax.set_title(f"Kaplan-Meier pour {variable}", fontsize=12)
        plt.tight_layout()
        return fig
    
    fig_selected = plot_kaplan_meier(selected_variable)
    st.pyplot(fig_selected)
