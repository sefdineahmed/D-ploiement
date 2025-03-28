import streamlit as st
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
from utils import load_data
import matplotlib.pyplot as plt

def analyse_descriptive():
    # Configuration du style CSS personnalisé
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .header-card {
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
        }
        
        .metric-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            transition: transform 0.3s;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
        }
        
        .stPlotlyChart {
            border-radius: 15px;
            overflow: hidden;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='header-card'><h1 style='margin:0;'>📈 Exploration des Données Médicales</h1></div>", unsafe_allow_html=True)
    
    df = load_data()
    if df.empty:
        return

    # Section d'aperçu des données
    with st.expander("🔎 Aperçu Structuré des Données", expanded=True):
        cols = st.columns([3, 1, 1])
        with cols[0]:
            st.dataframe(df.head(5).style.highlight_null(color='#ffcccc'))
        with cols[1]:
            st.metric("Patients", df.shape[0])
        with cols[2]:
            st.metric("Variables", df.shape[1])
    
    st.markdown("---")
    
    # Section des statistiques d'âge
    st.markdown("### 📅 Analyse Démographique")
    age_data = df['AGE']
    age_stats = {
        "min": np.min(age_data),
        "med": np.median(age_data),
        "max": np.max(age_data),
        "mean": np.mean(age_data)
    }
    
    # Affichage sous forme de cartes métriques
    cols = st.columns(4)
    stats_config = {
        "min": {"label": "Minimum", "icon": "⬇️"},
        "med": {"label": "Médiane", "icon": "📊"},
        "max": {"label": "Maximum", "icon": "⬆️"},
        "mean": {"label": "Moyenne", "icon": "⚖️"}
    }
    
    for (key, stat), col in zip(age_stats.items(), cols):
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>{stats_config[key]['icon']}</div>
                <h3 style='color: var(--primary); margin: 0;'>{stat:.1f} ans</h3>
                <p style='color: #666; margin: 0;'>{stats_config[key]['label']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section d'analyse visuelle
    st.markdown("### 📊 Exploration Visuelle")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        with st.container():
            st.markdown("#### 🔍 Sélection des Variables")
            selected_var = st.selectbox("Variable à analyser", df.columns)
            plot_type = st.radio("Type de visualisation", 
                               ["Histogramme", "Box Plot", "Violin Plot"])
    
    with col2:
        st.markdown(f"#### 📌 Distribution de {selected_var}")
        if plot_type == "Histogramme":
            fig = px.histogram(df, x=selected_var, 
                              color_discrete_sequence=['#2e77d0'],
                              nbins=20)
        elif plot_type == "Box Plot":
            fig = px.box(df, y=selected_var, color_discrete_sequence=['#2e77d0'])
        else:
            fig = px.violin(df, y=selected_var, box=True, 
                           color_discrete_sequence=['#2e77d0'])
        
        fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Section d'analyse de survie
    st.markdown("### ⏳ Analyse de Survie Kaplan-Meier")
    kmf = KaplanMeierFitter()
    kmf.fit(df["Tempsdesuivi (Mois)"], df["Deces"])
    
    fig, ax = plt.subplots()
    kmf.plot_survival_function(ax=ax, ci_show=st.checkbox("Afficher l'intervalle de confiance"))
    ax.set_title('Courbe de Survie Globale')
    ax.set_xlabel('Mois de suivi')
    ax.set_ylabel('Probabilité de survie')
    st.pyplot(fig)
    
    st.markdown("---")
    
    # Section de corrélation interactive
    st.markdown("### 🔗 Matrice de Corrélation Interactive")
    numeric_df = df.select_dtypes(include=["number"])
    corr_matrix = numeric_df.corr()
    
    fig = px.imshow(corr_matrix,
                   color_continuous_scale='RdBu_r',
                   labels=dict(color="Corrélation"),
                   height=600)
    
    fig.update_xaxes(side="top")
    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    analyse_descriptive()
