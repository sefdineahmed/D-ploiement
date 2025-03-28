def analyse_descriptive():
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .header-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #f8faff, #ffffff);
            border-left: 4px solid var(--primary);
            padding: 1.5rem;
            margin: 1rem 0;
            border-radius: 12px;
            transition: transform 0.3s;
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
        }
        
        .analysis-section {
            background: white;
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.05);
            margin: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("🔍 Analyse Descriptive Avancée")
    df = load_data()
    if df.empty:
        return

    # Section Aperçu des données
    with st.expander("📂 Exploration des Données Brutes", expanded=True):
        st.markdown("<div class='header-card'>", unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.dataframe(df.head(5).style.highlight_max(color='#e6f3ff'), use_container_width=True)
        with col2:
            st.metric("Nombre de Patients", df.shape[0])
            st.metric("Variables Analysées", df.shape[1])
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section Analyse de Survie
    with st.container():
        st.markdown("<div class='analysis-section'>", unsafe_allow_html=True)
        st.header("📈 Analyse de Survie Kaplan-Meier")
        
        # Création du modèle Kaplan-Meier
        kmf = KaplanMeierFitter()
        kmf.fit(df[time], df[event])
        
        # Courbe de survie interactive
        fig = px.line(
            kmf.survival_function_.reset_index(),
            x=time,
            y='KM_estimate',
            labels={time: 'Temps (mois)', 'KM_estimate': 'Probabilité de Survie'},
            color_discrete_sequence=['#2e77d0']
        )
        fig.update_layout(
            hovermode="x unified",
            title="Courbe de Survie Globale"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Statistiques de survie
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Médiane de Survie", f"{kmf.median_survival_time_:.1f} mois")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Taux de Survie à 12 mois", f"{kmf.predict(12)*100:.1f}%")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col3:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Taux de Survie à 24 mois", f"{kmf.predict(24)*100:.1f}%")
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Analyse Stratifiée par Âge
    with st.container():
        st.markdown("<div class='analysis-section'>", unsafe_allow_html=True)
        st.header("🧮 Analyse Stratifiée par Âge")
        
        # Création des groupes d'âge
        df['Groupe d\'âge'] = pd.cut(df['AGE'], 
                                   bins=[0, 50, 65, 120],
                                   labels=['<50 ans', '50-65 ans', '>65 ans'])
        
        # Courbes de survie par groupe d'âge
        fig = px.line(
            title="Courbes de Survie par Tranche d'Âge"
        )
        
        for name, grouped_df in df.groupby('Groupe d\'âge'):
            kmf.fit(grouped_df[time], grouped_df[event])
            fig.add_scatter(
                x=kmf.survival_function_.index,
                y=kmf.survival_function_['KM_estimate'],
                mode='lines',
                name=str(name)
            )
        
        fig.update_layout(
            xaxis_title='Temps (mois)',
            yaxis_title='Probabilité de Survie',
            colorway=['#2e77d0', '#22d3ee', '#1d5ba6']
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Test du log-rank
        results = logrank_test(
            df[time][df['Groupe d\'âge'] == '<50 ans'],
            df[time][df['Groupe d\'âge'] == '>65 ans'],
            df[event][df['Groupe d\'âge'] == '<50 ans'],
            df[event][df['Groupe d\'âge'] == '>65 ans']
        )
        
        st.markdown(f"""
        <div class='metric-card'>
            <h4>Test du Log-Rank (Groupes extrêmes)</h4>
            <p>p-value : {results.p_value:.4f}</p>
            <p>{'Différence significative' if results.p_value < 0.05 else 'Pas de différence significative'}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Analyse Multivariée
    with st.container():
        st.markdown("<div class='analysis-section'>", unsafe_allow_html=True)
        st.header("📊 Analyse des Corrélations")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            selected_vars = st.multiselect(
                "Sélectionner les variables à analyser",
                options=df.select_dtypes(include=np.number).columns,
                default=['AGE', time]
            )
        
        with col2:
            corr_matrix = df[selected_vars].corr()
            fig = px.imshow(
                corr_matrix,
                color_continuous_scale='RdBu',
                zmin=-1,
                zmax=1,
                labels=dict(color="Corrélation")
            )
            fig.update_layout(
                title="Matrice de Corrélation Interactive",
                width=800
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
