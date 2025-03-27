# 🎤 Speech Emotion Recognition (SER)

## 📌 Project Overview

Speech Emotion Recognition (SER) is a machine learning project that identifies emotions from speech signals. This project utilizes a **pretrained CNN model** to classify emotions such as **happy, sad, angry, neutral**, etc., based on audio features extracted from speech samples.

## 🏗️ Features

✅ **Pretrained Model**: No need for retraining; directly classify emotions.
✅ **Audio Upload**: Upload a `.wav` file for analysis.
✅ **Emotion Prediction**: Detects emotions like **Happy, Sad, Angry, etc.**
✅ **Interactive UI**: Built using **Streamlit** for ease of use.
✅ **Visualization**: Displays prediction probabilities in a bar chart.

## 🚀 Installation Guide

### 🔹 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/speech-emotion-recog.git
cd speech-emotion-recog
```

### 🔹 2️⃣ Create a Virtual Environment

```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate on Linux/Mac
venv\Scripts\activate  # Activate on Windows
```

### 🔹 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

## 🗂️ Dataset (For Reference)

This project uses **preprocessed datasets** stored in `X.joblib` and `y.joblib`. If you want to train your own model, you can use datasets like:

- 🎭 **[RAVDESS](https://zenodo.org/record/1188976)**
- 🎙️ **CREMA-D**
- 📢 **TESS**
- 🔊 **SAVEE**

## 🎤 Running the Streamlit App

Once installed, you can launch the **interactive web application**:

```sh
streamlit run app.py
```

### 🌟 Web App Features

- Upload and play `.wav` audio files.
- Predict emotions in **real-time**.
- Display **probability distribution** of emotions.
- Show **emoji-based emotion visualization** 😃😢😠.

## 📊 Model Performance & Evaluation

- The best model is selected dynamically based on accuracy.
- Uses **Confusion Matrix** and **Classification Report** for evaluation.
- The **trained CNN model** (`testing10_model.h5`) is used for predictions.

## 📜 References & Resources

- 🎵 **[Librosa Documentation](https://librosa.org/doc/latest/)**
- 🔬 **[TensorFlow/Keras](https://www.tensorflow.org/)**
- 🏗 **[Streamlit](https://streamlit.io/)**

## 🤝 Contributing

Feel free to fork this repo and contribute to improving the **SER model & UI**!

---

Built with ❤️ using **Python, TensorFlow & Streamlit** 🚀
