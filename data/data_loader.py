import yfinance as yf
import pandas as pd


def fetch_data(ticker: str, period: str = "5y"):
    """
    Fetch market data from Yahoo Finance.

    Standard schema (IMPORTANT):
    Date, Open, High, Low, Close, Volume
    """

    df = yf.download(ticker, period=period, auto_adjust=True)

    if df is None or df.empty:
        raise ValueError(f"No data returned for ticker: {ticker}")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)

    df = df.reset_index()

    # Ensure consistent column names
    expected_cols = ["Date", "Open", "High", "Low", "Close", "Volume"]
    df = df[expected_cols]

    # Optional: standardize naming (recommended for consistency)
    df.columns = ["date", "open", "high", "low", "close", "volume"]

    # Clean data
    df = df.dropna()
    df = df.sort_values("date")

    return df