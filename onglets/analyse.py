import streamlit as st
import numpy as np
import plotly.express as px
from lifelines import KaplanMeierFitter
from utils import load_data

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
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
        }
        
        .analysis-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.05);
            border: 1px solid rgba(46, 119, 208, 0.1);
        }
        
        .metric-card {
            background: #f8faff;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
        }
        
        .stPlotlyChart {
            border-radius: 12px;
            overflow: hidden;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='header-card'><h1 style='margin:0;'>📈 Analyse Médicale Avancée</h1></div>", unsafe_allow_html=True)
    
    df = load_data()
    if df.empty:
        return

    # Section d'aperçu des données
    with st.expander("🔍 Exploration des Données Brutes", expanded=False):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.dataframe(df.head(5).style.highlight_max(color='#2e77d030')
        with col2:
            st.metric("Patients", df.shape[0])
            st.metric("Variables", df.shape[1])
    
    # Section des indicateurs clés
    st.markdown("<div class='analysis-card'>", unsafe_allow_html=True)
    st.subheader("🎯 Indicateurs Clés de Population")
    cols = st.columns(3)
    with cols[0]:
        st.metric("Âge Médian", f"{np.median(df['AGE'])} ans", help="Âge médian de la cohorte")
    with cols[1]:
        dece_rate = df['statut'].mean() * 100
        st.metric("Taux de Décès", f"{dece_rate:.1f}%", delta_color="inverse")
    with cols[2]:
        median_survival = df['time'].median()
        st.metric("Survie Médiane", f"{median_survival} mois", help="Temps médian de suivi")
    st.markdown("</div>", unsafe_allow_html=True)

    # Analyse de survie
    st.markdown("<div class='analysis-card'>", unsafe_allow_html=True)
    st.subheader("📉 Analyse de Survie Kaplan-Meier")
    
    kmf = KaplanMeierFitter()
    kmf.fit(df['time'], event_observed=df['statut'])
    
    fig = px.line(
        x=kmf.timeline,
        y=kmf.survival_function_['KM_estimate'],
        labels={'x': 'Temps (mois)', 'y': 'Probabilité de Survie'},
        color_discrete_sequence=['#2e77d0']
    )
    fig.update_layout(
        hovermode="x unified",
        title="Fonction de Survie Globale",
        xaxis_range=[0, df['time'].max()]
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Analyse comparative
    st.markdown("<div class='analysis-card'>", unsafe_allow_html=True)
    st.subheader("🔬 Analyse Comparative des Variables")
    
    col1, col2 = st.columns(2)
    with col1:
        selected_var = st.selectbox("Sélectionner une Variable", df.columns.drop(['statut', 'time']))
        
        if df[selected_var].nunique() < 5:
            fig = px.pie(df, names=selected_var, title=f"Répartition {selected_var}", hole=0.4)
        else:
            fig = px.histogram(df, x=selected_var, nbins=20, color_discrete_sequence=['#2e77d0'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📌 Statistiques Descriptives")
        st.dataframe(df[selected_var].describe().T.style.format("{:.2f}"))
    st.markdown("</div>", unsafe_allow_html=True)

    # Matrice de corrélation améliorée
    st.markdown("<div class='analysis-card'>", unsafe_allow_html=True)
    st.subheader("🌐 Matrice d'Association des Variables")
    
    numeric_df = df.select_dtypes(include=np.number)
    corr_matrix = numeric_df.corr()
    
    fig = px.imshow(
        corr_matrix,
        color_continuous_scale='RdBu',
        zmin=-1,
        zmax=1,
        labels=dict(color="Corrélation")
    )
    fig.update_xaxes(side="top")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Détection des valeurs aberrantes
    st.markdown("<div class='analysis-card'>", unsafe_allow_html=True)
    st.subheader("🚨 Détection des Valeurs Aberrantes")
    
    Q1 = numeric_df.quantile(0.25)
    Q3 = numeric_df.quantile(0.75)
    IQR = Q3 - Q1
    
    outliers = ((numeric_df < (Q1 - 1.5 * IQR)) | ((numeric_df > (Q3 + 1.5 * IQR)))
    outlier_counts = outliers.sum().sort_values(ascending=False)
    
    fig = px.bar(
        outlier_counts,
        color=outlier_counts,
        color_continuous_scale='reds',
        labels={'value': "Nombre d'Outliers"}
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    analyse_descriptive()
