# setup.py
from setuptools import setup, find_packages

setup(
    name="crypto-analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.23.0",
        "matplotlib>=3.7.0",
        "tensorflow>=2.12.0",
        "scikit-learn>=1.2.0",
        "yfinance>=0.1.70",
        "gradio>=2.9.0"
    ],
)