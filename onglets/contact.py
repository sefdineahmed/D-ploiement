import streamlit as st
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration visuelle
st.markdown("""
<style>
    :root {
        --primary: #2e77d0;
        --secondary: #1d5ba6;
        --accent: #22d3ee;
    }
    
    .contact-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .form-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(46, 119, 208, 0.1);
    }
    
    .input-field {
        margin-bottom: 1.5rem;
    }
    
    .input-field label {
        font-weight: 600;
        color: var(--primary);
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .stTextInput input, .stTextArea textarea {
        border: 2px solid #e2e8f0 !important;
        border-radius: 8px !important;
        padding: 0.8rem 1rem !important;
    }
    
    .success-message {
        background: #f0fdf4;
        border-left: 4px solid #22c55e;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .team-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Configuration email (à sécuriser en production)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "votre-email@gmail.com"
EMAIL_PASSWORD = "12_SEFD"  
EMAIL_RECEIVER = "sefdine668@gmail.com"

def send_email(name, sender_email, message):
    """Envoie un email professionnel avec mise en forme"""
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"📨 Nouveau contact - Plateforme MED-AI"

        body = f"""
        <div style="font-family: Arial, sans-serif; color: #1e293b;">
            <h2 style="color: {var(--primary)};">Nouveau message de {name}</h2>
            <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 8px;">
                <p><strong>📧 Email :</strong> {sender_email}</p>
                <p><strong>📅 Date :</strong> {st.session_state.contact_date}</p>
            </div>
            <div style="margin-top: 1.5rem;">
                <h3 style="color: {var(--secondary)};">Message :</h3>
                <p style="white-space: pre-wrap; line-height: 1.6;">{message}</p>
            </div>
        </div>
        """
        msg.attach(MIMEText(body, "html"))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(sender_email, EMAIL_RECEIVER, msg.as_string())
        
        return True
    except Exception as e:
        st.error(f"Erreur d'envoi : {str(e)}")
        return False

def validate_email(email):
    """Validation avancée d'email"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def contact():
    """Page de contact professionnelle"""
    st.title("📬 Nous Contacter")
    
    with st.container():
        st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
        
        # Section coordonnées
        cols = st.columns([2, 1])
        with cols[0]:
            st.subheader("📋 Formulaire de Contact")
            with st.form("contact_form"):
                st.session_state.contact_date = st.date_input("Date du contact")
                
                c1, c2 = st.columns(2)
                with c1:
                    name = st.text_input("Nom complet *", placeholder="Jean Dupont")
                with c2:
                    email = st.text_input("Email *", placeholder="contact@exemple.com")
                
                message = st.text_area("Votre message *", 
                                    placeholder="Décrivez votre demande en détail...",
                                    height=150)
                
                if st.form_submit_button("📤 Envoyer le Message", use_container_width=True):
                    if not all([name, email, message]):
                        st.error("Tous les champs obligatoires (*) doivent être remplis")
                    elif not validate_email(email):
                        st.error("Format d'email invalide")
                    else:
                        if send_email(name, email, message):
                            st.session_state.form_submitted = True
        
        with cols[1]:
            st.subheader("📍 Nous Trouver")
            st.markdown("""
            **Adresse :**  
            123 Rue de la Santé  
            75000 Ville, Sénégal
            """)
            
            # Carte interactive
            st.map(latitude=14.716677, longitude=-17.467686, zoom=12)
        
        # Section équipe
        st.markdown("---")
        st.subheader("👥 Équipe de Support")
        t_cols = st.columns(3)
        team = [
            {"name": "Dr. Alioune Ndiaye", "role": "Support Technique", "email": "tech@medai.sn"},
            {"name": "Aminata Diop", "role": "Service Clients", "email": "client@medai.sn"},
            {"name": "Moussa Fall", "role": "Développement", "email": "dev@medai.sn"}
        ]
        
        for col, member in zip(t_cols, team):
            with col:
                st.markdown(f"""
                <div class="team-card">
                    <h4>{member['name']}</h4>
                    <p style="color: {var(--primary)};">{member['role']}</p>
                    <a href="mailto:{member['email']}" style="color: {var(--secondary)};">✉️ Contact</a>
                </div>
                """, unsafe_allow_html=True)
        
        # Section FAQ
        st.markdown("---")
        with st.expander("❓ Foire aux Questions"):
            faq = {
                "Quel est le délai de réponse ?": "Nous répondons sous 24h ouvrées",
                "Comment accéder à mon compte ?": "Utilisez le portail patient dédié",
                "Problème technique ?": "Contactez notre support technique"
            }
            
            for question, reponse in faq.items():
                st.markdown(f"""
                <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 8px;">
                    <h4 style="color: {var(--primary)};">{question}</h4>
                    <p>{reponse}</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    contact()
