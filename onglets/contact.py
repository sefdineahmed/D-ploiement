import streamlit as st
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ⚠️ Remplace ces valeurs par des informations sécurisées (utiliser un mot de passe d'application)
SMTP_SERVER = "smtp.gmail.com"  # Exemple pour Gmail
SMTP_PORT = 587
EMAIL_SENDER = "votre-email@gmail.com"  # Remplace par ton email
EMAIL_PASSWORD = "votre-mot-de-passe-application"  # Remplace par un mot de passe sécurisé
EMAIL_RECEIVER = "sefdine668@gmail.com"  # Destinataire (peut être le même que l'expéditeur)

def send_email(name, sender_email, message):
    """Envoie un email contenant les informations du formulaire."""
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"📩 Nouveau message de {name}"

        body = f"""
        🔹 Nom : {name}
        🔹 Email : {sender_email}
        
        📜 Message :
        {message}
        """
        msg.attach(MIMEText(body, "plain"))

        # Connexion au serveur SMTP et envoi de l'email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(sender_email, EMAIL_RECEIVER, msg.as_string())
        
        return True
    except Exception as e:
        st.error(f"❌ Erreur lors de l'envoi du message : {e}")
        return False

def validate_email(email):
    """Vérifie si l'email a un format valide."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def contact():
    """Affiche un formulaire de contact simple et efficace."""
    st.title("📩 Contactez-nous")

    # Formulaire de contact
    with st.form("contact_form"):
        name = st.text_input("Nom complet *", placeholder="Entrez votre nom")
        email = st.text_input("Email *", placeholder="exemple@domaine.com")
        message = st.text_area("Message *", placeholder="Écrivez votre message ici...")

        submit_button = st.form_submit_button("Envoyer")

        if submit_button:
            if not name or not email or not message:
                st.error("❌ Tous les champs sont obligatoires.")
            elif not validate_email(email):
                st.error("❌ Veuillez entrer une adresse email valide.")
            else:
                if send_email(name, email, message):
                    st.success("✅ Votre message a été envoyé avec succès !")
