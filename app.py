import streamlit as st
import numpy as np
import librosa
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Load the best Random Forest model
best_model = joblib.load("best_model.pkl")  # Ensure best_model.pkl is saved from training

# Emotion Mapping with Icons
emotions = {
    0: ("Neutral", "😐"),
    1: ("Calm", "🧘"),
    2: ("Happy", "😃"),
    3: ("Sad", "😢"),
    4: ("Angry", "😠"),
    5: ("Fearful", "😨"),
    6: ("Disgust", "🤢"),
    7: ("Surprised", "😲")
}

emotion_labels = [emotions[i][0] for i in range(8)]  # Extract emotion names

# Function to extract features for RFC
def extract_features(file):
    X, sample_rate = librosa.load(file, res_type="kaiser_fast")
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
    return np.array(mfccs).reshape(1, -1)  # RFC expects 2D input

# Streamlit UI
st.set_page_config(page_title="🎤 Speech Emotion Recognition", layout="wide")

# Header
st.markdown("<h1 style='text-align: center;'>🎤 Speech Emotion Recognition</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Upload a `.wav` file and let AI detect the emotion!</h3>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("🎵 Choose a `.wav` file", type="wav")

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    # Extract features
    features = extract_features(uploaded_file)

    # Predict emotion using RFC
    predicted_index = best_model.predict(features)[0]
    predicted_emotion, emotion_icon = emotions[predicted_index]

    # Display result
    st.markdown(f"<h2 style='text-align: center;'>🎭 Detected Emotion: {emotion_icon} <b>{predicted_emotion}</b></h2>", unsafe_allow_html=True)

    # Get prediction probabilities
    probabilities = best_model.predict_proba(features)[0]

    # Plot emotion probability distribution
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=emotion_labels, y=probabilities, palette="viridis", ax=ax)
    ax.set_ylabel("Probability", fontsize=12)
    ax.set_title("Emotion Probability Distribution", fontsize=14)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>Built with ❤️ using Streamlit & Scikit-learn</p>", unsafe_allow_html=True)