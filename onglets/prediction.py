import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from utils import FEATURE_CONFIG, encode_features, load_model, predict_survival, clean_prediction, save_new_patient, MODELS
from io import BytesIO

# 📌 Configuration de la page
st.set_page_config(page_title="MED-AI - Prédiction en oncologie", page_icon="⚕️", layout="wide")

def modelisation():
    st.title("🤖 Prédiction de Survie en Oncologie Digestive")

    # 🩺 **Section 1 : Entrée des paramètres cliniques**
    with st.expander("📋 Paramètres du patient", expanded=True):
        inputs = {}
        cols = st.columns(3)
        for i, (feature, label) in enumerate(FEATURE_CONFIG.items()):
            with cols[i % 3]:
                if feature == "AGE":
                    inputs[feature] = st.number_input(label, min_value=18, max_value=120, value=50, key=feature)
                else:
                    inputs[feature] = st.selectbox(label, options=["Non", "Oui"], key=feature)
    
    input_df = encode_features(inputs)
    st.markdown("---")

    # 🛠️ Vérification des données manquantes
    missing_columns = [col for col in FEATURE_CONFIG.keys() if col not in input_df.columns]
    if missing_columns:
        st.error(f"❌ Colonnes manquantes : {', '.join(missing_columns)}")
        return
    
    # 🧠 **Sélection du modèle**
    model_name = st.selectbox("Choisir un modèle de prédiction", list(MODELS.keys()))
    model = load_model(MODELS[model_name])

    # 🔮 **Prédiction**
    if st.button("🔍 Prédire le temps de survie"):
        if model:
            try:
                pred = predict_survival(model, input_df, model_name)
                cleaned_pred = clean_prediction(pred, model_name)
                if np.isnan(cleaned_pred):
                    raise ValueError("La prédiction renvoyée est NaN.")
                
                # 📊 **Affichage du résultat**
                st.metric(label="📅 Survie médiane estimée", value=f"{cleaned_pred:.1f} mois")
                
                # 📉 **Courbe de survie**
                months = min(int(cleaned_pred), 120)
                fig = px.line(
                    x=list(range(months)),
                    y=[100 - (i / months) * 100 for i in range(months)],
                    labels={"x": "Mois", "y": "Probabilité de survie (%)"},
                    color_discrete_sequence=['#2ca02c']
                )
                st.plotly_chart(fig, use_container_width=True)

                # 📂 **Téléchargement du rapport**
                pdf_bytes = generate_report(cleaned_pred, input_df)
                st.download_button(label="📄 Télécharger le rapport médical", data=pdf_bytes, file_name="rapport_medical.pdf", mime="application/pdf")

                # 🔬 **Analyse avancée**
                st.subheader("📊 Analyse des prédictions")
                visualize_prediction_distribution()

            except Exception as e:
                st.error(f"❌ Erreur de prédiction pour {model_name} : {e}")

    # 📌 **Suivi thérapeutique**
    st.markdown("---")
    st.subheader("💊 Comparaison des Options Thérapeutiques")
    with st.expander("📌 Sélectionnez une stratégie de traitement", expanded=False):
        option = st.radio("Options disponibles :", ["Chimiothérapie", "Immunothérapie", "Traitement combiné"])
        st.write(f"📌 Vous avez sélectionné : **{option}**")

    # 📥 **Enregistrement du patient**
    if st.button("💾 Enregistrer le patient"):
        save_new_patient(input_df.iloc[0].to_dict())
        st.success("✅ Données patient enregistrées avec succès.")

# 📝 **Fonction pour générer un rapport médical PDF**
def generate_report(prediction, patient_data):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Rapport Médical - Prédiction de Survie", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Survie médiane estimée : {prediction:.1f} mois", ln=True)
    
    pdf.cell(200, 10, "🔹 Paramètres du patient :", ln=True)
    for key, value in patient_data.items():
        pdf.cell(200, 10, f"- {key}: {value}", ln=True)
    
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    return pdf_output.getvalue()

# 📊 **Visualisation de la distribution des prédictions**
def visualize_prediction_distribution():
    data = np.random.normal(12, 5, 100)  # Génération de données fictives
    fig, ax = plt.subplots()
    ax.hist(data, bins=15, color='skyblue', edgecolor='black')
    ax.set_xlabel("Temps de survie (mois)")
    ax.set_ylabel("Nombre de patients")
    ax.set_title("Distribution des prédictions de survie")
    st.pyplot(fig)
