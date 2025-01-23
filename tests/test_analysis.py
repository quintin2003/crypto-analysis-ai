# tests/test_analysis.py
import unittest
from crypto_analysis import fetch_crypto_data, calculate_technical_indicators

class TestAnalysis(unittest.TestCase):
    def test_fetch_crypto_data(self):
        df = fetch_crypto_data("BTC-USD", days=30)
        self.assertFalse(df.empty)
    
    def test_calculate_technical_indicators(self):
        df = fetch_crypto_data("BTC-USD", days=30)
        df = calculate_technical_indicators(df)
        self.assertIn("RSI", df.columns)
        self.assertIn("MA_7", df.columns)
        self.assertIn("MA_30", df.columns)

if __name__ == "__main__":
    unittest.main()