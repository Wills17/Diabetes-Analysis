# 🩺 **DiabetesCheck — Machine Learning Web App for Diabetes Prediction**

## 🌟 Overview

**DiabetesCheck** is a Flask-based **machine learning web application** that predicts whether a patient is at risk of diabetes based on health indicators.
It provides a sleek dark-mode interface, supports multiple ML models, and delivers quick, interpretable predictions — all wrapped in a modern, responsive UI.

This app extends the offline Python model pipeline (EDA + Model Training + Cross Validation) into a **deployable web experience** powered by Flask.

---

### 🚀 Live Demo

🔗 **Try it here:** [Live Demo.](https://diabetes-analysis-7ew5.onrender.com)

---

## ⚙️ **Features**

* 🧠 **Multiple Models** — Logistic Regression & K-Nearest Neighbors
* 💡 **User-Friendly Web Interface** — Simple input form with instant results
* 🌙 **Dark Mode** — Elegant and readable design across devices
* ⚕️ **Interactive Prediction** — Enter medical parameters and get real-time predictions
* 🔍 **Model Transparency** — Displays which model made the prediction

---

## 📁 **Project Structure**

```bash
DIABETES-ANALYSIS/
│
├── Dataset/
│   └── diabetes.csv
│
├── EDA on Diabetes/        # Exploratory Data Analysis
│   ├── Box Plots.py
│   ├── Histograms.py
│   ├── Pair Plots.py
│   └── Violin Plots.py
│
├── Input/                  # Test script
│   └── Input.py
│
├── Models/                 # ML models
│   ├── KNN_diabetes_model.pkl
│   └── LR_diabetes_model.pkl
│
├── Overview/
│   └── main.py             # Dataset summary/overview
│
├── Prediction Models/
│   ├── Knn.py
│   └── LogisticRegression.py
│
├── static/                 # Static frontend file
│   └── styles.css
│
├── templates/              # HTML pages
│   ├── home.html
│   ├── predict.html
│   └── result.html
│
├── app.py                  # Flask app entry point
├── requirements.txt        # Dependencies
│
└── README.md
```

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/diabetescheck.git
cd diabetescheck
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app

```bash
python app.py
```

Then open your browser and go to 👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📊 **Dataset**

The model uses the **Pima Indians Diabetes Dataset**, a classic benchmark dataset for medical prediction tasks.
It contains diagnostic measurements like:

* Glucose concentration
* Blood pressure
* BMI
* Insulin level
* Age, pregnancies, etc.

This dataset allows the model to learn risk patterns and generalize across patient data.

---

## 📊 **Exploratory Data Analysis (EDA)**

The EDA scripts under `EDA on Diabetes/` provide visual insights into the dataset:

* `Box Plots.py` — Outlier and spread visualization
* `Histograms.py` — Distribution of variables
* `Pair Plots.py` — Correlation patterns
* `Violin Plots.py` — Density and range comparison

These analyses ensure proper understanding before model training.

---

## 🧪 **Models Used**

| Model                         | Description                            | Strength                |
| ----------------------------- | -------------------------------------- | ----------------------- |
| **Logistic Regression**       | Linear model for binary classification | Fast, interpretable     |
| **K-Nearest Neighbors (KNN)** | Instance-based non-linear model        | Flexible, pattern-aware |

✅ Each model was trained and tested using **cross-validation** for better generalization.

---

## ⚠️ **Disclaimer**

> This application provides **machine learning–based predictions** and is **not a substitute** for professional medical advice, diagnosis, or treatment.
> Always consult a qualified healthcare professional for clinical guidance.

---

## 👨‍💻 **Author**

**Williams Odunayo**
Machine Learning Engineer

🔗 [LinkedIn](https://linkedin.com/in/williams-odunayo)
