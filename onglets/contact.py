import streamlit as st
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Paramètres SMTP (à configurer avec un vrai serveur)
SMTP_SERVER = "smtp.gmail.com"  # Ex: smtp.gmail.com pour Gmail
SMTP_PORT = 587
EMAIL_SENDER = "sefdine668@gmail.com"  # Remplacez par votre email d'envoi
EMAIL_PASSWORD = "SEfd_1956"  # Remplacez par votre mot de passe (ou mot de passe d'application)

def send_email(name, sender_email, message):
    """Envoie un email via SMTP."""
    recipient_email = "sefdine668@gmail.com"
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = f"Nouveau message de {name}"

    body = f"""
    Nom: {name}
    Email: {sender_email}
    
    Message:
    {message}
    """
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"❌ Erreur lors de l'envoi de l'email : {e}")
        return False

def validate_email(email):
    """Vérifie si l'email a un format valide."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def contact():
    st.title("📩 Contactez-nous")
    
    st.markdown("""
    <style>
        .section {
            background: linear-gradient(135deg, #ffffff, #f8f9fa);
            padding: 2em;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            font-family: 'Poppins', sans-serif;
        }
        .btn-submit {
            background-color: #2e77d0;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        .btn-submit:hover {
            background-color: #1b5b9e;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section">
        <h4>📍 Localisation</h4>
        <p>Bambey, BP 13, Sénégal</p>
        
        <h4>📞 Téléphone</h4>
        <p>+221 77 808 09 42</p>
        
        <h4>📩 Email</h4>
        <p>sefdine668@gmail.com</p>
        </div>
        """, unsafe_allow_html=True
    )

    with st.form("contact_form"):
        name = st.text_input("Nom complet *", placeholder="Entrez votre nom")
        email = st.text_input("Email *", placeholder="exemple@domaine.com")
        message = st.text_area("Message *", placeholder="Écrivez votre message ici...")

        submit_button = st.form_submit_button("Envoyer", help="Cliquez pour envoyer le message")

        if submit_button:
            if not name or not email or not message:
                st.error("❌ Tous les champs sont obligatoires.")
            elif not validate_email(email):
                st.error("❌ Veuillez entrer une adresse email valide.")
            else:
                sent = send_email(name, email, message)
                if sent:
                    st.success("✅ Votre message a été envoyé avec succès !")
