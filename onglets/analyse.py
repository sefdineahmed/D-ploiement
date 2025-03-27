import streamlit as st
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from utils import load_data

def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    if df.empty:
        return

    # Vérification des valeurs manquantes et infinies
    if df['Tempsdesuivi (Mois)'].isnull().any() or df['Deces'].isnull().any():
        st.error("Des valeurs manquantes ont été détectées dans les colonnes 'Tempsdesuivi (Mois)' ou 'Deces'. Veuillez vérifier les données.")
        df = df.dropna(subset=['Tempsdesuivi (Mois)', 'Deces'])  # Suppression des lignes avec NaN dans ces colonnes
    
    if np.isinf(df['Tempsdesuivi (Mois)']).any() or np.isinf(df['Deces']).any():
        st.error("Des valeurs infinies ont été détectées dans les colonnes 'Tempsdesuivi (Mois)' ou 'Deces'. Veuillez vérifier les données.")
        df = df.replace([np.inf, -np.inf], np.nan)  # Remplacer les valeurs infinies par NaN
        df = df.dropna(subset=['Tempsdesuivi (Mois)', 'Deces'])  # Suppression des lignes avec NaN

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

    # Encodage des variables catégoriques
    CatCols = df.select_dtypes(include=['object']).columns
    label_encoder = LabelEncoder()
    for col in CatCols:
        df[col] = label_encoder.fit_transform(df[col].astype(str))

    # Initialisation du Kaplan-Meier
    kmf = KaplanMeierFitter()

    # Ajustement du modèle avec les données
    kmf.fit(df['Tempsdesuivi (Mois)'], event_observed=df['Deces'])

    # Tracer la fonction de survie avec les intervalles de confiance
    fig, ax = plt.subplots(figsize=(8, 4))
    kmf.plot_survival_function(ax=ax, ci_show=True)  # Affiche les intervalles de confiance

    # Ajouter les points de censure
    censored_times = df.loc[df['Deces'] == 0, 'Tempsdesuivi (Mois)']
    survival_probabilities = [float(kmf.survival_function_at_times(time).iloc[0]) for time in censored_times]

    ax.scatter(censored_times,
            survival_probabilities,
            color='red',
            label='Censures',
            alpha=0.7)

    # Ajouter les titres et légendes
    ax.set_title('Fonction de survie avec intervalles de confiance et censures')
    ax.set_xlabel('Mois')
    ax.set_ylabel('Probabilité de survie')
    ax.legend()

    st.pyplot(fig)  # Affichage avec Streamlit

    st.markdown("---")

    # Sélection de la variable pour analyser la fonction de survie
    selected_var = st.selectbox("Sélectionner une variable pour l'analyse Kaplan-Meier", df.columns)
    
    if selected_var:
        plot_kaplan_meier(df, selected_var)

def plot_kaplan_meier(df, variable):
    """
    Trace le graphique Kaplan-Meier pour une variable donnée et effectue le test de log-rank.
    """
    # Initialisation de la figure
    fig, ax = plt.subplots(figsize=(8, 4))

    # Instanciation du KaplanMeierFitter
    kmf = KaplanMeierFitter()

    # Tracer les courbes Kaplan-Meier pour chaque groupe de la variable
    for group in df[variable].unique():
        mask = (df[variable] == group)
        kmf.fit(df.loc[mask, 'Tempsdesuivi (Mois)'], event_observed=df.loc[mask, 'Deces'], label=str(group))
        kmf.plot(ax=ax)

    # Test de log-rank entre les groupes
    groups = df[variable].unique()
    if len(groups) == 2:  # Test seulement si deux groupes existent
        group_0 = df.loc[df[variable] == groups[0]]
        group_1 = df.loc[df[variable] == groups[1]]
        results = logrank_test(
            group_0['Tempsdesuivi (Mois)'],
            group_1['Tempsdesuivi (Mois)'],
            event_observed_A=group_0['Deces'],
            event_observed_B=group_1['Deces']
        )
        p_value = results.p_value
        ax.set_title(f"{variable}\nLog-rank p = {p_value:.4f}", fontsize=12)
    else:
        ax.set_title(f"{variable} (Pas de test log-rank, plus de 2 groupes)", fontsize=12)

    # Configurations supplémentaires
    ax.set_xlabel("Temps (mois)", fontsize=10)
    ax.set_ylabel("Probabilité de survie", fontsize=10)
    ax.legend(fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

