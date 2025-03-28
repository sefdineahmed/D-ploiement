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
              .container {{ max-width: 800px; margin: 20px auto; background: #ffffff; }}
              .header {{ background: #2e77d0; padding: 30px; color: white; border-radius: 15px 15px 0 0; }}
              .content {{ padding: 30px; color: #444; }}
              .message-box {{ background: #f8f9fa; border-radius: 10px; padding: 20px; margin: 20px 0; }}
              .footer {{ background: #1d5ba6; color: white; padding: 15px; text-align: center; border-radius: 0 0 15px 15px; }}
            </style>
          </head>
          <body>
            <div class="container">
              <div class="header">
                <h1>Nouveau message de {name}</h1>
                <p>Plateforme MED-AI - Contact</p>
              </div>
              <div class="content">
                <h3>📬 Informations de contact</h3>
                <p><strong>Email :</strong> {sender_email}</p>
                <div class="message-box">
                  <h4>📝 Message :</h4>
                  <p>{message}</p>
                </div>
              </div>
              <div class="footer">
                <p>© 2024 MED-AI | Tous droits réservés</p>
                <p>Cet email a été généré automatiquement</p>
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
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        
        .contact-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .contact-card {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(46, 119, 208, 0.15);
            transition: transform 0.3s ease;
        }
        
        .contact-card:hover {
            transform: translateY(-5px);
        }
        
        .form-input {
            margin-bottom: 2rem;
        }
        
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            border: 2px solid #e9ecef !important;
            border-radius: 12px !important;
            padding: 1rem !important;
            font-size: 1rem !important;
        }
        
        .stButton>button {
            background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
            color: white !important;
            border: none !important;
            padding: 1.2rem 2.5rem !important;
            border-radius: 12px !important;
            font-size: 1.1rem !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        
        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 20px rgba(46, 119, 208, 0.3) !important;
        }
        
        .success-message {
            background: #f0f9ff;
            border-left: 4px solid var(--primary);
            padding: 2rem;
            border-radius: 12px;
            margin: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
        
        # En-tête
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
            <div style="padding-right: 3rem;">
                <h1 style="color: var(--primary); margin-bottom: 1.5rem; font-size: 2.8rem;">
                    📍 Contactez Notre Équipe Médicale
                </h1>
                <p style="font-size: 1.1rem; color: #666; line-height: 1.6;">
                    Notre équipe d'experts est à votre disposition pour répondre à toutes 
                    vos questions concernant nos services médicaux et solutions innovantes.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.image("https://via.placeholder.com/400x250.png?text=Medical+Team", use_column_width=True)

        st.markdown("---")

        # Grille de contact
        col_form, col_info = st.columns([2, 1])
        
        with col_form:
            with st.form("contact_form"):
                st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
                
                st.markdown("""
                <h3 style="color: var(--primary); margin-bottom: 2rem;">
                    ✉️ Formulaire de Contact
                </h3>
                """, unsafe_allow_html=True)
                
                name = st.text_input("Nom Complet *", placeholder="Dr. Jean Dupont")
                email = st.text_input("Email Professionnel *", placeholder="contact@clinique.com")
                message = st.text_area("Message *", height=200, 
                                     placeholder="Décrivez votre demande en détail...")
                
                submitted = st.form_submit_button("Envoyer le Message 🚀")
                st.markdown("</div>", unsafe_allow_html=True)

        with col_info:
            st.markdown("""
            <div class='contact-card' style="padding: 2rem;">
                <h3 style="color: var(--primary); margin-bottom: 1.5rem;">📌 Coordonnées</h3>
                
                <div style="margin-bottom: 2rem;">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                        <div style="font-size: 2rem;">🏥</div>
                        <div>
                            <h4 style="margin: 0; color: var(--secondary);">Adresse Clinique</h4>
                            <p style="margin: 0.5rem 0 0; color: #666;">
                                Tour Médicale, 15ème étage<br>
                                Corniche Ouest, Dakar<br>
                                Sénégal
                            </p>
                        </div>
                    </div>
                    
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                        <div style="font-size: 2rem;">📞</div>
                        <div>
                            <h4 style="margin: 0; color: var(--secondary);">Support Téléphonique</h4>
                            <p style="margin: 0.5rem 0 0; color: #666;">
                                +221 33 800 70 70<br>
                                Disponible 24h/24
                            </p>
                        </div>
                    </div>
                    
                    <div style="border-top: 2px solid #eee; padding-top: 1.5rem;">
                        <h4 style="color: var(--secondary); margin-bottom: 1rem;">🔗 Réseaux Sociaux</h4>
                        <div style="display: flex; gap: 1.5rem; font-size: 1.8rem;">
                            <a href="#" style="color: var(--primary);">🌐</a>
                            <a href="#" style="color: var(--primary);">💼</a>
                            <a href="#" style="color: var(--primary);">📘</a>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Traitement du formulaire
        if submitted:
            if not all([name, email, message]):
                st.error("🚨 Veuillez remplir tous les champs obligatoires (*)")
            elif not validate_email(email):
                st.error("📧 Format d'email invalide")
            else:
                with st.spinner("Envoi en cours..."):
                    if send_email(name, email, message):
                        st.markdown("""
                        <div class='success-message'>
                            <div style="display: flex; align-items: center; gap: 1rem;">
                                <div style="font-size: 2.5rem;">🎉</div>
                                <div>
                                    <h3 style="margin: 0; color: var(--primary);">Message envoyé avec succès !</h3>
                                    <p style="margin: 0.5rem 0 0; color: #666;">
                                        Nous vous répondrons dans les plus brefs délais.
                                    </p>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()

        # Section Carte & FAQ
        st.markdown("---")
        
        tab1, tab2 = st.tabs(["🗺️ Localisation", "❓ FAQ"])
        
        with tab1:
            st.markdown("""
            <div class='contact-card' style="padding: 0; overflow: hidden;">
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3859.227291477752!2d-17.44483768468878!3d14.693534078692495!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xec1725a1bb04215%3A0x9d5f3e9d0e8e4b1e!2sDakar!5e0!3m2!1sfr!2ssn!4v1625060000000!5m2!1sfr!2ssn" 
                    width="100%" 
                    height="400" 
                    style="border:0; border-radius: 0 0 20px 20px;" 
                    allowfullscreen="" 
                    loading="lazy">
                </iframe>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            with st.expander("Quels sont les horaires de consultation ?"):
                st.markdown("""
                - **Lundi à Vendredi** : 8h - 20h  
                - **Samedi** : 9h - 13h  
                - **Urgences** : 24h/24
                """)
            
            with st.expander("Comment préparer ma première visite ?"):
                st.markdown("""
                - Carte d'identité  
                - Ordonnances récentes  
                - Résultats d'examens  
                - Carte vitale (si applicable)
                """)
            
            with st.expander("Quelles assurances acceptez-vous ?"):
                st.markdown("""
                - Toutes assurances privées  
                - CMU (Couverture Maladie Universelle)  
                - Prise en charge internationale
                """)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    contact()
