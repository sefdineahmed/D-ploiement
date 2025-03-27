def analyse_descriptive():
    # Style CSS avancé corrigé
    st.markdown(f"""
        <style>
            :root {{
                --primary: #6366f1;
                --secondary: #a855f7;
                --glass: rgba(255, 255, 255, 0.9);
            }}
            
            .metric-card {{
                background: var(--glass);
                backdrop-filter: blur(12px);
                border-radius: 16px;
                padding: 1.5rem;
                box-shadow: 0 4px 24px -6px rgba(99, 102, 241, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.4);
                transition: transform 0.3s ease;
            }}
            
            .metric-card:hover {{
                transform: translateY(-5px);
            }}
            
            .metric-value {{
                font-size: 2.2rem;
                font-weight: 800;
                background: linear-gradient(45deg, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                color: transparent;
            }}
            
            .chart-header {{
                font-size: 1.4rem;
                font-weight: 600;
                color: #2d3748;
                margin-bottom: 1rem;
                padding-left: 0.5rem;
                border-left: 4px solid var(--primary);
            }}
        </style>
    """, unsafe_allow_html=True)

    st.title("🔮 Exploration Analytique")
    df = load_data()
    if df.empty:
        return

    # Section Aperçu des données
    with st.container():
        st.markdown("""
            <div class='glass-container' style='margin-bottom: 2rem;'>
                <h3 style='color: var(--primary); margin-bottom: 1.5rem;'>📦 Exploration des Données Brutes</h3>
                <div style='max-height: 300px; overflow: auto; border-radius: 12px;'>
        """, unsafe_allow_html=True)
        st.dataframe(df.head(5).style.highlight_max(color='#f0f4ff'), use_container_width=True)
        st.markdown("</div></div>", unsafe_allow_html=True)
        
    # Métriques Âge
    AGE = df['AGE']
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 1.1rem; color: #4a5568;'>🎯 Âge Minimum</div>
                <div class='metric-value'>{np.min(AGE)}</div>
                <div style='color: #718096; font-size: 0.9rem;'>ans</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 1.1rem; color: #4a5568;'>📌 Âge Médian</div>
                <div class='metric-value'>{np.median(AGE):.1f}</div>
                <div style='color: #718096; font-size: 0.9rem;'>ans</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 1.1rem; color: #4a5568;'>🚀 Âge Maximum</div>
                <div class='metric-value'>{np.max(AGE)}</div>
                <div style='color: #718096; font-size: 0.9rem;'>ans</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # Visualisations
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown("<div class='chart-header'>📊 Distribution Dynamique</div>", unsafe_allow_html=True)
            selected_var = st.selectbox("Choisir une variable", df.columns, key='var_select')
            fig_hist = px.histogram(
                df, 
                x=selected_var, 
                color_discrete_sequence=['#6366f1'],
                nbins=30,
                template='plotly_white',
                marginal='rug'
            )
            fig_hist.update_layout(
                plot_bgcolor='rgba(255,255,255,0.8)',
                paper_bgcolor='rgba(255,255,255,0.5)',
                hoverlabel=dict(
                    bgcolor="white",
                    font_size=14
                )
            )
            st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        with st.container():
            st.markdown("<div class='chart-header'>🌐 Matrice de Corrélations</div>", unsafe_allow_html=True)
            numeric_df = df.select_dtypes(include=["number"])
            corr_matrix = numeric_df.corr()
            
            fig_corr = px.imshow(
                corr_matrix,
                color_continuous_scale='PuOr_r',
                aspect='auto',
                template='plotly_white'
            )
            
            fig_corr.update_layout(
                coloraxis_colorbar=dict(
                    title='Corrélation',
                    thickness=15,
                    len=0.5
                ),
                xaxis=dict(tickangle=45),
                margin=dict(l=0, r=0)
            )
            
            st.plotly_chart(fig_corr, use_container_width=True)
    
    st.markdown("---")
