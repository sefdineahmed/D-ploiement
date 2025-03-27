import streamlit as st
import numpy as np
import plotly.express as px
from utils import FEATURE_CONFIG, encode_features, load_model, predict_survival, clean_prediction, save_new_patient, MODELS

def modelisation():
    st.title("🤖 Prédiction de Survie en Oncologie Digestive")

    # 🚀 **Ajout d'un menu latéral**
    st.sidebar.header("📌 Navigation")
    st.sidebar.markdown("🔹 **1️⃣ Prédiction personnalisée**")
    st.sidebar.markdown("🔹 **2️⃣ Analyse des résultats**")
    st.sidebar.markdown("🔹 **3️⃣ Suivi thérapeutique**")
    
    st.markdown("---")

    # 1️⃣ **Prédiction personnalisée**
    with st.expander("📋 1️⃣ Saisissez les paramètres du patient", expanded=True):
        st.info("Renseignez les informations du patient pour générer une prédiction.")
        
        inputs = {}
        cols = st.columns(3)
        for i, (feature, label) in enumerate(FEATURE_CONFIG.items()):
            with cols[i % 3]:
                if feature == "AGE":
                    inputs[feature] = st.number_input(label, min_value=18, max_value=120, value=50, key=feature)
                else:
                    inputs[feature] = st.selectbox(label, options=["Non", "Oui"], key=feature)
    
    # Conversion des données d'entrée
    input_df = encode_features(inputs)
    
    st.markdown("---")

    # Vérification des colonnes manquantes
    missing_columns = [col for col in FEATURE_CONFIG.keys() if col not in input_df.columns]
    if missing_columns:
        st.error(f"❌ Colonnes manquantes : {', '.join(missing_columns)}")
        return

    # Sélection du modèle
    model_name = st.selectbox("🧠 Choisissez un modèle de prédiction", list(MODELS.keys()))
    model = load_model(MODELS[model_name])
    
    st.markdown("---")

    # 2️⃣ **Analyse des résultats**
    if st.button("🚀 Prédire le temps de survie"):
        if model:
            try:
                pred = predict_survival(model, input_df, model_name)
                cleaned_pred = clean_prediction(pred, model_name)

                if np.isnan(cleaned_pred):
                    raise ValueError("La prédiction renvoyée est NaN.")
                
                st.success("✅ Prédiction réussie !")
                st.metric(label="📊 Survie médiane estimée", value=f"{cleaned_pred:.1f} mois")

                # **Graphique interactif**
                months = min(int(cleaned_pred), 120)
                fig = px.line(
                    x=list(range(months)),
                    y=[100 - (i / months) * 100 for i in range(months)],
                    labels={"x": "Mois", "y": "Probabilité de survie (%)"},
                    color_discrete_sequence=['#2ca02c']
                )
                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"❌ Erreur de prédiction : {e}")

    st.markdown("---")

    # 3️⃣ **Suivi thérapeutique**
    with st.expander("💊 3️⃣ Options de traitement et suivi", expanded=False):
        st.markdown("""
        🔹 **Comparez différentes stratégies thérapeutiques**  
        🔹 **Obtenez des recommandations basées sur le modèle**  
        🔹 **Planifiez un suivi médical automatisé**  
        """)
    
    # 📄 **Téléchargement du rapport**
    if st.button("📥 Télécharger le rapport médical"):
        st.download_button(
            label="📄 Télécharger le rapport",
            data="Résumé de la prédiction en format PDF ou texte...",
            file_name="rapport_prediction.txt",
            mime="text/plain"
        )

    st.markdown("---")

    # 📌 **Enregistrement du patient**
    if st.button("💾 Enregistrer le patient"):
        save_new_patient(input_df.iloc[0].to_dict())
        st.success("✅ Patient enregistré avec succès !")

