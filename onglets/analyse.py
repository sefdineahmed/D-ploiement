import pandas as pd

import numpy as np
import streamlit as st
import plotly.express as px
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from utils import load_data
import matplotlib.pyplot as plt
def analyse_descriptive():
    st.title("📊 Analyse Médico-Statistique")
    df = load_data()
    
    # Nettoyage avancé des données avec gestion d'erreur
    try:
        # Conversion sécurisée du temps de suivi
        if 'Tempsdesuivi (Mois)' in df.columns:
            # Étape 1: Nettoyage des caractères spéciaux
            df['Tempsdesuivi (Mois)'] = (
                df['Tempsdesuivi (Mois)']
                .astype(str)
                .str.replace('[^\d,.]', '', regex=True)  # Supprime tous les caractères non numériques
                .str.replace(',', '.')  # Convertit les virgules décimales
                .str.strip()  # Enlève les espaces
            )
            
            # Étape 2: Conversion numérique avec gestion des erreurs
            df['Tempsdesuivi (Mois)'] = pd.to_numeric(
                df['Tempsdesuivi (Mois)'], 
                errors='coerce',
                downcast='float'
            )
            
            # Vérification des valeurs manquantes après conversion
            if df['Tempsdesuivi (Mois)'].isnull().sum() > 0:
                st.warning(f"""
                **Alerte de données :** 
                {df['Tempsdesuivi (Mois)'].isnull().sum()} valeurs invalides détectées dans la colonne 'Temps de suivi'.
                Les valeurs problématiques ont été remplacées par la médiane.
                """)
                
                # Remplacement par la médiane calculée de manière sécurisée
                try:
                    median_value = df['Tempsdesuivi (Mois)'].median(skipna=True)
                    df['Tempsdesuivi (Mois)'].fillna(median_value, inplace=True)
                except:
                    st.error("Impossible de calculer la médiane - Vérifiez l'intégrité des données")
                    return
                
        else:
            st.error("Colonne 'Tempsdesuivi (Mois)' introuvable dans le dataset")
            return

        # Validation de la colonne 'Deces'
        if 'Deces' in df.columns:
            df['Deces'] = df['Deces'].astype(bool)
        else:
            st.error("Colonne 'Deces' introuvable dans le dataset")
            return

    except Exception as e:
        st.error(f"""
        **Erreur critique de prétraitement :** 
        {str(e)}
        """)
        st.stop()
    
    # Style CSS professionnel
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .data-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.05);
            border: 1px solid rgba(46, 119, 208, 0.1);
        }
        
        .metric-box {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .metric-box:hover {
            transform: translateY(-5px);
        }
    </style>
    """, unsafe_allow_html=True)

    # Nettoyage des données
    try:
        df['Tempsdesuivi (Mois)'] = df['Tempsdesuivi (Mois)'].astype(str).str.replace(',', '.').str.strip()
        df['Tempsdesuivi (Mois)'] = pd.to_numeric(df['Tempsdesuivi (Mois)'], errors='coerce')
        df['Deces'] = df['Deces'].astype(bool)
        
        if df['Tempsdesuivi (Mois)'].isnull().any():
            st.warning("Certaines valeurs de temps de suivi sont invalides et ont été remplacées par la médiane.")
            median_value = df['Tempsdesuivi (Mois)'].median()
            df['Tempsdesuivi (Mois)'] = df['Tempsdesuivi (Mois)'].fillna(median_value)
            
    except Exception as e:
        st.error(f"Erreur de prétraitement des données : {str(e)}")
        return

    with st.container():
        # Section d'aperçu des données
        with st.expander("🔍 Exploration des Données Brutes", expanded=True):
            st.markdown("<div class='data-card'>", unsafe_allow_html=True)
            cols = st.columns([1, 4])
            with cols[0]:
                st.metric("Patients", df.shape[0])
                st.metric("Variables", df.shape[1])
            with cols[1]:
                st.dataframe(df.head(5).style.highlight_null(color='#ffcccc')
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Analyse de survie
        st.header("📈 Analyse de Survie Kaplan-Meier")
        cols = st.columns([2, 1])
        
        with cols[0]:
            st.markdown("<div class='data-card'>", unsafe_allow_html=True)
            kmf = KaplanMeierFitter()
            kmf.fit(df["Tempsdesuivi (Mois)"], df["Deces"])
            
            fig = px.line(
                kmf.survival_function_.reset_index(),
                x='timeline',
                y='KM_estimate',
                labels={'timeline': 'Mois de suivi', 'KM_estimate': 'Probabilité de survie'},
                color_discrete_sequence=['#2e77d0']
            )
            fig.add_hline(y=0.5, line_dash="dot", annotation_text="Survie médiane")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown("<div class='data-card'>", unsafe_allow_html=True)
            st.subheader("Indicateurs Clés")
            st.metric("Survie Médiane", f"{kmf.median_survival_time_:.1f} mois")
            st.metric("Taux de Censure", f"{1 - df['Deces'].mean():.1%}")
            st.metric("Suivi Moyen", f"{df['Tempsdesuivi (Mois)'].mean():.1f} mois")
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Analyse multivariée
        st.header("🧮 Analyse Multidimensionnelle")
        cols = st.columns(2)
        
        with cols[0]:
            st.markdown("<div class='data-card'>", unsafe_allow_html=True)
            st.subheader("Distribution des Variables")
            selected_var = st.selectbox("Sélectionnez une variable", df.columns)
            
            if df[selected_var].dtype == 'object':
                fig = px.pie(df, names=selected_var, hole=0.3)
            else:
                fig = px.histogram(df, x=selected_var, nbins=20, 
                                 color_discrete_sequence=['#2e77d0'])
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown("<div class='data-card'>", unsafe_allow_html=True)
            st.subheader("Matrice de Corrélation")
            numeric_df = df.select_dtypes(include=np.number)
            corr_matrix = numeric_df.corr()
            
            fig = px.imshow(
                corr_matrix,
                color_continuous_scale='RdBu',
                zmin=-1,
                zmax=1,
                labels=dict(color="Corrélation")
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Analyse comparative
        st.header("📌 Analyse Stratifiée")
        group_var = st.selectbox("Choisir une variable de stratification", 
                               df.select_dtypes(exclude='number').columns)
        
        if group_var:
            st.markdown("<div class='data-card'>", unsafe_allow_html=True)
            fig = px.area(
                pd.pivot_table(
                    df,
                    index='Tempsdesuivi (Mois)',
                    columns=group_var,
                    values='Deces',
                    aggfunc='mean'
                ).cumsum(),
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    analyse_descriptive()
