# 🎤 Speech Emotion Recognition (SER)

## 📌 Project Overview
Speech Emotion Recognition (SER) is a machine learning project that identifies emotions from speech signals. This project evaluates multiple models (**CNN, KNN, SVC, RFC, DTC**) and selects the **best-performing model** dynamically based on accuracy. The chosen model is then saved as a `.pkl` file for efficient deployment.

## 🚀 Live Demo
🔗 **Try it here:** [Speech Emotion Recognition Web App](https://speech-emotion-recognition-using-various-datasets-qu3ptjnsb7gs.streamlit.app/)

## 🏗️ Features

- ✅ **Multiple Model Training**: Compares various models (**CNN, KNN, SVC, RFC, DTC**) and selects the best one.
- ✅ **Pretrained Model Deployment**: Uses the best model (`best_model.pkl`) for real-time predictions.
- ✅ **Audio Upload**: Upload a `.wav` file for analysis.
- ✅ **Emotion Prediction**: Detects emotions like **Happy, Sad, Angry, Neutral, etc.**
- ✅ **Interactive UI**: Built using **Streamlit** for an easy-to-use interface.
- ✅ **Visualization**: Displays **prediction probabilities** in a bar chart.

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

- 🎭 **[RAVDESS](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)**
- 📢 **[TESS](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess?resource=download)**

## 🔍 Model Training & Selection
- Multiple models (**CNN, KNN, SVC, RFC, DTC**) are trained and evaluated.
- The best model is selected dynamically based on **highest accuracy**.
- The best model is saved as **`best_model.pkl`** for future predictions.

### 📊 Running Model Training
```sh
python train.py --epochs 50 --batch_size 32
```

## 🎤 Running the Streamlit App
Once installed, you can launch the **interactive web application**:
```sh
streamlit run app.py
```

### 🌟 Web App Features
- Upload and play `.wav` audio files.
- Predict emotions in **real-time** using the best model.
- Display **probability distribution** of emotions.
- Show **emoji-based emotion visualization** 😃😢😠.

## 📊 Model Performance & Evaluation
- The **best model** is selected based on accuracy.
- Performance is evaluated using:
  - ✅ **Confusion Matrix**
  - ✅ **Classification Report**
  - ✅ **Accuracy Score**
- The final model is saved as **`best_model.pkl`** for deployment.

## 📜 References & Resources
- 🎵 **[Librosa Documentation](https://librosa.org/doc/latest/)**
- 🔬 **[TensorFlow/Keras](https://www.tensorflow.org/)**
- 🏗 **[Streamlit](https://streamlit.io/)**

## 🤝 Contributing
Feel free to fork this repo and contribute to improving the **SER model & UI**!

---

Built with ❤️ using **Python, TensorFlow & Streamlit** 🚀
