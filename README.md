# 📈 Stock Price Predictor using Machine Learning

A Machine Learning project that predicts the next day's stock closing price using historical stock market data. The project leverages Python, Scikit-learn, Yahoo Finance API, and Streamlit to build an end-to-end predictive analytics application.

---

## 🚀 Features

* Historical stock data collection using Yahoo Finance
* Data preprocessing and feature engineering
* Machine Learning model training with Random Forest Regression
* Next-day stock price prediction
* Model persistence using Joblib
* Interactive web interface with Streamlit
* Visualization-ready architecture for future enhancements

---

## 🛠️ Tech Stack

### Languages

* Python

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-learn
* yFinance
* Joblib
* Streamlit
* Matplotlib

---

## 📂 Project Structure

```text
Stock-Price-Predictor/
│
├── app.py                 # Streamlit application
├── train.py               # Model training script
├── requirements.txt       # Project dependencies
├── stock_data.csv         # Historical stock data (generated automatically)
├── model.pkl              # Trained ML model (generated automatically)
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/maddy-bit/Stock-Price-Predictor.git
cd Stock-Price-Predictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

Run:

```bash
python train.py
```

This will:

* Download historical stock data
* Train the Random Forest model
* Evaluate model performance
* Generate `model.pkl`

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📊 Machine Learning Workflow

1. Collect historical stock data
2. Clean and preprocess dataset
3. Create prediction target (next day's closing price)
4. Split dataset into training and testing sets
5. Train Random Forest Regression model
6. Evaluate model performance
7. Save trained model
8. Predict future stock prices through Streamlit UI

---

## 📈 Example Input

| Feature     | Example  |
| ----------- | -------- |
| Open Price  | 220      |
| High Price  | 225      |
| Low Price   | 218      |
| Close Price | 223      |
| Volume      | 50000000 |

### Output

```text
Predicted Next Day Price: $224.73
```

---

## 🔮 Future Improvements

* Support multiple stock symbols
* Real-time stock market integration
* LSTM-based deep learning model
* Advanced technical indicators
* Candlestick chart visualization
* Model comparison dashboard
* Deployment on Streamlit Cloud

---

## 🎯 Learning Outcomes

This project demonstrates:

* Data Collection
* Data Preprocessing
* Feature Engineering
* Machine Learning
* Model Evaluation
* Model Deployment
* Data Visualization
* End-to-End ML Pipeline Development

---

## 👨‍💻 Author

Anmol Trivedi

GitHub: https://github.com/maddy-bit

---

## ⭐ If you found this project useful, consider giving it a star.
