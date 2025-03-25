# D-ploiement

```markdown
# MOYO - Plateforme d'Aide à la Décision pour l'Estimation de la Survie des Patients Atteints du Cancer Gastrique

MOYO est une application interactive développée avec Streamlit, permettant l'estimation du temps de survie post-traitement des patients atteints du cancer gastrique. Elle intègre plusieurs modèles de prédiction basés sur l'apprentissage statistique et profond.

---

## 🚀 Fonctionnalités

✅ **Analyse descriptive des données**  
✅ **Prédiction du temps de survie à l'aide de plusieurs modèles**  
✅ **Stockage et gestion des informations des patients**  
✅ **Visualisation interactive avec Plotly**  
✅ **Interface intuitive avec Streamlit**

---

## 📌 Technologies Utilisées

- **Python** 🐍
- **Streamlit** - Interface utilisateur interactive  
- **TensorFlow / Keras** - Modèle *DeepSurv*  
- **Lifelines** - Modèle *Cox Proportionnel des Risques*  
- **Scikit-learn** - Modèles Random Survival Forest (*RSF*) et Gradient Boosting Survival Trees (*GBST*)  
- **Pandas & NumPy** - Manipulation des données  
- **Plotly** - Visualisation interactive  

---

## 📂 Structure du Projet

```
📁 moyo/
│── 📁 assets/               # Images et logos  
│── 📁 data/                 # Fichiers de données  
│── 📁 models/               # Modèles pré-entraînés  
│── 📁 pages/                # Modules de navigation  
│── main.py                  # Fichier principal de l'application  
│── requirements.txt         # Liste des dépendances  
│── README.md                # Documentation  
```

---

## ⚙️ Installation et Exécution

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/votre-repository/moyo.git
cd moyo
```

### 2️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application
```bash
streamlit run main.py
```

---

## 🧠 Modèles de Prédiction Utilisés

| Modèle        | Description |
|--------------|------------|
| **Cox PH**   | Modèle de régression de Cox Proportionnel des Risques (*Lifelines*) |
| **RSF**      | Random Survival Forest (*Scikit-learn*) |
| **DeepSurv** | Réseau de neurones profond (*TensorFlow/Keras*) |
| **GBST**     | Gradient Boosting Survival Trees (*Scikit-learn*) |

---

## 👥 Équipe du Projet

- **Pr. Aba Diop** - Maître de Conférences  
- **PhD. Idrissa Sy** - Enseignant Chercheur  
- **M. Ahmed Sefdine** - Étudiant  

📧 Contact : [ahmed.sefdine@uadb.edu.sn](mailto:ahmed.sefdine@uadb.edu.sn)

---

## 📜 Licence

Projet académique réalisé dans le cadre d'un mémoire de fin d'études en **Statistique et Informatique Décisionnelle**.

---

🔗 **Liens utiles**  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Lifelines Survival Analysis](https://lifelines.readthedocs.io/)  
- [TensorFlow & Keras](https://www.tensorflow.org/)  
```
