
# Algerian Forest Fire Prediction 🔥🌲

This is a machine learning web application built with **Flask** to predict the **Fire Weather Index** (FWI) using environmental features from the **Algerian Forest Fire dataset**.

---

## 🚀 Project Overview

The goal of this project is to build a regression model that predicts the severity of forest fires based on features like temperature, humidity, wind, rain, and other fire indices (FFMC, DMC, DC, ISI). The model is deployed via a web interface using Flask.

---

## 📁 Project Structure

```
├── model/
│   ├── ridge.pkl          # Trained Ridge Regression model
│   └── scalar.pkl         # StandardScaler used during training
├── templates/
│   ├── index.html         # Input form page
│   └── home.html          # Result display page
├── application.py         # Flask backend application
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## 🧠 Machine Learning

- **Algorithm Used**: Ridge Regression
- **Preprocessing**: StandardScaler
- **Target Variable**: Fire Weather Index (FWI)

---

## 🌐 Web Interface

- Users enter environmental parameters via a simple HTML form.
- The input is passed to a Flask backend.
- The model predicts and returns the FWI value.

---

## 🛠️ How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Algerian-Forest-Fire-Prediction-.git
cd Algerian-Forest-Fire-Prediction-
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Flask app**

```bash
python application.py
```

4. Open your browser and go to: `http://127.0.0.1:5000/`

---

## 🧪 Sample Input Parameters

- Temperature
- Relative Humidity
- Wind Speed
- Rain
- FFMC Index
- DMC Index
- DC Index
- ISI Index
- Classes (1 = fire, 0 = no fire)

---

## 📊 Dataset Source

- The cleaned dataset used in this project is based on the [Algerian Forest Fire dataset](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset).

---

## 🙌 Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [Flask](https://flask.palletsprojects.com/)
- Algerian Forest Fire Dataset Contributors

---

## ✍️ Author

**Prathmesh Wavhal**  
[GitHub Profile](https://github.com/PW-5214)
