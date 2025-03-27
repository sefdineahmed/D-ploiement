import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

def envoyer_email(subject, body, to_email):
    try:
        # Paramètres d'authentification SMTP
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "votre_email@gmail.com"  # Remplacez par votre adresse email
        sender_password = "votre_mot_de_passe"  # Remplacez par votre mot de passe ou utilisez un mot de passe d'application

        # Créer l'objet MIMEMultipart
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject

        # Ajouter le corps du message
        message.attach(MIMEText(body, "plain"))

        # Connexion au serveur SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Sécuriser la connexion
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
            st.success("✅ Message envoyé avec succès !")
    except Exception as e:
        st.error(f"Erreur lors de l'envoi de l'e-mail : {e}")

def contact():
    st.title("📩 Contact")
    
    # Style personnalisé
    st.markdown("""
    <style>
        .contact-header {
            text-align: center;
            margin-bottom: 2rem;
            font-family: 'Poppins', sans-serif;
        }
        .contact-header h2 {
            color: #2e77d0;
            font-size: 2.5rem;
        }
        .contact-header p {
            color: #6c757d;
            font-size: 1.1rem;
        }
        .contact-info {
            text-align: center;
            margin-bottom: 2rem;
            font-family: 'Poppins', sans-serif;
            font-size: 1.1rem;
            color: #333;
        }
        .contact-form {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: auto;
            font-family: 'Poppins', sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # En-tête
    st.markdown("""
    <div class="contact-header">
        <h2>Contactez-nous</h2>
        <p>Envoyez-nous un message et nous reviendrons vers vous dès que possible.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Coordonnées de contact
    st.markdown("""
    <div class="contact-info">
        <p>🌍 Localisation : Bambey, BP 13, Sénégal</p>
        <p>📞 Téléphone : +221 77 808 09 42</p>
        <p>📩 E-mail : ahmed.sefdine@uadb.edu.sn</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Formulaire de contact
    with st.form("contact_form", clear_on_submit=True):
        st.markdown('<div class="contact-form">', unsafe_allow_html=True)
        name = st.text_input("Nom complet *", placeholder="Votre nom complet")
        email = st.text_input("Email *", placeholder="exemple@domaine.com")
        message = st.text_area("Message *", placeholder="Votre message ici...")
        submitted = st.form_submit_button("Envoyer")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if submitted:
            # Vérification que tous les champs sont remplis
            if not name or not email or not message:
                st.error("Tous les champs sont obligatoires.")
            else:
                # Validation du format de l'email
                pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
                if not re.match(pattern, email):
                    st.error("Veuillez saisir un email valide.")
                else:
                    subject = f"Message de {name}"
                    body = f"""
                    Nom : {name}
                    Email : {email}
                    
                    Message :
                    {message}
                    """
                    # Envoi de l'email
                    envoyer_email(subject, body, "ahmed.sefdine@uadb.edu.sn")
