import os
import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import plotly.express as px
from PIL import Image
from lifelines import KaplanMeierFitter

# ----------------------------------------------------------
# Configuration de l'application
# ----------------------------------------------------------
st.set_page_config(
    page_title="OncoSuite - Cancer Gastrique",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chemins vers les ressources
DATA_PATH = "data/GastricCancerData.xlsx"
LOGO_PATH = "assets/header.jpg"
TEAM_IMG_PATH = "assets/team.jpg"

MODELS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib",
    "DeepSurv": "models/deepsurv.keras",
    "GBST": "models/gbst.joblib"
}

FEATURE_CONFIG = {
    "Age": "Âge",
    "Cardiopathie": "Cardiopathie",
    "Ulceregastrique": "Ulcère gastrique",
    "Douleurepigastrique": "Douleur épigastrique",
    "Ulcero-bourgeonnant": "Lésion ulcéro-bourgeonnante",
    "Denutrution": "Dénutrition",
    "Tabac": "Tabagisme actif",
    "Mucineux": "Type mucineux",
    "Infiltrant": "Type infiltrant",
    "Stenosant": "Type sténosant",
    "Metastases": "Métastases",
    "Adenopathie": "Adénopathie"
}

# ----------------------------------------------------------
# Fonctions Utilitaires
# ----------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_data():
    """Charge et prétraite les données"""
    if not os.path.exists(DATA_PATH):
        st.error(f"❌ Fichier introuvable : {DATA_PATH}")
        return pd.DataFrame()
    
    df = pd.read_excel(DATA_PATH)
    
    # Conversion des types de données critiques
    if 'Tempsdesuivi (Mois)' in df.columns:
        df['Tempsdesuivi (Mois)'] = pd.to_numeric(df['Tempsdesuivi (Mois)'], errors='coerce')
    
    if 'Deces' in df.columns:
        df['Deces'] = df['Deces'].astype(int)
    
    return df.dropna(subset=['Tempsdesuivi (Mois)', 'Deces'], how='any')

@st.cache_resource(show_spinner=False)
def load_model(model_path):
    """Charge un modèle avec gestion d'erreur"""
    if not os.path.exists(model_path):
        st.error(f"❌ Modèle introuvable : {model_path}")
        return None
    
    try:
        if model_path.endswith(".keras"):
            return tf.keras.models.load_model(model_path)
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Erreur de chargement : {e}")
        return None

# ----------------------------------------------------------
# Pages de l'Application
# ----------------------------------------------------------
def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    
    if df.empty:
        return

    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(10))
        st.write(f"Données disponibles : {len(df)} patients")
    
    # Vérification des colonnes nécessaires
    km_columns = ['Tempsdesuivi (Mois)', 'Deces']
    if all(col in df.columns for col in km_columns):
        st.markdown("---")
        st.subheader("📉 Courbe de Survie Kaplan-Meier")
        
        kmf = KaplanMeierFitter()
        try:
            kmf.fit(
                durations=df['Tempsdesuivi (Mois)'], 
                event_observed=df['Deces']
            )
            
            fig = px.line(
                kmf.survival_function_.reset_index(),
                x='timeline',
                y='KM_estimate',
                labels={'timeline': 'Mois', 'KM_estimate': 'Probabilité de Survie'},
                title="Courbe de Survie Global"
            )
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Erreur dans le calcul Kaplan-Meier : {str(e)}")
    else:
        st.warning("Colonnes manquantes pour l'analyse Kaplan-Meier")

# Le reste du code (autres fonctions) reste inchangé...

def main():
    tabs = st.tabs(list(PAGES.keys()))
    for tab, (page_name, page_func) in zip(tabs, PAGES.items()):
        with tab:
            page_func()

if __name__ == "__main__":
    main()
