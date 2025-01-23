import pandas as pd
import yfinance as yf

def load_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    return df

def preprocess_data(df):
    df['Date'] = pd.to_datetime(df.index)
    df.set_index('Date', inplace=True)
    df = df[['Close', 'Volume']]
    return df