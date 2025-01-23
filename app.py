import gradio as gr
from datetime import datetime, timedelta
from crypto_analysis.data_loader import load_data, preprocess_data
from crypto_analysis.analysis import analyze_crypto

# -------------------------
# Configuration
# -------------------------
DEFAULT_CRYPTOS = ["BTC-USD", "ETH-USD", "BNB-USD"]
THEME = gr.themes.Soft(
    primary_hue="emerald",
    font=[gr.themes.GoogleFont('Inter'), 'sans-serif']
).set(
    button_shadow="*shadow_drop_lg",
    block_shadow="*shadow_drop_lg"
)

# -------------------------
# Gradio Interface
# -------------------------
def analyze(ticker, analysis_type):
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    df = load_data(ticker, start_date, end_date)
    df = preprocess_data(df)
    fig, summary = analyze_crypto(df, analysis_type)
    return fig, summary

with gr.Blocks(theme=THEME, title="Crypto Analysis Bot") as demo:
    gr.Markdown("# 🚀 Crypto Analysis Bot")
    
    with gr.Row():
        with gr.Column():
            ticker_input = gr.Dropdown(
                label="Select Cryptocurrency",
                choices=DEFAULT_CRYPTOS,
                value="BTC-USD"
            )
            analysis_type = gr.Radio(
                label="Analysis Type",
                choices=["Price Trends", "RSI", "Volume Analysis"],
                value="Price Trends"
            )
            analyze_btn = gr.Button("Analyze", variant="primary")
            
        with gr.Column():
            plot_output = gr.Plot(label="Technical Analysis")
            summary_output = gr.Markdown(label="Latest Metrics")
    
    examples = gr.Examples(
        examples=[["BTC-USD", "Price Trends"], ["ETH-USD", "RSI"]],
        inputs=[ticker_input, analysis_type],
        outputs=[plot_output, summary_output],
        fn=analyze,
        cache_examples=True
    )
    
    analyze_btn.click(
        fn=analyze,
        inputs=[ticker_input, analysis_type],
        outputs=[plot_output, summary_output]
    )

if __name__ == "__main__":
    demo.launch(server_port=7860, share=True)