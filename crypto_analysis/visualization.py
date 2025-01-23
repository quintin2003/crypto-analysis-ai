# crypto-analysis/visualization.py
import matplotlib.pyplot as plt

def plot_technical_analysis(df, analysis_type, ticker):
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
    
    return fig