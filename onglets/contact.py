import streamlit as st

def contact():
    st.title("📩 Contact")
    st.markdown(
        """
        #### Coordonnées
        
        🌍 Localisation : Bambey, BP 13, Sénégal
        
        📞 Téléphone : +221 77 808 09 42
        
        📩 E-mail : ahmed.sefdine@uadb.edu.sn
        """
    )
    with st.form("contact_form"):
        name = st.text_input("Nom complet")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Envoyer"):
            st.success("✅ Message envoyé avec succès !")
