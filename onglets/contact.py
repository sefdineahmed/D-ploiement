import streamlit as st
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration SMTP (à remplacer par vos informations)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "votre-email@gmail.com"
EMAIL_PASSWORD = "12_SEFD"  
EMAIL_RECEIVER = "sefdine668@gmail.com"

def send_email(name, sender_email, message):
    """Envoie un email avec un design HTML professionnel"""
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"📬 Nouveau contact depuis MED-AI : {name}"
        
        # Corps du message en HTML
        html = f"""
        <html>
          <body style="font-family: Arial, sans-serif;">
            <div style="background: #f8f9fa; padding: 30px; border-radius: 10px;">
              <h2 style="color: #2e77d0; border-bottom: 2px solid #2e77d0; padding-bottom: 10px;">
                Nouveau message de {name}
              </h2>
              <div style="margin: 20px 0;">
                <p><strong>📧 Email :</strong> {sender_email}</p>
                <p><strong>📝 Message :</strong></p>
                <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0;">
                  {message}
                </div>
              </div>
              <footer style="color: #6c757d; font-size: 0.9em;">
                Envoyé via la plateforme MED-AI
              </footer>
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
        st.error(f"❌ Erreur d'envoi : {str(e)}")
        return False

def validate_email(email):
    """Validation avancée d'email"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def contact():
    """Interface de contact professionnelle"""
    
    # Style CSS personnalisé
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
        
        .contact-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(46, 119, 208, 0.1);
        }
        
        .form-input {
            margin-bottom: 1.5rem;
        }
        
        .form-input label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--primary);
            font-weight: 500;
        }
        
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            border: 2px solid #e9ecef;
            border-radius: 8px;
            padding: 0.8rem;
            transition: all 0.3s;
        }
        
        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(46, 119, 208, 0.1);
        }
        
        .stButton>button {
            background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
            color: white !important;
            border: none !important;
            padding: 1rem 2rem !important;
            border-radius: 8px !important;
            transition: all 0.3s !important;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(46, 119, 208, 0.3) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
        
        # En-tête
        st.markdown("""
        <div style="text-align: center; margin-bottom: 3rem;">
            <h1 style="color: var(--primary); margin-bottom: 1rem;">📬 Contactez Notre Équipe</h1>
            <p style="font-size: 1.1rem; color: #6c757d;">
                Nous vous répondrons dans les 24 heures
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Grille de contact
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with st.form("contact_form"):
                st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
                
                # Formulaire
                st.markdown("<div class='form-input'>", unsafe_allow_html=True)
                name = st.text_input("Nom Complet *", placeholder="Jean Dupont")
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("<div class='form-input'>", unsafe_allow_html=True)
                email = st.text_input("Email *", placeholder="contact@exemple.com")
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("<div class='form-input'>", unsafe_allow_html=True)
                message = st.text_area("Message *", height=150, 
                                      placeholder="Décrivez votre demande en détail...")
                st.markdown("</div>", unsafe_allow_html=True)
                
                submitted = st.form_submit_button("Envoyer le Message ✉️")
                st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            # Informations de contact
            st.markdown("""
            <div class='contact-card' style="padding: 1.5rem;">
                <h3 style="color: var(--primary); margin-bottom: 1rem;">📌 Nous trouver</h3>
                
                <div style="margin-bottom: 1.5rem;">
                    <h4 style="color: var(--secondary); margin: 0.5rem 0;">🏢 Adresse</h4>
                    <p style="margin: 0; color: #6c757d;">
                        Centre Médical Avancé<br>
                        123 Rue de la Santé<br>
                        Dakar, Sénégal
                    </p>
                </div>
                
                <div style="margin-bottom: 1.5rem;">
                    <h4 style="color: var(--secondary); margin: 0.5rem 0;">📞 Téléphone</h4>
                    <p style="margin: 0; color: #6c757d;">
                        +221 33 123 45 67<br>
                        (Lun-Ven : 8h-18h)
                    </p>
                </div>
                
                <div>
                    <h4 style="color: var(--secondary); margin: 0.5rem 0;">🌐 Réseaux sociaux</h4>
                    <div style="display: flex; gap: 1rem; font-size: 1.5rem;">
                        <a href="#" style="color: var(--primary);">📘</a>
                        <a href="#" style="color: var(--primary);">📷</a>
                        <a href="#" style="color: var(--primary);">💼</a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Validation et envoi
        if submitted:
            if not all([name, email, message]):
                st.error("🚨 Tous les champs obligatoires (*) doivent être remplis")
            elif not validate_email(email):
                st.error("📧 Veuillez saisir une adresse email valide")
            else:
                with st.spinner("Envoi en cours..."):
                    if send_email(name, email, message):
                        st.success("✅ Message envoyé avec succès !")
                        st.balloons()

        # Carte interactive
        st.markdown("""
        <div class='contact-card' style="margin-top: 2rem;">
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3859.227291477752!2d-17.44483768468878!3d14.693534078692495!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xec1725a1bb04215%3A0x9d5f3e9d0e8e4b1e!2sDakar!5e0!3m2!1sfr!2ssn!4v1625060000000!5m2!1sfr!2ssn" 
                width="100%" 
                height="300" 
                style="border:0; border-radius: 8px;" 
                allowfullscreen="" 
                loading="lazy">
            </iframe>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    contact()
