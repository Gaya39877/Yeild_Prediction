# Crop Yield Prediction

Welcome to the **Crop Yield Prediction** project! This Flask-based web application predicts crop yield based on various environmental and agricultural factors.

## 🚀 Features
- Predict crop yield using **Machine Learning**
- Flask-based web app with **interactive UI**
- **Dockerized** for easy deployment
- Supports multiple countries and crops

---

## 🛠️ Installation Guide

### 🔹 Prerequisites
Ensure you have the following installed:
- **Python 3.9+**
- **pip** (Python package manager)
- **Docker** (for containerized deployment)

### 🔹 Setup Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/crop-yield-prediction.git
   cd crop-yield-prediction
   ```
2. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask application**
   ```bash
   python app.py
   ```
5. Open your browser and go to: **http://127.0.0.1:5000** 🚀

---

## 🐳 Deploy with Docker

### 🔹 Build and Run the Container
1. **Build the Docker image**
   ```bash
   docker build -t crop-yield-prediction .
   ```
2. **Run the container**
   ```bash
   docker run -p 5000:5000 crop-yield-prediction
   ```
3. **Access the app** at [http://localhost:5000](http://localhost:5000) 🌎

### 🔹 Troubleshooting Docker Issues
❌ **Facing timeout or image pull errors?**
   - Check your internet connection 🌍
   - Try `docker logout` and retry building
   - Restart Docker 🐳

❌ **Version mismatch errors?**
   - Ensure `scikit-learn` versions match between training and deployment
   - Reinstall dependencies with `pip install --upgrade -r requirements.txt`

---

## 🧠 How It Works
1. **User Inputs Data** (Year, Rainfall, Pesticides, Temperature, Area, Crop Type)
2. **Data Preprocessing** (Using Scikit-learn transformers)
3. **Machine Learning Model (Decision Tree Regressor)** predicts yield
4. **Results displayed** on the web app 📊

---

## 📌 Future Enhancements
✅ Improve model accuracy with **advanced ML algorithms**
✅ Add **real-time weather data integration**
✅ Deploy on **cloud platforms (AWS, Azure, GCP)**

---

## 👥 Contributors
💡 **Your Name** – *Developer & Maintainer*
📧 Contact:gayathrirasangikahw@gmail.com
---

## ⭐ Support & Feedback
If you find this project useful, give it a ⭐ on GitHub! 🎉

**Got suggestions?** Feel free to open an issue or reach out! 🚀

