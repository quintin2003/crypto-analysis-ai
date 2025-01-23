# examples/example_usage.py
from crypto_analysis import fetch_crypto_data, calculate_technical_indicators, plot_technical_analysis

ticker = "BTC-USD"
df = fetch_crypto_data(ticker)
df = calculate_technical_indicators(df)
fig = plot_technical_analysis(df, "Price Trends", ticker)
fig.show()