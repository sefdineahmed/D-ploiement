def analyse_descriptive():
    # CSS personnalisé
    st.markdown(f"""
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #10b981;
            --glass: rgba(255, 255, 255, 0.7);
        }}
        
        .metric-card {{
            background: var(--glass);
            backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 1.5rem;
            margin: 0.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            transition: transform 0.3s ease;
            border: 1px solid rgba(255,255,255,0.3);
        }}
        
        .metric-card:hover {{
            transform: translateY(-5px);
        }}
        
        .hover-plot {{
            transition: all 0.3s ease;
            border-radius: 16px;
            overflow: hidden;
        }}
        
        .hover-plot:hover {{
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        
        .section-title {{
            font-family: 'Inter', sans-serif;
            color: #1f2937;
            font-weight: 700;
            margin-bottom: 1rem;
            position: relative;
            padding-left: 1.5rem;
        }}
        
        .section-title:before {{
            content: '';
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 4px;
            height: 70%;
            background: linear-gradient(to bottom, var(--primary), var(--secondary));
            border-radius: 2px;
        }}
    </style>
    """, unsafe_allow_html=True)

    st.title("🔮 Exploration des Données")
    df = load_data()
    if df.empty:
        return

    # Section aperçu des données
    with st.expander("📂 Exploration des Données Brutes", expanded=True):
        with st.container():
            cols = st.columns([3, 1])
            with cols[0]:
                st.dataframe(df.head(5).style.background_gradient(cmap='Blues'), height=200)
            with cols[1]:
                st.metric("📊 Patients", df.shape[0])
                st.metric("📈 Variables", df.shape[1])
    
    st.markdown("---")
    
    # Section métriques age
    AGE = df['AGE']
    stats = {
        "🧒 Jeune": np.min(AGE),
        "👨⚕️ Médian": np.median(AGE),
        "🧓 Senior": np.max(AGE)
    }
    
    with st.container():
        st.markdown('<div class="section-title">Distribution d\'Âge</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, (title, value) in enumerate(stats.items()):
            with cols[i]:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size: 1.2rem; color: #6b7280; margin-bottom: 0.5rem;">{title}</div>
                    <div style="font-size: 2rem; font-weight: 700; color: var(--primary);">{value:.1f} ans</div>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section visualisations interactives
    with st.container():
        tabs = st.tabs(["📊 Distribution", "🌐 Corrélations"])
        
        with tabs[0]:
            selected_var = st.selectbox("Choisir une variable", df.columns, key='var_select')
            fig_hist = px.histogram(
                df, 
                x=selected_var, 
                color_discrete_sequence=['#6366f1'],
                template='plotly_white',
                labels={'count': 'Fréquence'},
                title=f"Distribution de {selected_var}"
            ).update_layout(height=400)
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with tabs[1]:
            numeric_df = df.select_dtypes(include=["number"])
            corr_matrix = numeric_df.corr()
            fig_corr = px.imshow(
                corr_matrix,
                color_continuous_scale='Tealrose',
                labels={'color': 'Corrélation'},
                title="Matrice de Corrélation Interactive"
            ).update_layout(height=500)
            
            # Annotation dynamique
            fig_corr.update_traces(
                hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>Corrélation: %{z:.2f}<extra></extra>"
            )
            st.plotly_chart(fig_corr, use_container_width=True)
    
    st.markdown("---")
