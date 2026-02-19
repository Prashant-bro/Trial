import matplotlib.pyplot as plt  
import os 
from datetime import datetime
from dotenv import load_dotenv
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from sklearn.ensemble import RandomForestRegressor as RF
from sklearn.model_selection import train_test_split 
load_dotenv()
API_KEY = os.getenv("KEY")
API_SECRET = os.getenv("SECRET")
SYMBOL = "NVDA"
START_DATE ="2021-01-01"
END_DATE= datetime.now().strftime("%Y-%m-%d")
client= StockHistoricalDataClient(API_KEY, API_SECRET)
request_params = StockBarsRequest(
    symbol_or_symbols=SYMBOL,
    timeframe=TimeFrame.Day,
    start=START_DATE,
    end=END_DATE,
)
bars=client.get_stock_bars(request_params)
df=bars.df.reset_index()
df=df[df["symbol"]==SYMBOL]
df["return"] = df["close"].pct_change()
df["volatility"] = df["return"].rolling(window=20).std()
df["ma_5"]= df["close"].rolling(window=5).mean()
df["ma_10"]= df["close"].rolling(window=10).mean()
df["ma_20"]= df["close"].rolling(window=20).mean()
df["target"] = df["close"].shift(-1)
df = df.dropna()
features=["close","volume", "volatility", "ma_5", "ma_10", "ma_20"]
X=df[features]
y=df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
model= RF(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
plt.figure(figsize=(12,6))
plt.plot(y_test.values,label="Actual Price", color="blue")
plt.plot(y_pred,label="Predicted Price", color="orange")
plt.title(f"{SYMBOL} Stock Price Prediction")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()
current_data= X.iloc[-1:].values
predicted_price = model.predict(current_data)[0]
print(f"Predicted Next Day  price for {SYMBOL}: ${predicted_price:.2f}")