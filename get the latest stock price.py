import yfinance as yf

# Define the stock ticker symbol
ticker = "TCS.NS"

# Get the latest stock market data for the specified stock
stock_data = yf.Ticker(ticker)

# Get the stock price and other relevant information
stock_info = stock_data.info
stock_name = stock_info['longName']
stock_exchange = stock_info['exchange']
previous_close = stock_info['regularMarketPreviousClose']
opening_price = stock_info['regularMarketOpen']
previous_high = stock_info['regularMarketDayHigh']
previous_low = stock_info['regularMarketDayLow']
previous_volume = stock_info['regularMarketVolume']

# Print the results
print(f"The latest stock market data for {stock_name} ({ticker}) on the {stock_exchange} exchange is:")
for i in range(0,500):
    print("The"+ str(i) +"Time")
    print(f"Previous close price = {previous_close}")
    print(f"Previous open price = {opening_price}")
    print(f"Previous high value = {previous_high}")
    print(f"Previous low value = {previous_low}")
    print(f"Previous volume = {previous_volume}")

print("End")