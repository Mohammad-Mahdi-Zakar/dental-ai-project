# 🦷 Dental Caries Detection AI Assistant

An end-to-end Deep Learning project designed to detect dental tooth decay from X-ray and clinical images with high precision. This project demonstrates a full AI lifecycle: from model training to cloud deployment.

## 🚀 Live Demo
Check out the interactive web application here:
**(https://mohammad-mahdi-zakar-dental-caries-final.hf.space)**

---

## 📊 Project Highlights
* **Model Accuracy:** Achieved a stellar **97.6% accuracy** on the test dataset.
* **Core Technology:** Built using **TensorFlow/Keras** for the deep learning backbone (CNN).
* **Deployment:** * **Frontend:** Interactive UI built with **Gradio** for real-time inference.
    * **Backend Support:** Successfully implemented and tested with **FastAPI** for high-performance API logging and request tracking.
    * **Hosting:** Deployed on **Hugging Face Spaces**.

---

## 🛠️ Technical Stack
* **Deep Learning:** TensorFlow, Keras (CNN Architecture)
* **Data Processing:** Pandas, NumPy, PIL (Pillow)
* **Web Frameworks:** Gradio (Current UI), FastAPI (Backend Logic)
* **Database:** SQLite (Used for logging inference history during testing)
* **Version Control:** Git & GitHub

---

## 🔍 How It Works
1.  **Image Pre-processing:** Every uploaded image is automatically converted to **RGB** and resized to **224x224** to ensure consistency across different image formats (PNG, JPG, Grayscale X-rays).
2.  **Inference:** The model predicts the probability of dental caries.
3.  **Real-time Results:** The UI displays a professional **Label view** with confidence scores for both "Healthy" and "Caries Detected" classes.

---

### 🛠️ Challenges & Technical Evolution (The "War Stories")
Building this wasn't easy. I faced several critical issues that required deep troubleshooting:

**The Accuracy Plateau & Data Quality**: Initially, the model's accuracy was stuck and wouldn't improve. I realized the original dataset had inconsistent labeling and low-quality X-rays. I pivoted by performing a complete data audit, cleaning the noise, and integrating a higher-quality, balanced dataset to ensure the model actually learned features instead of just memorizing patterns.

**The Preprocessing Pivot**: One of the biggest hurdles was handling the diverse formats of medical X-rays. I had to build a custom Preprocessing Pipeline that standardized image intensity and resized inputs without losing the fine details of the dental caries. This step was the turning point for the model's performance.

**Architectural Fine-Tuning**: Moving beyond a basic CNN, I experimented with different layer depths and activation functions to find the "Sweet Spot" that could handle the subtle textures of X-ray images. This optimization was crucial for achieving high precision in detecting early-stage caries.

---

## 🖼️ Application Interface
Below is a look at the final working application in action:

![Dental AI Screenshot](screenshot.png)

---

## 📁 Project Structure
```bash
├── app/
│   └── app.py              # Main Gradio application script
├── notebooks/
│   └── Training.ipynb      # Model training & evaluation (97% Accuracy)
├── dental_caries_model_v2.h5 # Trained TensorFlow model
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

---

## 👨‍💻 Developed By
**Mohammad Mahdi Zakar** *Junior Data Scientist | AI Specialist* "Building AI that solves real problems, one bug at a time."