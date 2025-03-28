import streamlit as st
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "votre-email@gmail.com"
EMAIL_PASSWORD = "12_SEFD"  
EMAIL_RECEIVER = "sefdine668@gmail.com"

def send_email(name, sender_email, message):
    """Envoie un email avec un design moderne"""
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"📬 Nouveau contact MED-AI : {name}"
        
        # Design HTML amélioré
        html = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; }}
                    .container {{ max-width: 600px; margin: 20px auto; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
                    .header {{ background: #2e77d0; padding: 30px; border-radius: 12px 12px 0 0; }}
                    .content {{ padding: 30px; color: #444444; }}
                    .footer {{ background: #f8f9fa; padding: 20px; text-align: center; font-size: 12px; color: #666666; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <img src="https://i.ibb.co/0jQd8Wz/logo.png" alt="MED-AI Logo" width="120">
                    </div>
                    <div class="content">
                        <h2 style="color: #2e77d0;">Nouveau message de {name}</h2>
                        <div style="margin: 25px 0;">
                            <p><strong>📧 Email :</strong> {sender_email}</p>
                            <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                                {message}
                            </div>
                        </div>
                    </div>
                    <div class="footer">
                        © 2024 MED-AI | Plateforme d'Intelligence Médicale
                    </div>
                </div>
            </body>
        </html>
        """
        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        
        return True
    except Exception as e:
        st.error(f"Erreur d'envoi : {str(e)}")
        return False

def validate_email(email):
    """Validation d'email avancée"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def contact():
    """Interface de contact premium"""
    
    # CSS personnalisé
    st.markdown(f"""
    <style>
        :root {{
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }}
        
        .contact-container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .contact-card {{
            background: rgba(255, 255, 255, 0.98);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(46, 119, 208, 0.1);
            transition: all 0.3s ease;
        }}
        
        .form-input {{
            margin-bottom: 1.5rem;
        }}
        
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {{
            border: 2px solid #e9ecef !important;
            border-radius: 10px !important;
            padding: 1rem !important;
            transition: all 0.3s !important;
        }}
        
        .stButton>button {{
            background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
            border: none !important;
            padding: 1rem 2rem !important;
            border-radius: 10px !important;
            font-weight: 500 !important;
            transition: 0.3s !important;
        }}
        
        .map-container {{
            border-radius: 12px;
            overflow: hidden;
            margin-top: 2rem;
        }}
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
        
        # En-tête
        st.markdown("""
        <div style="text-align: center; margin-bottom: 3rem;">
            <h1 style="color: var(--primary); margin-bottom: 1rem;">📨 Contactez Notre Équipe</h1>
            <p style="font-size: 1.1rem; color: #6c757d;">
                Une réponse garantie sous 24 heures
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Grille de contact
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with st.form("contact_form"):
                st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
                name = st.text_input("Nom Complet *", placeholder="Votre nom complet")
                email = st.text_input("Email *", placeholder="exemple@domaine.com")
                message = st.text_area("Message *", height=200, 
                                      placeholder="Décrivez votre demande en détail...")
                
                if st.form_submit_button("Envoyer le Message ✉️"):
                    if not all([name, email, message]):
                        st.error("Veuillez remplir tous les champs obligatoires")
                    elif not validate_email(email):
                        st.error("Adresse email invalide")
                    else:
                        with st.spinner("Envoi en cours..."):
                            if send_email(name, email, message):
                                st.success("Message envoyé avec succès ! 🎉")
                                st.balloons()
                st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            # Carte de visite
            st.markdown("""
            <div class='contact-card'>
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h3 style="color: var(--primary);">MED-AI Sénégal</h3>
                    <p style="color: #6c757d;">Innovation au service de la santé</p>
                </div>
                
                <div style="margin-bottom: 2rem;">
                    <h4 style="color: var(--secondary);">📌 Adresse</h4>
                    <p>Tour Médicale, 12ème étage<br>Corniche Ouest, Dakar</p>
                </div>
                
                <div style="margin-bottom: 2rem;">
                    <h4 style="color: var(--secondary);">📞 Contacts</h4>
                    <p>+221 33 876 54 32<br>support@medai.sn</p>
                </div>
                
                <div>
                    <h4 style="color: var(--secondary);">🌐 Réseaux</h4>
                    <div style="display: flex; gap: 1rem; font-size: 1.5rem;">
                        <a href="#" style="color: var(--primary);">💼</a>
                        <a href="#" style="color: var(--primary);">🐦</a>
                        <a href="#" style="color: var(--primary);">📘</a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Carte interactive
        st.markdown("""
        <div class='map-container'>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3859.227291477752!2d-17.44483768468878!3d14.693534078692495!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xec1725a1bb04215%3A0x9d5f3e9d0e8e4b1e!2sDakar!5e0!3m2!1sfr!2ssn!4v1625060000000!5m2!1sfr!2ssn" 
                width="100%" 
                height="400" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy">
            </iframe>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    contact()
