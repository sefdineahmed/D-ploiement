def analyse_descriptive():
    st.title("🔍 Analyse Médicale Avancée")
    df = load_data()
    if df.empty:
        return

    # Style CSS personnalisé
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .metric-card {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border-left: 4px solid var(--primary);
        }
        
        .section-title {
            color: var(--primary);
            border-bottom: 3px solid var(--accent);
            padding-bottom: 0.5rem;
            margin: 2rem 0 !important;
        }
        
        .plot-container {
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 24px rgba(0,0,0,0.05);
        }
    </style>
    """, unsafe_allow_html=True)

    # Section 1: Aperçu des données
    with st.expander("📁 Aperçu des Données Brutes", expanded=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.dataframe(df.head(5).style.format(precision=2), height=200)
        with col2:
            st.metric("Nombre de Patients", df.shape[0])
            st.metric("Variables Analysées", df.shape[1])
            st.download_button("📥 Exporter les Données", df.to_csv(), "donnees_medicales.csv")
    
    st.markdown("---")

    # Section 2: Analyse de Survie
    st.markdown("<h2 class='section-title'>📈 Analyse de Survie Kaplan-Meier</h2>", unsafe_allow_html=True)
    
    kmf = KaplanMeierFitter()
    kmf.fit(df["Tempsdesuivi (Mois)"], event_observed=df["Deces"])
    
    with st.container():
        fig = px.line(
            kmf.survival_function_,
            x=kmf.survival_function_.index,
            y='KM_estimate',
            labels={'x': 'Mois de suivi', 'y': 'Probabilité de survie'},
            color_discrete_sequence=['#2e77d0']
        )
        fig.update_layout(
            hovermode="x unified",
            title="Courbe de Survie Globale",
            xaxis_title="Temps (mois)",
            yaxis_title="Probabilité de Survie",
            plot_bgcolor='rgba(240, 244, 254, 0.3)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

    # Section 3: Statistiques Descriptives
    st.markdown("<h2 class='section-title'>📋 Statistiques Démographiques</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Âge Minimum", f"{np.min(df['AGE']} ans")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Âge Médian", f"{np.median(df['AGE'])} ans")
        st.markdown("</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Âge Maximum", f"{np.max(df['AGE'])} ans")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # Section 4: Analyse des Variables
    st.markdown("<h2 class='section-title'>📊 Exploration des Variables</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Distribution", "Corrélations", "Analyse Catégorielle"])
    
    with tab1:
        selected_var = st.selectbox("Choisir une variable numérique", df.select_dtypes(include=np.number).columns)
        fig = px.histogram(
            df, 
            x=selected_var, 
            nbins=30, 
            color_discrete_sequence=['#2e77d0'],
            marginal="box"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        corr_matrix = df.corr(numeric_only=True)
        fig = px.imshow(
            corr_matrix,
            color_continuous_scale='RdBu',
            zmin=-1,
            zmax=1,
            labels=dict(color="Corrélation")
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        categorical_vars = df.select_dtypes(exclude=np.number).columns.tolist()
        if categorical_vars:
            selected_cat = st.selectbox("Choisir une variable catégorielle", categorical_vars)
            counts = df[selected_cat].value_counts().reset_index()
            fig = px.bar(
                counts, 
                x=selected_cat, 
                y='count',
                color='count',
                color_continuous_scale=['#2e77d0', '#1d5ba6']
            )
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

if __name__ == "__main__":
    analyse_descriptive()
