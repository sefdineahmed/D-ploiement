import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
from lifelines.utils import concordance_index

# Charger les modèles
cox_model = joblib.load("models/coxph.joblib")
rsf_model = joblib.load("models/rsf.joblib")
gbst_model = joblib.load("models/gbst.joblib")
deep_model = tf.keras.models.load_model("models/deepsurv.keras")

# Variables de l'étude
features = ['Cardiopathie', 'Ulceregastrique', 'Douleurepigastrique',
    'Ulcero-bourgeonnant', 'Denutrution', 'Tabac',
    'Mucineux', 'Infiltrant', 'Stenosant', 'Metastases',
    'Adenopathie']

def user_input_features():
    """Formulaire de saisie des informations du patient."""
    st.sidebar.header("Entrer les données du patient")
    input_data = {}
    for feature in features:
        input_data[feature] = st.sidebar.selectbox(feature, [0, 1])
    return pd.DataFrame([input_data])

def predict_survival(model, data):
    """Faire des prédictions avec un modèle donné."""
    if model == 'Cox':
        return cox_model.predict_median(data)
    elif model == 'RSF':
        return rsf_model.predict(data)
    elif model == 'GBST':
        return gbst_model.predict(data)
    elif model == 'DeepSurv':
        return deep_model.predict(data).flatten()
    return None

def main():
    st.set_page_config(layout="wide")
    st.title("Prédiction du Temps de Survie des Patients atteints de Cancer de l'Estomac")
    st.markdown("""Cette application permet d'estimer le temps de survie des patients atteints de cancer de l'estomac
    en utilisant plusieurs modèles de Machine Learning et Deep Learning.""")
    
    input_df = user_input_features()
    st.sidebar.write("### Données saisies")
    st.sidebar.write(input_df)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Cox PH", "Random Survival Forest", "GBST", "DeepSurv"])
    
    with tab1:
        st.header("Modèle Cox Proportionnel des Risques")
        pred_cox = predict_survival('Cox', input_df)
        st.write(f"Temps de survie estimé : {pred_cox} mois")
    
    with tab2:
        st.header("Modèle Random Survival Forest")
        pred_rsf = predict_survival('RSF', input_df)
        st.write(f"Temps de survie estimé : {pred_rsf} mois")
    
    with tab3:
        st.header("Modèle Gradient Boosting Survival Trees")
        pred_gbst = predict_survival('GBST', input_df)
        st.write(f"Temps de survie estimé : {pred_gbst} mois")
   
    with tab4:
        st.header("Modèle DeepSurv")
        pred_deep = predict_survival('DeepSurv', input_df)
        st.write(f"Temps de survie estimé : {pred_deep} mois")
    
    st.markdown("---")
    st.write("L'application est flexible et permet d'ajouter de nouvelles variables à l'avenir sans modification majeure.")

if __name__ == "__main__":
    main()
