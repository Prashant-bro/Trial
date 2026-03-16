# 📈 AlphaPredict – Stock Price Forecasting with Random Forest

AlphaPredict is a financial machine learning project designed to predict **next-day stock closing prices** for high-volatility stocks such as **NVIDIA (NVDA)** and **Tesla (TSLA)** using historical market data and technical indicators.

The system integrates real-time market data from the **Alpaca API** and applies a **Random Forest regression model** to forecast short-term price movements.

---

# 🎯 Project Objective

The goal of this project is to move beyond simple price tracking and apply **Machine Learning** to identify market momentum patterns.

By analyzing **technical indicators such as moving averages, rolling volatility, and trading volume**, the model attempts to predict the **next-day closing price** with high accuracy.

---

# 🛠️ Tech Stack

- **Python** – Core programming language
- **Alpaca API** – Fetching real-time and historical stock market data
- **Scikit-Learn** – Implementing the Random Forest regression model
- **Pandas & NumPy** – Data preprocessing and feature engineering
- **Matplotlib** – Visualizing actual vs predicted price trends

---

# 🧠 Feature Engineering

Instead of using only raw prices, the model generates additional indicators to capture **market trends and sentiment**.

### Technical Indicators Used

- **MA_5, MA_10, MA_20**
  - Short and medium-term moving averages

- **Rolling Volatility**
  - 20-day standard deviation of returns

- **Volume Tracking**
  - Identifying liquidity shifts in the market

- **Next-Day Target**
  - Shifted closing price used for supervised learning

---

# ⚙️ Machine Learning Model

The project uses **Random Forest Regression**, which is an ensemble learning method that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

Model Workflow:

1. Fetch historical stock data using Alpaca API
2. Perform feature engineering
3. Train Random Forest regression model
4. Generate next-day price predictions
5. Compare predicted vs actual prices

---

# 🚀 Performance Snapshot

Example prediction for **NVIDIA (NVDA)**

| Metric | Value |
|------|------|
| Actual Price | $186.94 |
| Predicted Price | $186.91 |
| Variance | 0.05% |

This demonstrates strong short-term forecasting capability using engineered features.

---

# 📊 Visualization

The system also generates plots comparing **actual vs predicted stock prices**.

