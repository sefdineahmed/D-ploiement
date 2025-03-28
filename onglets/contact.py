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
        msg["Subject"] = f"📬 Nouveau contact depuis MED-AI : {name}"
        
        # Corps du message en HTML
        html = f"""
        <html>
          <body style="font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0;">
            <div style="background: #f8fafc; padding: 40px; border-radius: 16px;">
              <div style="max-width: 600px; margin: 0 auto;">
                <div style="text-align: center; margin-bottom: 30px;">
                  <img src="https://i.ibb.co.com/logo.png" alt="MED-AI Logo" style="height: 60px;">
                </div>
                
                <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.05);">
                  <h2 style="color: #2e77d0; margin-bottom: 20px; border-bottom: 2px solid #f0f4ff; padding-bottom: 15px;">
                    Nouveau message de {name}
                  </h2>
                  
                  <div style="margin-bottom: 25px;">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                      <div style="width: 40px; height: 40px; background: #f0f4ff; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                        📧
                      </div>
                      <div style="margin-left: 15px;">
                        <p style="margin: 0; font-weight: 500; color: #1e293b;">{sender_email}</p>
                      </div>
                    </div>
                    
                    <div style="background: #f8fafc; padding: 20px; border-radius: 8px;">
                      <p style="margin: 0; color: #64748b; line-height: 1.6;">{message}</p>
                    </div>
                  </div>
                </div>
                
                <footer style="text-align: center; margin-top: 30px; color: #94a3b8; font-size: 0.9em;">
                  © 2024 MED-AI | Plateforme d'Intelligence Médicale
                </footer>
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
    """Interface de contact professionnelle"""
    
    # Style CSS personnalisé
    st.markdown("""
    <style>
        :root {
            --primary: #2563eb;
            --secondary: #1e40af;
            --accent: #0891b2;
            --background: #ffffff;
        }
        
        .contact-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .contact-card {
            background: var(--background);
            border-radius: 16px;
            padding: 2.5rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
            border: 1px solid #e2e8f0;
            margin-bottom: 2rem;
        }
        
        .form-input {
            margin-bottom: 2rem;
        }
        
        .form-input label {
            display: block;
            margin-bottom: 0.8rem;
            color: var(--secondary);
            font-weight: 600;
            font-size: 0.95rem;
        }
        
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            border: 2px solid #e2e8f0 !important;
            border-radius: 10px !important;
            padding: 1rem !important;
            transition: all 0.3s !important;
        }
        
        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
        }
        
        .stButton>button {
            background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
            color: white !important;
            border: none !important;
            padding: 1rem 2rem !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: all 0.3s !important;
        }
        
        .contact-info-item {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
            padding: 1.5rem;
            background: #f8fafc;
            border-radius: 12px;
        }
        
        .info-icon {
            font-size: 1.5rem;
            margin-right: 1rem;
            color: var(--primary);
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
        
        # En-tête
        st.markdown("""
        <div style="text-align: center; margin-bottom: 4rem;">
            <h1 style="color: var(--secondary); margin-bottom: 1rem; font-size: 2.5rem;">
                📍 Contact & Support
            </h1>
            <p style="font-size: 1.1rem; color: #64748b;">
                Notre équipe est disponible 24/7 pour répondre à vos questions
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Grille de contact
        col1, col2 = st.columns([2, 1], gap="2rem")
        
        with col1:
            with st.form("contact_form"):
                st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
                
                st.markdown("""
                <div style="margin-bottom: 2rem;">
                    <h2 style="color: var(--secondary); margin-bottom: 1rem;">✉️ Formulaire de Contact</h2>
                    <p style="color: #64748b;">Tous les champs marqués d'un * sont obligatoires</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Formulaire
                name = st.text_input("Nom Complet *", placeholder="Jean Dupont")
                email = st.text_input("Email Professionnel *", placeholder="contact@entreprise.com")
                message = st.text_area("Message *", height=150, placeholder="Décrivez votre demande en détail...")
                
                submitted = st.form_submit_button("Envoyer le Message ➔", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            # Section Informations
            st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
            st.markdown("<h2 style='color: var(--secondary); margin-bottom: 1.5rem;'>📌 Informations</h2>", unsafe_allow_html=True)
            
            # Bloc Adresse
            st.markdown("""
            <div class="contact-info-item">
                <div class="info-icon">🏢</div>
                <div>
                    <h4 style="margin: 0 0 0.5rem; color: var(--secondary);">Siège Social</h4>
                    <p style="margin: 0; color: #64748b; line-height: 1.5;">
                        Tour Médicale, 15ème étage<br>
                        Corniche Ouest, Dakar<br>
                        Sénégal
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Bloc Téléphone
            st.markdown("""
            <div class="contact-info-item">
                <div class="info-icon">📞</div>
                <div>
                    <h4 style="margin: 0 0 0.5rem; color: var(--secondary);">Support Téléphonique</h4>
                    <p style="margin: 0; color: #64748b;">
                        +221 33 800 00 00<br>
                        <span style="font-size: 0.9em;">(24h/24 - 7j/7)</span>
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Bloc Réseaux Sociaux
            st.markdown("""
            <div class="contact-info-item" style="flex-direction: column; align-items: flex-start;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div class="info-icon">🌐</div>
                    <h4 style="margin: 0; color: var(--secondary);">Réseaux Sociaux</h4>
                </div>
                <div style="display: flex; gap: 1rem;">
                    <a href="#" style="color: var(--primary); text-decoration: none; padding: 0.5rem 1rem; border: 1px solid #e2e8f0; border-radius: 8px;">
                        LinkedIn
                    </a>
                    <a href="#" style="color: var(--primary); text-decoration: none; padding: 0.5rem 1rem; border: 1px solid #e2e8f0; border-radius: 8px;">
                        Twitter
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

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

        # Section Carte & FAQ
        tab1, tab2 = st.tabs(["🗺️ Localisation", "❓ FAQ"])
        
        with tab1:
            st.markdown("""
            <div class='contact-card' style="padding: 0; overflow: hidden;">
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3859.227291477752!2d-17.44483768468878!3d14.693534078692495!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xec1725a1bb04215%3A0x9d5f3e9d0e8e4b1e!2sDakar!5e0!3m2!1sfr!2ssn!4v1625060000000!5m2!1sfr!2ssn" 
                    width="100%" 
                    height="400" 
                    style="border:0; border-radius: 16px;" 
                    allowfullscreen="" 
                    loading="lazy">
                </iframe>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
            st.markdown("""
            <h2 style="color: var(--secondary);">Foire aux Questions</h2>
            
            <details style="margin: 1rem 0; border-bottom: 1px solid #e2e8f0; padding-bottom: 1rem;">
                <summary style="font-weight: 600; color: var(--secondary); cursor: pointer;">
                    Quels sont les délais de réponse ?
                </summary>
                <p style="color: #64748b; margin: 0.5rem 0 0; padding-left: 1.5rem;">
                    Nous nous engageons à répondre à toutes les demandes dans un délai maximum de 24 heures.
                </p>
            </details>
            
            <details style="margin: 1rem 0; border-bottom: 1px solid #e2e8f0; padding-bottom: 1rem;">
                <summary style="font-weight: 600; color: var(--secondary); cursor: pointer;">
                    Comment accéder à mon espace client ?
                </summary>
                <p style="color: #64748b; margin: 0.5rem 0 0; padding-left: 1.5rem;">
                    Utilisez les identifiants fournis lors de votre inscription sur notre plateforme.
                </p>
            </details>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    contact()
