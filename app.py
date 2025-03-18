import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test
from sksurv.metrics import concordance_index_censored
import tensorflow as tf

# Charger les modèles de survie
cox_model = joblib.load("models/coxph.joblib")
rsf_model = joblib.load("models/rsf.joblib")
gbst_model = joblib.load("models/gbst.joblib")
deepsurv_model = tf.keras.models.load_model("models/deepsurv.keras")

# Charger les données
df = pd.read_excel("data/GastricCancerData.xlsx", skiprows=1)

# Liste des variables utilisées
variables = ['AGE', 'Cardiopathie', 'Ulceregastrique', 'Douleurepigastrique',
             'Ulcero-bourgeonnant', 'Denitrution', 'Tabac', 'Mucineux', 
             'Infiltrant', 'Stenosant', 'Metastases', 'Adenopathie']
time_col = "Tempsdesuivi (Mois)"
event_col = "Deces"

# --- Interface Streamlit ---
st.set_page_config(page_title="Prédiction de survie - Cancer de l'estomac", layout="wide")

# Barre de navigation
menu = st.sidebar.radio("Navigation", ["Accueil", "Formulaire Patient", "Analyse Descriptive",
                                       "Analyse de Survie", "Prédiction", "Aide & Contact"])

# --- Page d'accueil ---
if menu == "Accueil":
    st.title("🩺 Outil d'aide à la décision pour le cancer de l'estomac")
    st.image("assets/header.jpg", use_column_width=True)
    st.write("""
    Cette application permet d'analyser et de prédire le temps de survie des patients atteints de cancer de l'estomac au Sénégal.
    """)

# --- Formulaire Patient ---
elif menu == "Formulaire Patient":
    st.title("📋 Formulaire Patient")
    st.write("Veuillez entrer les informations du patient :")

    # Création du formulaire interactif
    input_data = {}
    for var in variables:
        input_data[var] = st.number_input(var, min_value=0, max_value=100, value=50)

    if st.button("Enregistrer"):
        st.success("Données enregistrées avec succès ✅")

# --- Analyse Descriptive ---
elif menu == "Analyse Descriptive":
    st.title("📊 Analyse Descriptive")
    
    st.subheader("Aperçu des données")
    st.write(df.head())

    st.subheader("Statistiques de base")
    st.write(df.describe())

    st.subheader("Corrélation entre les variables")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(plt)

# --- Analyse de Survie ---
elif menu == "Analyse de Survie":
    st.title("⏳ Analyse de Survie")

    # Kaplan-Meier
    kmf = KaplanMeierFitter()
    kmf.fit(df[time_col], event_observed=df[event_col])

    st.subheader("Courbe de survie Kaplan-Meier")
    plt.figure(figsize=(8, 5))
    kmf.plot_survival_function()
    plt.xlabel("Temps (mois)")
    plt.ylabel("Probabilité de survie")
    plt.title("Courbe de survie Kaplan-Meier")
    st.pyplot(plt)

    # Test de Log-Rank
    st.subheader("Test de Log-Rank")
    group1 = df[df["Traitement"] == 0]
    group2 = df[df["Traitement"] == 1]
    result = logrank_test(group1[time_col], group2[time_col], 
                          event_observed_A=group1[event_col], event_observed_B=group2[event_col])
    st.write(f"P-Value du test log-rank : {result.p_value:.4f}")

# --- Prédiction ---
elif menu == "Prédiction":
    st.title("🔮 Prédiction du Temps de Survie")

    st.write("Veuillez entrer les informations du patient pour effectuer une prédiction :")
    
    input_data = np.array([st.number_input(var, min_value=0, max_value=100, value=50) for var in variables]).reshape(1, -1)

    if st.button("Prédire"):
        cox_pred = cox_model.predict_survival_function(input_data)
        rsf_pred = rsf_model.predict(input_data)
        gbst_pred = gbst_model.predict(input_data)
        deepsurv_pred = deepsurv_model.predict(input_data)

        # Affichage des résultats
        st.subheader("Résultats des Prédictions")
        st.write(f"**Modèle de Cox** : {cox_pred[0][0]:.2f} mois")
        st.write(f"**Random Survival Forest** : {rsf_pred[0]:.2f} mois")
        st.write(f"**Gradient Boosting Survival Trees** : {gbst_pred[0]:.2f} mois")
        st.write(f"**DeepSurv** : {deepsurv_pred[0][0]:.2f} mois")

        # Graphique de prédiction
        plt.figure(figsize=(8, 5))
        plt.bar(["Cox", "RSF", "GBST", "DeepSurv"], 
                [cox_pred[0][0], rsf_pred[0], gbst_pred[0], deepsurv_pred[0][0]],
                color=["blue", "green", "orange", "red"])
        plt.ylabel("Temps de survie estimé (mois)")
        plt.title("Comparaison des prédictions")
        st.pyplot(plt)

# --- Aide & Contact ---
elif menu == "Aide & Contact":
    st.title("📞 Aide & Contact")
    st.write("Si vous avez des questions, contactez-nous :")
    st.write("📧 Email : contact@medsurv.com")
    st.write("📱 Téléphone : +221 77 123 45 67")
    st.image("assets/team.jpg", use_column_width=True)
