import pandas as pd
import yfinance as yf
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Download stock data
df = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2025-01-01"
)

# Keep required columns
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# Target column
df['Tomorrow'] = df['Close'].shift(-1)

# Remove null row
df.dropna(inplace=True)

# Features and target
X = df[['Open', 'High', 'Low', 'Close', 'Volume']]
y = df['Tomorrow']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", mae)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully.")