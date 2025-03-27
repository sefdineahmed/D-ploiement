import streamlit as st
import numpy as np
import plotly.express as px
from utils import FEATURE_CONFIG, encode_features, load_model, predict_survival, clean_prediction, save_new_patient, MODELS
from datetime import date
from fpdf import FPDF
from io import BytesIO

def generate_pdf(report_data):
    """
    Génère un PDF à partir d'un dictionnaire contenant les informations du rapport.
    """
    pdf = FPDF()
    pdf.add_page()
    # Titre du rapport
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 10, "Rapport Médical", ln=True, align="C")
    pdf.ln(10)
    
    # Contenu du rapport
    pdf.set_font("Arial", "", 12)
    for key, value in report_data.items():
        pdf.set_text_color(50, 50, 50)
        pdf.cell(0, 10, f"{key} : {value}", ln=True)
    pdf.ln(10)
    
    # Message final
    pdf.set_font("Arial", "I", 12)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 10, "Ce rapport a été généré automatiquement par la plateforme MED-AI.\nMerci de votre confiance.")
    
    # Sortie dans un buffer BytesIO
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest="S").encode("latin-1"))
    pdf_output.seek(0)
    return pdf_output

def modelisation():
    st.title("🤖 Prédiction de Survie")

    # 1️⃣ Prédiction personnalisée
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
    
    # Vérification de la présence de toutes les colonnes attendues
    missing_columns = [col for col in FEATURE_CONFIG.keys() if col not in input_df.columns]
    if missing_columns:
        st.error(f"❌ Colonnes manquantes : {', '.join(missing_columns)}")
        return
    
    # Choix du modèle pour la prédiction
    model_name = st.selectbox("Choisir un modèle", list(MODELS.keys()))
    model = load_model(MODELS[model_name])
    
    # Zone de prédiction
    cleaned_pred = None
    if st.button("Prédire le temps de survie"):
        if model:
            try:
                pred = predict_survival(model, input_df, model_name)
                cleaned_pred = clean_prediction(pred, model_name)
                if np.isnan(cleaned_pred):
                    raise ValueError("La prédiction renvoyée est NaN.")
                st.metric(label="Survie médiane estimée", value=f"{cleaned_pred:.1f} mois")
                
                # Visualisation graphique de la prédiction
                months = min(int(cleaned_pred), 120)
                fig = px.line(
                    x=list(range(months)),
                    y=[100 - (i / months) * 100 for i in range(months)],
                    labels={"x": "Mois", "y": "Probabilité de survie (%)"},
                    color_discrete_sequence=['#2ca02c']
                )
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"❌ Erreur de prédiction pour {model_name} : {e}")
    
    st.markdown("---")
    if st.button("Enregistrer le patient"):
        save_new_patient(input_df.iloc[0].to_dict())

    # 2️⃣ Analyse des résultats
    st.subheader("Analyse des résultats")
    if cleaned_pred is not None:
        # Préparation des données pour le rapport
        report_data = {
            "Paramètres du patient": input_df.to_dict(orient="records")[0],
            "Modèle choisi": model_name,
            "Survie médiane estimée": f"{cleaned_pred:.1f} mois"
        }
        pdf_report = generate_pdf(report_data)
        st.download_button(
            label="Télécharger le rapport médical complet 📄",
            data=pdf_report,
            file_name="rapport_medical.pdf",
            mime="application/pdf"
        )
    else:
        st.info("Effectuez une prédiction pour générer et télécharger le rapport.")

    st.markdown("---")
    # 3️⃣ Suivi thérapeutique
    st.subheader("Suivi thérapeutique")
    # Option de comparaison des traitements
    treatment_options = ["Chimiothérapie", "Radiothérapie", "Immunothérapie", "Thérapie ciblée"]
    selected_treatments = st.multiselect("Comparez les différentes options de traitement 💊", options=treatment_options)

    # Planification du suivi médical automatisé
    follow_up_date = st.date_input("Planifiez le suivi médical automatisé 🏥", value=date.today())
    if st.button("Confirmer le suivi thérapeutique"):
        if selected_treatments:
            st.success(f"Suivi planifié pour le {follow_up_date} avec les traitements : {', '.join(selected_treatments)}")
        else:
            st.warning("Veuillez sélectionner au moins une option de traitement pour planifier le suivi.")
