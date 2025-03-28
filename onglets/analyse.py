def analyse_descriptive():
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
        
        .metric-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border-left: 4px solid var(--accent);
        }
        
        .analysis-card {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.05);
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # En-tête stylisé
    st.markdown("""
    <div class="header-card">
        <h1 style="margin:0; font-size:2.5rem">📈 Exploration des Données Médicales</h1>
        <p style="opacity:0.9; margin-top:0.5rem">Analyse descriptive avancée des données patients</p>
    </div>
    """, unsafe_allow_html=True)

    df = load_data()
    if df.empty:
        return

    # Section Aperçu des données avec option de téléchargement
    with st.expander("🗃️ Base de Données Brutes", expanded=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.dataframe(df.head(10).style.highlight_max(color='#e6f3ff'), use_container_width=True)
        with col2:
            st.download_button(
                label="📥 Exporter les données",
                data=df.to_csv(index=False).encode('utf-8'),
                file_name='donnees_medicales.csv',
                mime='text/csv'
            )
        st.markdown(f"<div style='text-align: center; color: #666; margin-top: 1rem;'>Dataset contenant {df.shape[0]} patients et {df.shape[1]} variables</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # Section Statistiques descriptives
    st.markdown("### 📋 Métriques Clés")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="metric-card">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="font-size: 2rem;">👴</div>
                <div>
                    <h3 style="margin:0; color: var(--primary);">Âge Moyen</h3>
                    <p style="font-size: 1.5rem; margin:0.5rem 0;">{:.1f} ans</p>
                </div>
            </div>
        </div>
        """.format(np.mean(df['AGE'])), unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="metric-card">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="font-size: 2rem;">⚖️</div>
                <div>
                    <h3 style="margin:0; color: var(--primary);">Ratio H/F</h3>
                    <p style="font-size: 1.5rem; margin:0.5rem 0;">{:.2f}</p>
                </div>
            </div>
        </div>
        """.format(df['SEXE'].value_counts(normalize=True)[0])), unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div class="metric-card">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="font-size: 2rem;">🕰️</div>
                <div>
                    <h3 style="margin:0; color: var(--primary);">Suivi Moyen</h3>
                    <p style="font-size: 1.5rem; margin:0.5rem 0;">{:.1f} mois</p>
                </div>
            </div>
        </div>
        """.format(np.mean(df['SUIVI_MOIS']))), unsafe_allow_html=True)
    
    st.markdown("---")

    # Section Analyse avancée
    tab1, tab2, tab3 = st.tabs(["📊 Distributions", "🔗 Corrélations", "📉 Survie"])

    with tab1:
        col1, col2 = st.columns([1, 2])
        with col1:
            selected_var = st.selectbox("Sélectionner une variable", df.columns, key='var_select')
            show_cumulative = st.checkbox("Afficher la distribution cumulative")
        
        with col2:
            fig = px.histogram(df, x=selected_var, 
                             color_discrete_sequence=['#2e77d0'],
                             cumulative=show_cumulative,
                             title=f"Distribution de {selected_var}")
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("#### 🌐 Matrice de Corrélation Thermique")
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()
        
        fig = px.imshow(corr_matrix,
                        color_continuous_scale='RdBu',
                        zmin=-1,
                        zmax=1,
                        labels={"color": "Coefficient<br>de Corrélation"})
        
        fig.update_layout(height=600,
                        coloraxis_colorbar=dict(title="Corrélation",
                                                thickness=20,
                                                yanchor="top",
                                                y=1,
                                                len=0.8))
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        kmf = KaplanMeierFitter()
        kmf.fit(df['SUIVI_MOIS'], event_observed=df['EVENEMENT'])
        
        fig, ax = plt.subplots(figsize=(10, 6))
        kmf.plot_survival_function(ax=ax, ci_show=True, color='#2e77d0')
        plt.title('Courbe de Survie Kaplan-Meier')
        plt.xlabel('Mois de suivi')
        plt.ylabel('Probabilité de survie')
        st.pyplot(fig)
        
        # Test du Log-Rank
        results = logrank_test(df['SUIVI_MOIS'], df['EVENEMENT'])
        st.markdown(f"""
        <div class="analysis-card">
            <h4>📉 Analyse de Survie</h4>
            <p>Test du Log-Rank : <strong>p-value = {results.p_value:.4f}</strong></p>
            <p style="color: #666;">Seuil de significativité : α = 0.05</p>
        </div>
        """, unsafe_allow_html=True)

    # Nouvelle section : Détection des valeurs aberrantes
    st.markdown("---")
    st.markdown("### 🚨 Détection des Valeurs Aberrantes")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    selected_outlier = st.selectbox("Sélectionner une variable numérique", numeric_cols)
    
    q1 = df[selected_outlier].quantile(0.25)
    q3 = df[selected_outlier].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df[selected_outlier] < (q1 - 1.5 * iqr)) | (df[selected_outlier] > (q3 + 1.5 * iqr))]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="analysis-card">
            <h4>📌 Statistiques des Outliers</h4>
            <p>Valeurs aberrantes détectées : {len(outliers)}</p>
            <p>Seuil inférieur : {q1 - 1.5 * iqr:.2f}</p>
            <p>Seuil supérieur : {q3 + 1.5 * iqr:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        fig = px.box(df, y=selected_outlier, color_discrete_sequence=['#2e77d0'])
        st.plotly_chart(fig, use_container_width=True)

    # Section de vérification de la qualité des données
    st.markdown("---")
    st.markdown("### 🧰 Qualité des Données")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        missing = df.isnull().sum().sum()
        st.markdown(f"""
        <div class="metric-card">
            <h4>🧩 Données Manquantes</h4>
            <p style="font-size: 1.5rem; color: {'#dc3545' if missing > 0 else '#28a745'}">{missing}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        duplicates = df.duplicated().sum()
        st.markdown(f"""
        <div class="metric-card">
            <h4>♻️ Doublons</h4>
            <p style="font-size: 1.5rem; color: {'#dc3545' if duplicates > 0 else '#28a745'}">{duplicates}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        data_types = df.dtypes.nunique()
        st.markdown(f"""
        <div class="metric-card">
            <h4>📦 Types de Données</h4>
            <p style="font-size: 1.5rem;">{data_types}</p>
        </div>
        """, unsafe_allow_html=True)
