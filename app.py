import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords', quiet=True)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #fffbea;
    color: #333333;
}

/* Header */
.header {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #f4b400;
    margin-bottom: 25px;
}

/* Text Area */
textarea {
    background-color: #fff3cd !important;
    color: #333 !important;
    border-radius: 10px !important;
    border: 1px solid #f4b400 !important;
}

/* Button */
.stButton button {
    background-color: #f4b400;
    color: black;
    border-radius: 10px;
    padding: 10px 25px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #d39e00;
    color: white;
}

/* Result Box */
.result-box {
    padding: 15px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: gray;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">🛒 Flipkart Review Sentiment Analyzer</div>', unsafe_allow_html=True)

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', str(text))
    text = text.lower()
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)

review = st.text_area("Enter your review:")

if st.button("Analyze"):
    clean = clean_text(review)
    vector = vectorizer.transform([clean])
    prediction = model.predict(vector)[0]
    proba = model.predict_proba(vector)[0]

    confidence = round(max(proba) * 100, 2)

    if prediction == "positive":
        st.markdown(f'<div class="result-box" style="background-color:#d4edda; color:#155724;">😊 Positive Review <br> Confidence: {confidence}%</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="result-box" style="background-color:#f8d7da; color:#721c24;">😡 Negative Review <br> Confidence: {confidence}%</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Built by Chidvilas 🚀 | AI Sentiment Analysis Project</div>', unsafe_allow_html=True)