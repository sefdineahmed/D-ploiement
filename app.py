import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from lifelines import KaplanMeierFitter, CoxPHFitter

# Charger les modèles
cox_model = joblib.load("models/coxph.joblib")
rsf_model = joblib.load("models/rsf.joblib")
gbst_model = joblib.load("models/gbst.joblib")

# Charger les données
DATA_PATH = "data/GastricCancerData.xlsx"
df = pd.read_excel(DATA_PATH)

# Définition des variables clés
features = ['AGE', 'Cardiopathie', 'Ulceresgastrique', 'Douleurepigastrique',
            'Ulcero-bourgeonnant', 'Denitrution', 'Tabac', 'Mucineux',
            'Infiltrant', 'Stenosant', 'Metastases', 'Adenopathie']
target = ['Tempsdesuivi (Mois)', 'Deces']

# Barre de navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Aller à", ["Accueil", "Formulaire Patient", "Analyse Descriptive", "Analyse de Survie", "Prédiction", "Aide & Contact"])

# 📌 **Accueil**
if menu == "Accueil":
    st.title("🩺 Application de Prédiction du Temps de Survie")
    st.image("assets/header.jpg", use_column_width=True)
    st.write("Bienvenue sur l'application d'aide à la décision pour l'estimation du temps de survie des patients atteints du cancer de l'estomac.")

# 📌 **Formulaire Patient**
elif menu == "Formulaire Patient":
    st.title("📋 Formulaire Patient")
    
    patient_data = {}
    for feature in features:
        patient_data[feature] = st.number_input(f"{feature}", value=0)
    
    if st.button("Enregistrer"):
        new_data = pd.DataFrame([patient_data])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(DATA_PATH, index=False)
        st.success("Les données du patient ont été enregistrées avec succès !")

# 📌 **Analyse Descriptive**
elif menu == "Analyse Descriptive":
    st.title("📊 Analyse Descriptive")

    # Statistiques générales
    st.write("### Statistiques générales")
    st.write(df.describe())

    # Matrice de corrélation
    st.write("### Matrice de corrélation")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(fig)

# 📌 **Analyse de Survie**
elif menu == "Analyse de Survie":
    st.title("📈 Analyse de Survie")

    kmf = KaplanMeierFitter()
    kmf.fit(df["Tempsdesuivi (Mois)"], event_observed=df["Deces"])
    
    st.write("### Courbe de Kaplan-Meier")
    fig, ax = plt.subplots()
    kmf.plot_survival_function(ax=ax)
    st.pyplot(fig)

    st.write("### Modèle de Cox")
    cph = CoxPHFitter()
    cph.fit(df[features + target], duration_col="Tempsdesuivi (Mois)", event_col="Deces")
    st.write(cph.summary)

# 📌 **Prédiction**
elif menu == "Prédiction":
    st.title("🤖 Prédiction du Temps de Survie")

    input_data = np.array([[st.number_input(f"{feature}", value=0) for feature in features]])
    
    if st.button("Prédire"):
        pred_cox = cox_model.predict_median(input_data)
        pred_rsf = rsf_model.predict(input_data)
        pred_gbst = gbst_model.predict(input_data)

        st.write(f"⏳ **Prédiction Cox** : {pred_cox} mois")
        st.write(f"🌲 **Prédiction Random Survival Forest** : {pred_rsf} mois")
        st.write(f"📊 **Prédiction GBST** : {pred_gbst} mois")

# 📌 **Aide & Contact**
elif menu == "Aide & Contact":
    st.title("📞 Aide & Contact")
    st.write("📧 Email : contact@medapp.com")
    st.write("📞 Téléphone : +221 77 123 45 67")
    st.write("🌍 Site web : [medapp.com](https://medapp.com)")
