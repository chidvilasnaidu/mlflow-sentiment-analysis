# 🚀 Sentiment Analysis with MLflow Tracking

## 📌 Project Overview
This project performs **Sentiment Analysis** on customer reviews using multiple Machine Learning models.  
It integrates **MLflow** for experiment tracking, model comparison, and model management.

---

## 🎯 Objectives
- Perform text preprocessing on review data  
- Train multiple ML models  
- Track experiments using MLflow  
- Compare model performance  
- Register the best model  

---

## 🧠 Models Used
- Logistic Regression  
- Naive Bayes  
- K-Nearest Neighbors (KNN)  
- Decision Tree  
- Random Forest  
- Support Vector Machine (SVC)  

---

## ⚙️ Tech Stack
- Python 🐍  
- Scikit-learn  
- Pandas, NumPy  
- NLTK (Text preprocessing)  
- MLflow (Experiment Tracking)  
- Streamlit (Deployment - optional)  

---

## 🔄 Workflow

Data Collection
- → Text Preprocessing
- → Feature Engineering (TF-IDF)
→ Model Training
→ MLflow Tracking
→ Model Comparison
→ Best Model Selection
→ Model Registration 


📁 Sentiment-Analysis
│
├── Sentiment-Analysis.ipynb
├── main.py (Streamlit App)
├── requirements.txt
├── screenshots/
│   ├── runs.png
│   ├── comparison.png
│   ├── model_registry.png
│
└── README.md

## 🚀 How to Run the Project

### 🔹 Step 1: Clone the Repository
git clone https://github.com/your-username/sentiment-analysis-mlflow.git
cd sentiment-analysis-mlflow

---

### 🔹 Step 2: Create Virtual Environment (Optional but Recommended)
conda create -n sentiment_env python=3.10
conda activate sentiment_env

---

### 🔹 Step 3: Install Dependencies
pip install -r requirements.txt

---

### 🔹 Step 4: Download NLTK Resources
Open Python or Jupyter and run:
import nltk
nltk.download('stopwords')
nltk.download('punkt')

---

### 🔹 Step 5: Start MLflow UI
mlflow ui

Open in browser:
http://localhost:5000

---

### 🔹 Step 6: Run the Notebook
jupyter notebook

Open and run:
Sentiment-Analysis.ipynb

---

### 🔹 Step 7: (Optional) Run Streamlit App
streamlit run main.py

---

## ✅ Output
- MLflow dashboard shows:
  - Experiment runs  
  - Model comparison  
  - Metrics & parameters  
- Streamlit app provides sentiment prediction UI

---

## 🔥 Note
Replace `your-username` with your actual GitHub username.
