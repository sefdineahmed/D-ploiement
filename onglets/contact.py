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
    """Envoie un email avec un design HTML professionnel"""
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"🌟 Nouveau contact MED-AI : {name}"
        
        html = f"""
        <html>
          <body style="font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0;">
            <div style="background: #f8faff; padding: 40px; border-radius: 20px;">
              <div style="text-align: center; margin-bottom: 30px;">
                <img src="https://i.ibb.co.com/your-logo.png" alt="MED-AI Logo" style="height: 60px;">
              </div>
              <div style="background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <h2 style="color: #2563eb; margin: 0 0 25px 0; font-size: 22px;">
                  Nouveau message de <span style="color: #1e40af;">{name}</span>
                </h2>
                <div style="margin-bottom: 25px;">
                  <div style="display: flex; align-items: center; margin-bottom: 15px;">
                    <div style="background: #eff6ff; padding: 10px; border-radius: 8px; margin-right: 15px;">
                      📧
                    </div>
                    <div>
                      <p style="margin: 0; font-weight: 500; color: #1e293b;">Email</p>
                      <p style="margin: 0; color: #64748b;">{sender_email}</p>
                    </div>
                  </div>
                  <div style="background: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0;">
                    <p style="margin: 0; color: #475569; line-height: 1.6;">{message}</p>
                  </div>
                </div>
                <div style="border-top: 2px solid #f1f5f9; padding-top: 20px; text-align: center;">
                  <p style="color: #94a3b8; font-size: 14px;">Message envoyé via la plateforme MED-AI</p>
                </div>
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
        st.error(f"❌ Erreur d'envoi : {str(e)}")
        return False

def validate_email(email):
    """Validation avancée d'email"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def contact():
    """Interface de contact premium"""
    
    st.markdown("""
    <style>
        :root {
            --primary: #2563eb;
            --secondary: #1e40af;
            --accent: #22d3ee;
            --background: #f8fafc;
        }
        
        .contact-container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        .contact-header {
            text-align: center;
            padding: 4rem 0 2rem;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .form-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(221, 221, 221, 0.2);
            backdrop-filter: blur(12px);
        }
        
        .info-card {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 16px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
        }
        
        .info-card::before {
            content: '';
            position: absolute;
            top: -50px;
            right: -50px;
            width: 120px;
            height: 120px;
            background: rgba(34, 211, 238, 0.1);
            border-radius: 50%;
        }
        
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            border: 2px solid #e2e8f0 !important;
            border-radius: 10px !important;
            padding: 1rem !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        
        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
        }
        
        .stButton>button {
            background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
            color: white !important;
            padding: 1rem 2rem !important;
            border-radius: 12px !important;
            transition: all 0.3s !important;
            width: 100% !important;
        }
        
        .map-container {
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            margin: 2rem 0;
        }
        
        .social-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 0.8rem 1.2rem;
            border-radius: 50px;
            background: rgba(37, 99, 235, 0.1);
            color: var(--primary);
            transition: all 0.3s;
        }
        
        .social-badge:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
        
        # En-tête
        st.markdown("""
            <div class='contact-header'>
                <h1 style='font-size: 2.8rem; margin-bottom: 1rem;'>📬 Contactez Nos Experts</h1>
                <p style='font-size: 1.2rem; color: #64748b;'>
                    Une question ? Une suggestion ? Notre équipe est à votre écoute
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Grille de contact
        col1, col2 = st.columns([2, 1], gap="large")
        
        with col1:
            with st.form("contact_form"):
                st.markdown("<div class='form-card'>", unsafe_allow_html=True)
                
                # Formulaire
                name = st.text_input("Nom Complet *", placeholder="Dr. Jean Dupont")
                email = st.text_input("Email Professionnel *", placeholder="contact@hopital.com")
                message = st.text_area("Votre Message *", height=200, 
                                      placeholder="Décrivez votre demande en détail...")
                
                submitted = st.form_submit_button("Envoyer le Message 🚀")
                st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            # Informations de contact
            st.markdown("""
            <div class='info-card'>
                <div style="margin-bottom: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1.5rem;">📌 Nous Contacter</h3>
                    
                    <div style="margin-bottom: 1.5rem;">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div style="background: rgba(37, 99, 235, 0.1); padding: 12px; border-radius: 12px;">
                                📍
                            </div>
                            <div>
                                <p style="margin: 0; font-weight: 500; color: #1e293b;">Adresse</p>
                                <p style="margin: 0; color: #64748b; font-size: 0.9em;">
                                    Tour Médicale, 12ème étage<br>
                                    Corniche Ouest, Dakar
                                </p>
                            </div>
                        </div>
                        
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <div style="background: rgba(37, 99, 235, 0.1); padding: 12px; border-radius: 12px;">
                                📞
                            </div>
                            <div>
                                <p style="margin: 0; font-weight: 500; color: #1e293b;">Téléphone</p>
                                <p style="margin: 0; color: #64748b; font-size: 0.9em;">
                                    +221 33 123 45 67<br>
                                    Support 24h/24
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <h4 style="color: var(--primary); margin-bottom: 1rem;">🔗 Réseaux Sociaux</h4>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="#" class="social-badge">
                            <span>LinkedIn</span> 💼
                        </a>
                        <a href="#" class="social-badge">
                            <span>Twitter</span> 🐦
                        </a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Validation et envoi
        if submitted:
            if not all([name, email, message]):
                st.error("🚨 Veuillez remplir tous les champs obligatoires")
            elif not validate_email(email):
                st.error("📧 Format d'email invalide")
            else:
                with st.spinner("Envoi en cours..."):
                    if send_email(name, email, message):
                        st.success("✅ Message envoyé avec succès !")
                        st.balloons()

        # Section supplémentaire : FAQ
        st.markdown("""
        <div class='info-card' style="margin: 3rem 0;">
            <h3 style="color: var(--primary); margin-bottom: 1.5rem;">❓ Questions Fréquentes</h3>
            
            <div style="margin-bottom: 1.5rem;">
                <details style="margin-bottom: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 1rem;">
                    <summary style="font-weight: 500; cursor: pointer;">Quel est le délai de réponse ?</summary>
                    <p style="color: #64748b; margin: 0.5rem 0 0 0;">Notre équipe s'engage à répondre sous 24h ouvrées</p>
                </details>
                
                <details style="margin-bottom: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 1rem;">
                    <summary style="font-weight: 500; cursor: pointer;">Comment obtenir une consultation ?</summary>
                    <p style="color: #64748b; margin: 0.5rem 0 0 0;">Contactez-nous via ce formulaire pour prendre rendez-vous</p>
                </details>
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
