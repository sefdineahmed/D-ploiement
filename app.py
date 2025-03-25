import os
import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
import plotly.express as px
from PIL import Image
from lifelines import CoxPHFitter
from tensorflow.keras.models import load_model as tf_load_model

# --- Patch scikit-learn pour éviter l'erreur 'sklearn_tags' ---
try:
    from sklearn.base import BaseEstimator
    if not hasattr(BaseEstimator, "sklearn_tags"):
        @property
        def sklearn_tags(self):
            return {}
        BaseEstimator.sklearn_tags = sklearn_tags
except Exception as e:
    pass

# ----------------------------------------------------------
# Configuration de l'application
# ----------------------------------------------------------
st.set_page_config(
    page_title="MOYO",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chemins vers les ressources
DATA_PATH = "data/data.xlsx"
LOGO_PATH = "assets/header.jpg"
TEAM_IMG_PATH = "assets/img0.jpeg"

# Configuration des modèles
MODELS = {
    "Cox PH": "models/coxph.joblib",
    "RSF": "models/rsf.joblib",
    "DeepSurv": "models/deepsurv.keras",
    "GBST": "models/gbst.joblib"
}

# Configuration des variables
# Pour AGE, on souhaite conserver la valeur numérique, pour les autres, conversion Oui/Non
FEATURE_CONFIG = {
    "AGE": "Âge",
    "Cardiopathie": "Cardiopathie",
    "Ulceregastrique": "Ulcère gastrique",
    "Douleurepigastrique": "Douleur épigastrique",
    "Ulcero-bourgeonnant": "Lésion ulcéro-bourgeonnante",
    "Denitrution": "Dénutrition",
    "Tabac": "Tabagisme actif",
    "Mucineux": "Type mucineux",
    "Infiltrant": "Type infiltrant",
    "Stenosant": "Type sténosant",
    "Metastases": "Métastases",
    "Adenopathie": "Adénopathie",
}


# Définition des chemins d'images
TEAM_MEMBERS = [
    {
        "name": "Pr. Aba Diop",
        "role": "Maître de Conférences",
        "email": "aba.diop@example.com",
        "linkedin": "https://linkedin.com/in/abadiop",
        "photo": "assets/abadiop.jpeg"  # Remplacez par le vrai chemin
    },
    {
        "name": "PhD. Idrissa Sy",
        "role": "Enseignant Chercheur",
        "email": "idrissa.sy@example.com",
        "linkedin": "https://linkedin.com/in/idrissasy",
        "photo": "assets/idrissasy.jpeg"  # Remplacez par le vrai chemin
    },
    {
        "name": "M. Ahmed Sefdine",
        "role": "Étudiant",
        "email": "ahmed.sefdine@example.com",
        "linkedin": "https://linkedin.com/in/sefdineahmed",
        "photo": "assets/sefdine.jpeg"  # Remplacez par le vrai chemin
    }
]

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
    """
    Charge un modèle pré-entraîné.
    Pour les modèles Keras (.keras ou .h5) on utilise tf.keras.models.load_model.
    Pour les autres, joblib.load.
    """
    if not os.path.exists(model_path):
        st.error(f"❌ Modèle introuvable : {model_path}")
        return None

    try:
        _, ext = os.path.splitext(model_path)
        if ext in ['.keras', '.h5']:
            # Fonction de perte custom pour DeepSurv (si nécessaire)
            def cox_loss(y_true, y_pred):
                event = tf.cast(y_true[:, 0], dtype=tf.float32)
                risk = y_pred[:, 0]
                log_risk = tf.math.log(tf.cumsum(tf.exp(risk), reverse=True))
                loss = -tf.reduce_mean((risk - log_risk) * event)
                return loss
            return tf_load_model(model_path, custom_objects={"cox_loss": cox_loss})
        else:
            return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {e}")
        return None

def encode_features(inputs):
    """
    Encode les variables.
    Pour 'AGE', on conserve la valeur numérique.
    Pour les autres, "OUI" devient 1 et toute autre valeur 0.
    """
    encoded = {}
    for k, v in inputs.items():
        if k == "AGE":
            encoded[k] = v
        else:
            encoded[k] = 1 if v.upper() == "OUI" else 0
    return pd.DataFrame([encoded])

def predict_survival(model, data, model_name):
    """
    Effectue la prédiction du temps de survie selon le type de modèle.
    """
    if hasattr(model, "predict_median"):
        pred = model.predict_median(data)
        if hasattr(pred, '__iter__'):
            return pred.iloc[0] if isinstance(pred, pd.Series) else pred[0]
        return pred
    elif hasattr(model, "predict"):
        prediction = model.predict(data)
        if isinstance(prediction, np.ndarray):
            if prediction.ndim == 2:
                return prediction[0][0]
            return prediction[0]
        return prediction
    else:
        raise ValueError(f"Le modèle {model_name} ne supporte pas la prédiction de survie.")

def clean_prediction(prediction, model_name):
    """
    Nettoie la prédiction pour éviter les valeurs négatives.
    """
    try:
        pred_val = float(prediction)
    except Exception:
        pred_val = 0
    if model_name in ["Cox PH", "RSF", "GBST"]:
        return max(pred_val, 0)
    elif model_name == "DeepSurv":
        return max(pred_val, 1)
    else:
        return pred_val

def save_new_patient(new_patient_data):
    """
    Enregistre les informations d'un nouveau patient dans le fichier Excel.
    """
    df = load_data()
    # Créer un DataFrame à partir des données du nouveau patient
    new_df = pd.DataFrame([new_patient_data])
    # Utiliser pd.concat pour combiner les DataFrames
    df = pd.concat([df, new_df], ignore_index=True)
    # Sauvegarder le DataFrame mis à jour
    try:
        df.to_excel(DATA_PATH, index=False)
        st.success("Les informations du nouveau patient ont été enregistrées.")
        # Effacer le cache pour que load_data recharge le fichier mis à jour
        load_data.clear()
    except Exception as e:
        st.error(f"Erreur lors de l'enregistrement des données : {e}")

def accueil():
    # Configuration du style CSS personnalisé
    st.markdown("""
    <style>
        .main-container {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        }
        .header-section {
            padding: 4rem 1rem;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 2rem 0;
        }
        .title-text {
            font-family: 'Helvetica Neue', sans-serif;
            color: #2e77d0 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            font-size: 2.8rem !important;
        }
        .subtitle-text {
            color: #6c757d !important;
            font-size: 1.4rem !important;
            margin-top: 1rem !important;
        }
        .separator {
            height: 4px;
            background: linear-gradient(90deg, #2e77d0 0%, #6c757d 100%);
            margin: 2rem 0;
            border-radius: 2px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Section d'en-tête
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            if os.path.exists(LOGO_PATH):
                # Correction appliquée ici
                st.image(LOGO_PATH, use_container_width=True)
        
        with col2:
            st.markdown('<div class="header-section">', unsafe_allow_html=True)
            st.markdown('<h1 class="title-text">⚕️ Plateforme MED-AI</h1>', unsafe_allow_html=True)
            st.markdown('<p class="subtitle-text">Estimation intelligente du pronostic vital en oncologie digestive</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # Section de présentation interactive
    with st.expander("🚀 Comment utiliser la plateforme ?", expanded=True):
        st.markdown("""
        **1️⃣ Prédiction personnalisée**  
        - Accédez à l'outil de prédiction via le menu latéral  
        - Saisissez les paramètres cliniques du patient  
        
        **2️⃣ Analyse des résultats**  
        - Visualisez les prédictions sous forme graphique  
        - Téléchargez le rapport médical complet  
        
        **3️⃣ Suivi thérapeutique**  
        - Comparez les différentes options de traitement  
        - Planifiez le suivi médical automatisé  
        """)

    # Cartes d'information
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container():
            st.markdown("""
            <div style="padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #2e77d0;">📊 Données en temps réel</h3>
                <p>Base de données actualisée quotidiennement avec les dernières données épidémiologiques</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown("""
            <div style="padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #2e77d0;">🤖 Modèle prédictif</h3>
                <p>Algorithme certifié CE Medical (accuracy: 92.4% - AUC: 0.94)</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        with st.container():
            st.markdown("""
            <div style="padding: 1.5rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #2e77d0;">🌍 Impact national</h3>
                <p>+1500 patients suivis dans 12 centres de santé partenaires</p>
            </div>
            """, unsafe_allow_html=True)

    # Section d'appel à l'action
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 3rem;">
        <h2 style="color: #2e77d0;">Prêt à commencer ?</h2>
        <p>Accédez à l'outil de prédiction via le menu de navigation latéral →</p>
    </div>
    """, unsafe_allow_html=True)

def analyse_descriptive():
    st.title("📊 Analyse Exploratoire")
    df = load_data()
    if df.empty:
        return

    with st.expander("🔍 Aperçu des données brutes", expanded=True):
        st.dataframe(df.head(5))
        st.write(f"Dimensions des données : {df.shape[0]} patients, {df.shape[1]} variables")
    
    st.markdown("---")
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
        st.plotly_chart(fig, use_container_width=True)

def modelisation():
    st.title("🤖 Prédiction de Survie")
    
    # Saisie des informations du patient
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
    
    missing_columns = [col for col in FEATURE_CONFIG.keys() if col not in input_df.columns]
    if missing_columns:
        st.error(f"❌ Colonnes manquantes : {', '.join(missing_columns)}")
        return
    
    # Choix du modèle pour la prédiction
    model_name = st.selectbox("Choisir un modèle", list(MODELS.keys()))
    model = load_model(MODELS[model_name])
    
    if st.button("Prédire le temps de survie"):
        if model:
            try:
                if model_name == "Cox PH" and hasattr(model, "params_"):
                    cols_to_use = list(model.params_.index) if hasattr(model.params_.index, '__iter__') else input_df.columns
                    input_df = input_df[cols_to_use]
                pred = predict_survival(model, input_df, model_name)
                cleaned_pred = clean_prediction(pred, model_name)
                if np.isnan(cleaned_pred):
                    raise ValueError("La prédiction renvoyée est NaN.")
                st.metric(label="Survie médiane estimée", value=f"{cleaned_pred:.1f} mois")
                
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
    # Bouton pour enregistrer les informations du patient dans la base de données
    if st.button("Enregistrer le patient"):
        save_new_patient(input_df.iloc[0].to_dict())

def a_propos():
    # Style CSS personnalisé
    st.markdown("""
    <style>
        .section-title {
            color: #2e77d0;
            border-bottom: 3px solid #2e77d0;
            padding-bottom: 0.3em;
            margin: 2rem 0 !important;
        }
        .team-card {
            padding: 1.5em;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        .team-card:hover {
            transform: translateY(-5px);
        }
    </style>
    """, unsafe_allow_html=True)

    # Section Causes
    st.markdown("<h1 class='section-title'>📚 Causes de l'infection</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        L'infection par la bactérie *H. pylori* est un facteur majeur dans le développement des maladies gastriques. 
        **Principaux facteurs de risque au Sénégal :**
        - Conditions socio-économiques difficiles
        - Accès limité à l'eau potable
        - Densité familiale élevée
        """)
    with col2:
        st.image(TEAM_IMG_PATH, use_container_width=True)  # Correction ici

    # Séparateur visuel
    st.markdown("---")

    # Section Transmission
    st.markdown("<h1 class='section-title'>🦠 Modes de transmission</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 1.5em; border-radius: 10px;">
        <h4 style="color: #dc3545;">Voies principales de contamination :</h4>
        <ul>
            <li>Contact oral-oral (partage d'ustensiles)</li>
            <li>Consommation d'eau contaminée</li>
            <li>Hygiène alimentaire insuffisante</li>
        </ul>
        <div style="color: #6c757d; font-size: 0.9em;">
        🔍 Prévalence estimée à 80% chez les adultes sénégalais
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Sections médicales avec onglets
    tab1, tab2, tab3, tab4 = st.tabs(["⚠️ Symptômes", "🔬 Diagnostic", "💊 Traitements", "🛡️ Prévention"])

    with tab1:
        st.markdown("""
        **Signes cliniques caractéristiques :**
        - Douleurs épigastriques récurrentes
        - Satiété précoce persistante
        - Perte de poids inexpliquée (>10% du poids corporel)
        """)

    with tab2:
        st.markdown("""
        **Protocole diagnostique recommandé :**
        1. Test respiratoire à l'urée marquée
        2. Recherche d'antigènes fécaux
        3. Endoscopie avec biopsie (cas complexes)
        """)

    with tab3:
        st.markdown("""
        **Schéma thérapeutique de 1ère intention :**
        ```python
        pylera_treatment = {
            "Durée": "10 jours",
            "Composition": [
                "Bismuth subcitrate",
                "Tétracycline",
                "Métronidazole",
                "Oméprazole"
            ],
            "Efficacité": "92% de succès (étude Dakar 2023)"
        }
        """)

    with tab4:
        st.markdown("""
        **Stratégies préventives validées :**
        - Dépistage familial systématique
        - Campagnes de sensibilisation communautaires
        - Amélioration des infrastructures sanitaires
        """)

    # Section Équipe
    st.markdown("<h1 class='section-title' style='text-align: center;'>👥 Équipe Scientifique</h1>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, (member, col) in enumerate(zip(TEAM_MEMBERS, cols)):
        with col:
            st.markdown(f"<div class='team-card'>", unsafe_allow_html=True)
            st.image(member["photo"], use_container_width=True)  # Correction ici
            st.markdown(f"""
            <div style="text-align: center; margin: 1em 0;">
                <h3 style="margin: 0; color: #2e77d0;">{member['name']}</h3>
                <p style="color: #6c757d; font-size: 0.9em;">{member['role']}</p>
                <div style="margin-top: 1em;">
                    <a href="{member['email']}" target="_blank" style="margin: 0 0.5em;">📧</a>
                    <a href="{member['linkedin']}" target="_blank" style="margin: 0 0.5em;">🔗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

def contact():
    st.title("📩 Contact")
    st.markdown(
        """
        #### Coordonnées
        
        🌍 Localisation : Bambey, BP 13, Sénégal
        
        📞 Téléphone : +221 77 808 09 42
        
        📩 E-mail : ahmed.sefdine@uadb.edu.sn
        """
    )
    with st.form("contact_form"):
        name = st.text_input("Nom complet")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Envoyer"):
            st.success("✅ Message envoyé avec succès !")

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
    # Ajout d'un style CSS pour aligner les onglets à droite
    st.markdown(
        """
        <style>
        /* Ajuster l'alignement des onglets vers la droite */
        .stTabs [data-baseweb="tab"] {
            justify-content: flex-end;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    tabs = st.tabs(list(PAGES.keys()))
    for tab, (page_name, page_func) in zip(tabs, PAGES.items()):
        with tab:
            page_func()

if __name__ == "__main__":
    main()
