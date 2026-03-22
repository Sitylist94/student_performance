# 🎓 Student Performance Prediction

Predict the final grade (G3) of students using Machine Learning, based on the [UCI Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance).

---

## 📊 Dataset

- **Source** : UCI Machine Learning Repository
- **Taille** : 395 élèves × 33 features
- **Target** : `G3` — note finale (0-20)
- **Features** : caractéristiques socio-démographiques, notes intermédiaires (G1, G2), habitudes de vie

---

## 🚀 Résultats

| Modèle | R² | MAE |
|---|---|---|
| 🥇 AdaBoost (tuné) | **0.897** | 1.01 |
| 🥈 XGBoost | 0.883 | 0.96 |
| 🥉 Random Forest | 0.882 | 0.97 |

> Modèle final : **AdaBoost Regressor** — entraîné avec PyCaret

---

## 🔍 Feature Importance (SHAP)

Les variables les plus influentes sur la note finale :

1. **G2** — note du 2ème trimestre (impact majeur)
2. **Absences** — les absences dégradent significativement G3
3. **Age** — les élèves plus âgés (souvent redoublants) ont de moins bons résultats
4. **G1** — note du 1er trimestre

> Les features socio-démographiques seules (sans G1/G2) donnent un R² ≈ 0.26, ce qui confirme que les notes passées sont les meilleurs prédicteurs.

---

## 🛠️ Stack technique

- Python 3.11
- PyCaret 3.x
- scikit-learn
- XGBoost
- SHAP
- pandas / matplotlib

---

## ⚙️ Installation

```bash
# Cloner le repo
git clone https://github.com/Sitylist94/student_performance.git
cd student_performance

# Créer un environnement virtuel
python -m venv .venv
.venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

---

## ▶️ Utilisation

Ajouter le dataset dans le dossier `data/` :
```
data/student_data.csv
```

Lancer le script :
```bash
python main.py
```

Cela va :
1. Comparer automatiquement 17 modèles de régression
2. Tuner les 3 meilleurs (AdaBoost, XGBoost, Random Forest)
3. Générer les graphiques SHAP et feature importance
4. Sauvegarder le modèle final

---

## 📁 Structure du projet

```
student_performance/
├── data/               # Dataset (non inclus)
├── figure/             # Graphiques générés
├── model/              # Modèle sauvegardé
├── main.py             # Script principal
├── requirements.txt
└── README.md
```

---

## 👤 Auteur

**Adam Bara** — [Sitylist94](https://github.com/Sitylist94)