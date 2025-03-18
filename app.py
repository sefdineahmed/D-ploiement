import os
import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import plotly.express as px
from PIL import Image
from lifelines import KaplanMeierFitter

# ----------------------------------------------------------
# Patch pour les incompatibilités de versions
# ----------------------------------------------------------
# Patch pour trapz (SciPy)
import scipy.integrate as integrate
try:
    from scipy.integrate import trapz
except ImportError:
    from numpy import trapz as np_trapz
    integrate.trapz = np_trapz

# Patch pour validate_data (scikit-learn)
try:
    from sklearn.utils.validation import validate_data
except ImportError:
    def validate_data(*args, **kwargs):
        return

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

# Configuration des modèles (ajout du modèle DeepSurv)
MODELS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib",
    "DeepSurv": "models/deepsurv.keras",
    "GBST": "models/gbst.joblib"
}

# ----------------------------------------------------------
# Configuration des variables
# ----------------------------------------------------------
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
# Fonction personnalisée pour DeepSurv
# ----------------------------------------------------------
@tf.keras.utils.register_keras_serializable()
def cox_loss(y_true, y_pred):
    """
    Implémente la fonction de perte Cox.
    """
    return tf.reduce_mean(tf.square(y_true - y_pred))

# ----------------------------------------------------------
# Fonctions Utilitaires
# ----------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_data():
    """Charge les données depuis le fichier Excel."""
    if os.path.exists(DATA_PATH):
        return pd.read_excel(DATA_PATH)
    else:
        st.error(f"❌ Fichier introuvable : {DATA_PATH}")
        return pd.DataFrame()

@st.cache_resource(show_spinner=False)
def load_model(model_path):
    """Charge un modèle en gérant les erreurs et en passant les custom_objects si nécessaire."""
    if not os.path.exists(model_path):
        st.error(f"❌ Modèle introuvable : {model_path}")
        return None
    try:
        if model_path.endswith(".keras"):
            return tf.keras.models.load_model(model_path, custom_objects={'cox_loss': cox_loss})
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {e}")
        return None

def encode_features(inputs):
    """
    Encode les variables en format numérique.
    Pour les variables catégorielles : "Oui" devient 1, "Non" devient 0.
    Pour les variables numériques, on conserve la valeur.
    """
    encoded = {}
    for key, value in inputs.items():
        if isinstance(value, (int, float)):
            encoded[key] = [value]
        else:
            encoded[key] = [1 if value == "OUI" else 0]
    return pd.DataFrame(encoded)

# ----------------------------------------------------------
# Définition des Pages
# ----------------------------------------------------------
def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    if df.empty:
        return

    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(10))
        st.write(f"Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Distribution des variables")
        selected_var = st.selectbox("Choisir une variable", df.columns)
        fig = px.histogram(df, x=selected_var, color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig, use_container_width=True)
        
        # Histogramme de la distribution du traitement
        if "Traitement" in df.columns:
            st.subheader("📊 Distribution du Traitement")
            fig2 = px.histogram(df, x="Traitement", color_discrete_sequence=['#ff7f0e'])
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.warning("La colonne 'Traitement' n'est pas disponible dans les données.")
    
    with col2:
        st.subheader("🌡 Matrice de corrélation")
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r', labels={"color": "Corrélation"})
        st.plotly_chart(fig, use_container_width=True)
        
        # Courbe de survie Kaplan-Meier
        if "Tempsdesuivi (Mois)" in df.columns and "Deces" in df.columns:
            st.subheader("📉 Courbe de survie Kaplan-Meier")
            
            # Nettoyage des données (suppression des NaN et valeurs infinies)
            df_clean = df.dropna(subset=["Tempsdesuivi (Mois)", "Deces"])
            df_clean = df_clean[(df_clean["Tempsdesuivi (Mois)"] > 0) & (df_clean["Tempsdesuivi (Mois)"] < 120)]
            
            kmf = KaplanMeierFitter()
            kmf.fit(durations=df_clean["Tempsdesuivi (Mois)"], event_observed=df_clean["Deces"])
            km_data = kmf.survival_function_.reset_index()
            fig_km = px.line(km_data, x="index", y=km_data.columns[1],
                             labels={"index": "Temps", km_data.columns[1]: "Survie"},
                             title="Courbe de survie Kaplan-Meier")
            st.plotly_chart(fig_km, use_container_width=True)
        else:
            st.warning("Les colonnes 'Tempsdesuivi (Mois)' et 'Deces' sont manquantes ou mal formatées.")

# ----------------------------------------------------------
# Navigation Principale (Onglets en haut)
# ----------------------------------------------------------
PAGES = {
    "🏠 Accueil": accueil,
    "📊 Analyse": analyse_descriptive,
    "🤖 Prédiction": modelisation,
    "📚 À Propos": a_propos,
    "📩 Contact": contact
}

def main():
    tabs = st.tabs(list(PAGES.keys()))
    for tab, (page_name, page_func) in zip(tabs, PAGES.items()):
        with tab:
            page_func()

if __name__ == "__main__":
    main()
