import streamlit as st
import numpy as np
import plotly.express as px
from datetime import date
import io
from fpdf import FPDF
from utils import FEATURE_CONFIG, encode_features, load_model, predict_survival, clean_prediction, save_new_patient, MODELS

# Style CSS personnalisé
st.markdown("""
<style>
    :root {
        --primary: #2e77d0;
        --secondary: #1d5ba6;
        --accent: #22d3ee;
    }
    
    .st-emotion-cache-1y4p8pa {
        padding: 2rem 1rem;
    }
    
    .header-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
    
    .prediction-card {
        background: linear-gradient(135deg, #f8fafc, #ffffff);
        border-left: 4px solid var(--primary);
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .model-selector {
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 2px solid var(--primary) !important;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.8rem 2rem !important;
        transition: all 0.3s !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(46, 119, 208, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

def generate_pdf_report(input_data, model_name, cleaned_pred):
    pdf = FPDF()
    pdf.add_page()
    
    # En-tête professionnel
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(46, 119, 208)
    pdf.cell(0, 15, "Rapplet Médical MED-AI", ln=True, align='C')
    
    # Informations patient
    pdf.set_font('Arial', '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, f"Date : {date.today().strftime('%d/%m/%Y')}", ln=True)
    
    # Section paramètres avec tableau
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 15, "Paramètres Cliniques", ln=True)
    pdf.set_fill_color(240, 248, 255)
    
    # Tableau des données
    pdf.set_font('Arial', '', 12)
    col_widths = [60, 60]
    for key, value in input_data.items():
        pdf.cell(col_widths[0], 8, FEATURE_CONFIG.get(key, key), 1, 0, 'L', 1)
        pdf.cell(col_widths[1], 8, str(value), 1, 1, 'L')
    
    # Section prédiction
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 15, "Résultats de Prédiction", ln=True)
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 8, f"Modèle utilisé : {model_name}", ln=True)
    pdf.set_text_color(46, 119, 208)
    pdf.cell(0, 8, f"Survie médiane estimée : {cleaned_pred:.1f} mois", ln=True)
    
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    return pdf_buffer.getvalue()

def modelisation():
    st.title("📊 Prédiction Intelligente de Survie")
    
    # Section paramètres patient
    with st.container():
        st.markdown("<div class='header-card'>", unsafe_allow_html=True)
        st.subheader("📋 Profil Patient")
        inputs = {}
        cols = st.columns(3)
        for i, (feature, label) in enumerate(FEATURE_CONFIG.items()):
            with cols[i % 3]:
                if feature == "AGE":
                    inputs[feature] = st.number_input(
                        label, 
                        min_value=18, 
                        max_value=120, 
                        value=50,
                        help="Âge du patient en années"
                    )
                else:
                    inputs[feature] = st.selectbox(
                        label, 
                        options=["Non", "Oui"],
                        help="Présence de la caractéristique clinique"
                    )
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Calcul et résultats
    input_df = encode_features(inputs)
    model_name = st.selectbox(
        "🧠 Sélection du Modèle d'IA", 
        list(MODELS.keys()),
        help="Choisir l'algorithme de prédiction"
    )
    
    if st.button("🔮 Calculer la Prédiction", use_container_width=True):
        with st.spinner("Analyse en cours..."):
            try:
                model = load_model(MODELS[model_name])
                pred = predict_survival(model, input_df, model_name)
                cleaned_pred = clean_prediction(pred, model_name)
                
                # Affichage résultats
                with st.container():
                    st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.metric(
                            label="**Survie Médiane Estimée**", 
                            value=f"{cleaned_pred:.1f} mois",
                            help="Durée médiane de survie prédite avec intervalle de confiance"
                        )
                    with col2:
                        months = min(int(cleaned_pred), 120)
                        fig = px.line(
                            x=list(range(months)),
                            y=[100 - (i / months) * 100 for i in range(months)],
                            labels={"x": "Mois", "y": "Probabilité de Survie (%)"},
                            color_discrete_sequence=['#2e77d0']
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Génération rapport
                    pdf_bytes = generate_pdf_report(
                        input_df.to_dict(orient='records')[0], 
                        model_name, 
                        cleaned_pred
                    )
                    st.download_button(
                        label="📥 Télécharger le Rapport Complet",
                        data=pdf_bytes,
                        file_name="rapport_medical.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
            except Exception as e:
                st.error(f"Erreur de prédiction : {str(e)}")
    
    # Section suivi thérapeutique
    st.markdown("---")
    with st.expander("📅 Planification du Suivi Thérapeutique", expanded=True):
        treatment_cols = st.columns(2)
        with treatment_cols[0]:
            selected_treatments = st.multiselect(
                "Options Thérapeutiques",
                options=["Chimiothérapie", "Radiothérapie", "Immunothérapie"],
                help="Sélectionner les traitements à comparer"
            )
        with treatment_cols[1]:
            follow_up_date = st.date_input(
                "Date de Suivi Recommandée",
                value=date.today(),
                help="Date préconisée pour le prochain examen"
            )
        
        if st.button("💾 Enregistrer le Plan de Traitement", use_container_width=True):
            if selected_treatments:
                save_new_patient(input_df.iloc[0].to_dict())
                st.toast("Plan de traitement enregistré avec succès !")
            else:
                st.warning("Veuillez sélectionner au moins un traitement")

if __name__ == "__main__":
    modelisation()
