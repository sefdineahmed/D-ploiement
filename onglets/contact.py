import streamlit as st
import smtplib
import re
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv  # Pour stocker les infos sensibles

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()

# Paramètres SMTP sécurisés (Remplacez avec votre configuration)
SMTP_SERVER = "smtp.gmail.com"  # Exemple : Gmail
SMTP_PORT = 587
EMAIL_SENDER = os.getenv("sefdine668@gmail.com")  # À stocker dans un .env ou `st.secrets`
EMAIL_PASSWORD = os.getenv("SEfd_1956")  # Mot de passe d'application sécurisé

def send_email(name, sender_email, message):
    """Envoie un email via SMTP de manière sécurisée."""
    recipient_email = "sefdine668@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = recipient_email
    msg["Subject"] = f"Nouveau message de {name}"

    body = f"""
    Nom : {name}
    Email : {sender_email}

    Message :
    {message}
    """
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"❌ Erreur lors de l'envoi de l'email : {e}")
        return False

def validate_email(email):
    """Vérifie si l'email est valide."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def contact():
    """Interface du formulaire de contact."""
    st.title("📩 Contactez-nous")

    # Style CSS
    st.markdown("""
    <style>
        .section {
            background: linear-gradient(135deg, #f0f7ff, #ffffff);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            font-family: 'Poppins', sans-serif;
            text-align: center;
        }
        .contact-input {
            border: 2px solid #2e77d0;
            border-radius: 5px;
            padding: 10px;
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

    st.markdown("""
    <div class="section">
        <h4>📍 Localisation</h4>
        <p>Bambey, BP 13, Sénégal</p>
        
        <h4>📞 Téléphone</h4>
        <p>+221 77 808 09 42</p>
        
        <h4>📩 Email</h4>
        <p>sefdine668@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Nom complet *", placeholder="Entrez votre nom", help="Votre nom est requis.")
        email = st.text_input("Email *", placeholder="exemple@domaine.com", help="Votre email doit être valide.")
        message = st.text_area("Message *", placeholder="Écrivez votre message ici...", help="Écrivez votre message.")

        submit_button = st.form_submit_button("Envoyer", help="Cliquez pour envoyer votre message")

        if submit_button:
            if not name or not email or not message:
                st.error("❌ Tous les champs sont obligatoires.")
            elif not validate_email(email):
                st.error("❌ Veuillez entrer une adresse email valide.")
            else:
                sent = send_email(name, email, message)
                if sent:
                    st.success("✅ Votre message a été envoyé avec succès !")
