# 📈 AlphaPredict Stock Price Forecasting with Random Forest

AlphaPredict is a financial machine learning project designed to predict the next-day closing prices of high-volatility stocks like NVIDIA (NVDA) and Tesla (TSLA) using historical market data and technical indicators.

---

## 🎯 Project Objective
The goal is to move beyond simple price tracking and utilize Machine Learning (Random Forest) to identify momentum patterns. By analyzing rolling volatility and multiple moving averages, the model attempts to forecast short-term price movements with high precision.

## 🛠️ Technical Stack
- Python Core programming language.
- Alpaca API Real-time and historical market data ingestion.
- Scikit-Learn Implementing the Random Forest Regressor.
- Pandas & NumPy Data cleaning, feature engineering, and matrix operations.
- Matplotlib Visualizing actual vs. predicted price trends.

## 🧠 Model Features
The model doesn't just look at the price; it engineers features to understand market sentiment and trend
- MA_5, MA_10, MA_20 Short and medium-term Moving Averages.
- Rolling Volatility 20-day standard deviation of returns.
- Volume Tracking Analyzing liquidity shifts.
- Next-Day Target The shifted closing price used for supervised learning.

---

## 🚀 Performance Snapshot
In recent tests on NVDA, the model achieved remarkable accuracy
- Actual Price $186.94
- Predicted Price $186.91
- Variance  0.05%

## 📂 Installation & Usage

1. Clone the repository
   ```bash
   git clone [https://github.com/Prashant-bro/Trial]