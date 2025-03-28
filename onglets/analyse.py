def analyse_descriptive():
    # Configuration du style CSS
    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .eda-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 1rem;
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
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            transition: transform 0.3s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
        }
        
        .section-title {
            color: var(--primary);
            border-left: 4px solid var(--accent);
            padding-left: 1rem;
            margin: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='eda-container'>", unsafe_allow_html=True)
    
    # En-tête
    st.markdown("""
    <div class='header-card'>
        <h1 style="margin:0; font-size:2.5rem">📈 Analyse Exploratoire des Données</h1>
        <p style="opacity:0.9; font-size:1.1rem">Exploration interactive des données patients</p>
    </div>
    """, unsafe_allow_html=True)

    df = load_data()
    if df.empty:
        return

    # Section aperçu des données
    with st.expander("🔎 Aperçu des Données Brutes", expanded=True):
        st.dataframe(df.head(10).style.set_properties(**{
            'background-color': '#f8f9fa',
            'color': '#212529',
            'border': '1px solid #dee2e6'
        })
        st.markdown(f"""
        <div style="padding:1rem; background:#f8f9fa; border-radius:8px; margin-top:1rem">
            📐 Dimensions du dataset : 
            <strong>{df.shape[0]}</strong> patients · 
            <strong>{df.shape[1]}</strong> variables
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section analyse démographique
    st.markdown("<h3 class='section-title'>📌 Analyse Démographique</h3>", unsafe_allow_html=True)
    AGE = df['AGE']
    cols = st.columns(3)
    stats = [
        ("🧒 Âge Minimum", np.min(AGE)),
        ("📊 Âge Médian", np.median(AGE)),
        ("👴 Âge Maximum", np.max(AGE))
    ]
    
    for col, (title, value) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <div style="font-size:1.2rem; color:var(--primary); margin-bottom:0.5rem">{title}</div>
                <div style="font-size:2rem; font-weight:700">{value:.1f} ans</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section analyse multivariée
    st.markdown("<h3 class='section-title'>🔍 Analyse Multivariée</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div style="background:white; padding:1.5rem; border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,0.05)">
            <h4 style="color:var(--primary))">Paramètres d'Analyse</h4>
            <div style="margin:1.5rem 0">
                <div style="margin-bottom:1.5rem">
                    <label style="display:block; margin-bottom:0.5rem">Variable Numérique</label>
                    {st.selectbox("", df.select_dtypes(include='number').columns, key='num_var')}
                </div>
                <div>
                    <label style="display:block; margin-bottom:0.5rem">Variable Catégorielle</label>
                    {st.selectbox("", df.select_dtypes(exclude='number').columns, key='cat_var')}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Boxplot interactif
        fig = px.box(df, 
                     x=st.session_state.cat_var, 
                     y=st.session_state.num_var, 
                     color=st.session_state.cat_var,
                     color_discrete_sequence=[var(--primary), var(--secondary)])
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Nouvelle section : Analyse de survie
    st.markdown("<h3 class='section-title'>⏳ Analyse de Survie</h3>", unsafe_allow_html=True)
    
    if time_col in df.columns and event_col in df.columns:
        kmf = KaplanMeierFitter()
        kmf.fit(df[time_col], df[event_col])
        
        fig = px.line(
            x=kmf.timeline,
            y=kmf.survival_function_,
            labels={'x': 'Temps (mois)', 'y': 'Probabilité de Survie'},
            color_discrete_sequence=[var(--primary)]
        )
        fig.update_layout(
            hovermode="x unified",
            title="Courbe de Kaplan-Meier"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Colonnes de survie manquantes dans le dataset")
    
    st.markdown("</div>", unsafe_allow_html=True)
