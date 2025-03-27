def modelisation():
    # Style CSS avancé
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2563eb;
            --secondary: #1e40af;
            --accent: #0891b2;
            --background: #f8fafc;
        }}
        
        .prediction-card {{
            background: white;
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
            border: 1px solid #e2e8f0;
        }}
        
        .metric-badge {{
            background: rgba(8, 145, 178, 0.1);
            color: var(--accent);
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid rgba(8, 145, 178, 0.2);
        }}
        
        .timeline {{
            position: relative;
            padding-left: 20px;
            margin: 2rem 0;
        }}
        
        .timeline::before {{
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            width: 2px;
            height: 100%;
            background: var(--accent);
        }}
    </style>
    """, unsafe_allow_html=True)

    # Section principale
    with st.container():
        st.title("🎯 Prédiction de Survie Oncologique")
        
        # 1️⃣ Formulaire médical
        with st.expander("📋 Dossier Patient", expanded=True):
            cols = st.columns([2, 1])
            with cols[0]:
                inputs = {}
                grid = st.columns(3)
                for i, (feature, label) in enumerate(FEATURE_CONFIG.items()):
                    with grid[i % 3]:
                        if feature == "AGE":
                            inputs[feature] = st.number_input(label, min_value=18, max_value=120, value=50)
                        else:
                            inputs[feature] = st.selectbox(label, options=["Non", "Oui"])
            
            with cols[1]:
                st.image("assets/medical_illustration.png", use_column_width=True)
        
        st.markdown("---")
        
        # 2️⃣ Sélection du modèle
        st.subheader("🧠 Paramètres d'Analyse")
        model_cols = st.columns([3, 1])
        with model_cols[0]:
            model_name = st.selectbox("Modèle d'IA", list(MODELS.keys()), 
                                    help="Sélectionnez l'algorithme de prédiction adapté au cas clinique")
        
        # 3️⃣ Prédiction et visualisation
        if st.button("Lancer l'analyse prédictive", type="primary"):
            with st.spinner("Analyse en cours..."):
                try:
                    input_df = encode_features(inputs)
                    model = load_model(MODELS[model_name])
                    pred = predict_survival(model, input_df, model_name)
                    cleaned_pred = clean_prediction(pred, model_name)
                    
                    # Affichage des résultats
                    with st.container():
                        st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
                        
                        # Métrique principale
                        cols = st.columns([2, 1])
                        with cols[0]:
                            st.markdown(f"""
                            <div class='metric-badge'>
                                <h3 style='margin:0; color: var(--secondary);'>Survie Médiane Estimée</h3>
                                <div style='font-size: 2.5rem; font-weight: 700;'>{cleaned_pred:.1f} mois</div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Graphique interactif
                        with cols[1]:
                            months = min(int(cleaned_pred), 120)
                            fig = px.line(
                                x=list(range(months)),
                                y=[100 - (i / months) * 100 for i in range(months)],
                                labels={"x": "Mois", "y": "Probabilité de Survie (%)"},
                                color_discrete_sequence=[var(--primary)]
                            )
                            st.plotly_chart(fig, use_container_width=True)
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                        # Timeline thérapeutique
                        st.subheader("📅 Planification du Traitement")
                        treatment_steps = [
                            {"title": "Évaluation Initiale", "duration": "J1-J7"},
                            {"title": "Traitement Actif", "duration": "J8-J90"},
                            {"title": "Suivi Post-Traitement", "duration": "M3-M12"}
                        ]
                        
                        st.markdown("<div class='timeline'>", unsafe_allow_html=True)
                        for step in treatment_steps:
                            with st.container():
                                st.markdown(f"""
                                <div style='margin: 1rem 0; padding-left: 1rem;'>
                                    <h4 style='margin:0;'>{step['title']}</h4>
                                    <p style='color: #64748b; margin:0;'>{step['duration']}</p>
                                </div>
                                """, unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                        # Génération du rapport
                        pdf_bytes = generate_pdf_report(inputs, model_name, cleaned_pred)
                        st.download_button(
                            label="📥 Télécharger le Rapport Complet",
                            data=pdf_bytes,
                            file_name="rapport_medical.pdf",
                            mime="application/pdf",
                            type="primary"
                        )
                        
                except Exception as e:
                    st.error(f"Erreur d'analyse : {str(e)}")
        
        # 4️⃣ Base de connaissances
        st.markdown("---")
        with st.expander("📚 Recommandations Thérapeutiques"):
            tabs = st.tabs(["Chimiothérapie", "Radiothérapie", "Soins de Support"])
            with tabs[0]:
                st.markdown("""
                **Protocole Standard (FOLFOX)**
                - Oxaliplatine 85 mg/m²
                - Acide folinique 400 mg/m²
                - 5-FU 400 mg/m² en bolus
                """)
            
            with tabs[1]:
                st.markdown("""
                **Schéma de Radiothérapie**
                - Dose totale : 45-50 Gy
                - Fractionnement : 1.8-2 Gy/jour
                - Durée : 5 semaines
                """)
        
        # 5️⃣ Suivi patient
        st.markdown("---")
        st.subheader("🔔 Gestion du Suivi")
        followup_cols = st.columns(2)
        with followup_cols[0]:
            st.date_input("Prochaine Consultation", value=date.today())
        with followup_cols[1]:
            st.multiselect("Alertes Automatiques", options=["Rappel RDV", "Bilan sanguin", "Imagerie"])

if __name__ == "__main__":
    modelisation()
