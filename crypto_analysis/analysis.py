# crypto-analysis/analysis.py
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def fetch_crypto_data(ticker, days=365):
    """Fetch historical crypto data from Yahoo Finance"""
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    
    df = yf.download(
        ticker,
        start=start_date.strftime('%Y-%m-%d'),
        end=end_date.strftime('%Y-%m-%d'),
        progress=False
    )
    return df

def calculate_technical_indicators(df):
    """Add common crypto trading indicators"""
    # Moving Averages
    df['MA_7'] = df['Close'].rolling(window=7).mean()
    df['MA_30'] = df['Close'].rolling(window=30).mean()
    
    # RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # Bollinger Bands
    df['20MA'] = df['Close'].rolling(window=20).mean()
    df['20STD'] = df['Close'].rolling(window=20).std()
    df['Upper Band'] = df['20MA'] + (df['20STD'] * 2)
    df['Lower Band'] = df['20MA'] - (df['20STD'] * 2)
    
    return df.dropna()

def analyze_crypto(ticker, analysis_type):
    """Main analysis function"""
    df = fetch_crypto_data(ticker)
    df = calculate_technical_indicators(df)
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if analysis_type == "Price Trends":
        ax.plot(df.index, df['Close'], label='Price')
        ax.plot(df.index, df['MA_7'], label='7-Day MA')
        ax.plot(df.index, df['MA_30'], label='30-Day MA')
        ax.set_title(f'{ticker} Price Analysis')
        
    elif analysis_type == "RSI":
        ax.plot(df.index, df['RSI'], label='RSI', color='purple')
        ax.axhline(70, linestyle='--', color='red', alpha=0.5)
        ax.axhline(30, linestyle='--', color='green', alpha=0.5)
        ax.set_title(f'{ticker} Relative Strength Index')
        ax.set_ylim(0, 100)
        
    elif analysis_type == "Volume Analysis":
        ax.bar(df.index, df['Volume'], color='skyblue', alpha=0.6)
        ax.set_title(f'{ticker} Trading Volume')
        
    ax.legend()
    plt.tight_layout()
    
    # Generate summary stats
    latest = df.iloc[-1]
    summary = f"""
    **Latest Data ({datetime.today().strftime('%Y-%m-%d')})**
    - Price: ${latest['Close']:.2f}
    - 24h Change: {latest['Close'] - latest['Open']:.2f} USD
    - RSI: {latest['RSI']:.1f} ({'Overbought' if latest['RSI'] > 70 else 'Oversold' if latest['RSI'] < 30 else 'Neutral'})
    - Volume: {latest['Volume']:,.0f}
    """
    
    return fig, summary