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
          <head>
            <style>
              body {{ font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; }}
              .header {{ background: #2e77d0; padding: 40px; color: white; text-align: center; }}
              .content {{ padding: 40px 20px; max-width: 600px; margin: 0 auto; }}
              .message-box {{ background: #f8f9fa; border-radius: 10px; padding: 20px; margin: 20px 0; }}
              .footer {{ text-align: center; padding: 20px; color: #6c757d; font-size: 0.9em; }}
            </style>
          </head>
          <body>
            <div class="header">
              <h1>MED-AI Contact</h1>
              <p>Nouveau message reçu</p>
            </div>
            
            <div class="content">
              <div style="margin-bottom: 30px;">
                <h3 style="color: #2e77d0;">🗒 Détails du contact</h3>
                <p><strong>👤 Nom :</strong> {name}</p>
                <p><strong>📧 Email :</strong> {sender_email}</p>
              </div>
              
              <div class="message-box">
                <h4 style="margin-top: 0; color: #1d5ba6;">📝 Message :</h4>
                <p>{message}</p>
              </div>
            </div>
            
            <div class="footer">
              <p>© 2024 MED-AI | Support technique : support@medai.sn</p>
              <p>🚨 Ceci est un message automatique, ne pas répondre</p>
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
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .contact-container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .contact-card {
            background: white;
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);
            margin: 2rem 0;
        }
        
        .form-header {
            border-left: 4px solid var(--primary);
            padding-left: 1.5rem;
            margin-bottom: 2.5rem;
        }
        
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            border: 2px solid #e9ecef !important;
            border-radius: 10px !important;
            padding: 1rem !important;
            transition: all 0.3s !important;
        }
        
        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px rgba(46, 119, 208, 0.1) !important;
        }
        
        .stButton>button {
            background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
            color: white !important;
            padding: 1rem 2rem !important;
            border-radius: 12px !important;
            transition: all 0.3s !important;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(46, 119, 208, 0.3) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
        
        # Section Héros
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0;">
            <h1 style="font-size: 2.8rem; color: var(--primary); margin-bottom: 1rem;">
                ✉️ Contactez Notre Équipe Médicale
            </h1>
            <p style="font-size: 1.2rem; color: #4b5563;">
                Une réponse garantie sous 24 heures ouvrées
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Grille de contact
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with st.form("contact_form"):
                st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
                st.markdown("<div class='form-header'><h2>📤 Envoyer un Message</h2></div>", unsafe_allow_html=True)
                
                # Formulaire amélioré
                name = st.text_input("👤 Nom Complet *", placeholder="Dr. Jean Dupont")
                email = st.text_input("📧 Email Professionnel *", placeholder="contact@clinique.sn")
                message = st.text_area("💬 Message *", height=200,
                                     placeholder="Décrivez votre demande en détail...\n\nExemples :\n- Prise de rendez-vous\n- Demande de partenariat\n- Question médicale")
                
                submitted = st.form_submit_button("📨 Envoyer le Message")
                st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            # Carte de contact élégante
            st.markdown("""
            <div class='contact-card' style="padding: 2rem;">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">📌 Nous Contacter</h3>
                    <div style="display: inline-block; background: #f8f9fa; padding: 1rem; border-radius: 12px;">
                        <img src="https://via.placeholder.com/150" style="width: 120px; height: 120px; border-radius: 50%; margin-bottom: 1rem;">
                        <h4 style="margin: 0.5rem 0;">Service Relation Patients</h4>
                        <p style="color: #6c757d; margin: 0;">À votre écoute 7j/7</p>
                    </div>
                </div>
                
                <div style="margin-bottom: 2rem;">
                    <h4 style="color: var(--secondary); margin-bottom: 1rem;">📞 Contacts Urgents</h4>
                    <div style="background: #fff5f5; padding: 1rem; border-radius: 8px;">
                        <p style="margin: 0; color: #dc3545;">🚨 Urgences Médicales : +221 33 765 43 21</p>
                    </div>
                </div>
                
                <div>
                    <h4 style="color: var(--secondary); margin-bottom: 1rem;">🌍 Réseaux</h4>
                    <div style="display: flex; gap: 1rem; justify-content: center; font-size: 1.5rem;">
                        <a href="#" style="color: var(--primary);">🌐</a>
                        <a href="#" style="color: var(--primary);">💼</a>
                        <a href="#" style="color: var(--primary);">📷</a>
                        <a href="#" style="color: var(--primary);">🎥</a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Validation et envoi
        if submitted:
            if not all([name, email, message]):
                st.error("🚨 Tous les champs marqués d'un * sont obligatoires")
            elif not validate_email(email):
                st.error("📧 Format d'email invalide (exemple@domaine.com)")
            else:
                with st.spinner("Envoi en cours..."):
                    if send_email(name, email, message):
                        st.success("✅ Message envoyé avec succès !")
                        st.balloons()

        # Section Carte et FAQ
        st.markdown("""
        <div class='contact-card' style="margin-top: 2rem; padding: 0;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; padding: 2rem;">
                <div>
                    <h3 style="color: var(--primary);">🗺️ Notre Localisation</h3>
                    <iframe 
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3859.227291477752!2d-17.44483768468878!3d14.693534078692495!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xec1725a1bb04215%3A0x9d5f3e9d0e8e4b1e!2sDakar!5e0!3m2!1sfr!2ssn!4v1625060000000!5m2!1sfr!2ssn" 
                        width="100%" 
                        height="300" 
                        style="border:0; border-radius: 8px;" 
                        loading="lazy">
                    </iframe>
                </div>
                
                <div>
                    <h3 style="color: var(--primary);">❓ Foire Aux Questions</h3>
                    <div style="margin-top: 1rem;">
                        <details style="margin-bottom: 1rem; padding: 1rem; border-radius: 8px; border: 1px solid #e9ecef;">
                            <summary><strong>Quel est le délai de réponse ?</strong></summary>
                            <p style="margin: 0.5rem 0;">Nous nous engageons à répondre sous 24h ouvrées</p>
                        </details>
                        
                        <details style="margin-bottom: 1rem; padding: 1rem; border-radius: 8px; border: 1px solid #e9ecef;">
                            <summary><strong>Comment annuler un rendez-vous ?</strong></summary>
                            <p style="margin: 0.5rem 0;">Contactez-nous par téléphone au +221 33 123 45 67</p>
                        </details>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    contact()
