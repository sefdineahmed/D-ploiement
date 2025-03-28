import streamlit as st
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from utils import load_data
import matplotlib.pyplot as plt

# Configuration du style CSS
st.markdown("""
<style>
    :root {
        --primary: #2e77d0;
        --secondary: #1d5ba6;
        --accent: #22d3ee;
    }
    
    .section-title {
        color: var(--primary);
        border-bottom: 3px solid var(--primary);
        padding-bottom: 0.5rem;
        margin: 2rem 0 !important;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    .plot-container {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
    }
    
    .stSelectbox>div>div>select {
        border: 2px solid var(--primary) !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)


def analyse_descriptive():
    st.title("📈 Analyse de Survie Oncologique")
    df = load_data()
    if df.empty:
        return

    # Conversion des variables catégorielles
    df['Deces'] = df['Deces'].map({'OUI': 1, 'NON': 0})  # Conversion en binaire
    df['Tempsdesuivi (Mois)'] = pd.to_numeric(df['Tempsdesuivi (Mois)'], errors='coerce')

    # Section d'en-tête avec statistiques clés
    with st.container():
        st.markdown("<div class='plot-container'>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Patients", f"{len(df):,}")
        with col2:
            event_rate = df['Deces'].mean() * 100  # Fonctionne maintenant
            st.metric("Taux de Décès", f"{event_rate:.1f}%")
        with col3:
            median_fu = df['Tempsdesuivi (Mois)'].median()
            st.metric("Suivi Médian", f"{median_fu:.1f} mois")
        
        st.markdown("</div>", unsafe_allow_html=True)


    
    st.markdown("---")
    
    # Analyse de survie avec courbe de Kaplan-Meier
    with st.container():
        st.markdown("<div class='plot-container'>", unsafe_allow_html=True)
        st.markdown("### 📉 Courbe de Survie de Kaplan-Meier")
        
        kmf = KaplanMeierFitter()
        kmf.fit(df['Tempsdesuivi (Mois)'], df['Deces'])
        
        fig = px.line(
            x=kmf.timeline,
            y=kmf.survival_function_['KM_estimate'],
            labels={'x': 'Mois de suivi', 'y': 'Probabilité de survie'},
            color_discrete_sequence=['#2e77d0']
        )
        
        fig.update_layout(
            hovermode="x unified",
            yaxis_tickformat=".0%",
            xaxis_title="Temps de suivi (mois)",
            yaxis_title="Probabilité de survie"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Analyse comparative par sous-groupes
    with st.container():
        st.markdown("<div class='plot-container'>", unsafe_allow_html=True)
        st.markdown("### 🔄 Analyse Comparative par Variable")
        
        analysis_var = st.selectbox("Sélectionnez une variable catégorielle", 
                                  options=[col for col in df.columns if col not in ['Tempsdesuivi (Mois)', 'Deces']])
        
        if analysis_var:
            groups = df[analysis_var].unique()
            fig = px.ecdf(
                df,
                x="Tempsdesuivi (Mois)",
                color=analysis_var,
                ecdfnorm=None,
                ecdfmode="complementary",
                labels={'Tempsdesuivi (Mois)': 'Mois de suivi', 'ecdf': 'Probabilité de survie'}
            )
            
            fig.update_layout(
                yaxis_title="Probabilité de survie",
                yaxis_tickformat=".0%",
                legend_title=analysis_var
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Test du log-rank
            results = logrank_test(
                df['Tempsdesuivi (Mois)'][df[analysis_var] == groups[0]],
                df['Tempsdesuivi (Mois)'][df[analysis_var] == groups[1]],
                df['Deces'][df[analysis_var] == groups[0]],
                df['Deces'][df[analysis_var] == groups[1]]
            )
            st.markdown(f"""
                **Résultat du test du log-rank**  
                p-value = {results.p_value:.4f}  
                Statistique de test = {results.test_statistic:.2f}
            """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section d'analyse descriptive
    with st.container():
        st.markdown("<div class='plot-container'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Distribution des Variables")
            dist_var = st.selectbox("Choisir une variable", df.columns)
            fig = px.histogram(df, x=dist_var, color_discrete_sequence=['#2e77d0'])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 🌡 Matrice de Corrélation")
            numeric_df = df.select_dtypes(include=["number"])
            corr_matrix = numeric_df.corr()
            fig = px.imshow(
                corr_matrix,
                color_continuous_scale='RdBu_r',
                labels=dict(color="Corrélation"),
                zmin=-1,
                zmax=1
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    analyse_descriptive()
