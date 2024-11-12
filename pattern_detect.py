import talib
import yfinance as yf

# Download data
data = yf.download("^NSEBANK", start="2020-01-01", end="2020-08-01")
# Convert DataFrame columns to numpy arrays
open_prices = data['Open'].values.flatten()
high_prices = data['High'].values.flatten()
low_prices = data['Low'].values.flatten()
close_prices = data['Close'].values.flatten()
# Apply TA-Lib functions
morning_star = talib.CDLMORNINGSTAR(open_prices, high_prices, low_prices, close_prices)
engulfing = talib.CDLENGULFING(open_prices, high_prices, low_prices, close_prices)

data['Morning Star'] = morning_star
data['Engulfing'] = engulfing

engulfing_days = data[data['Engulfing'] != 0]
morning_star_days = data[data['Morning Star'] != 0]

#Display the result
print(engulfing_days)
print(morning_star_days)
