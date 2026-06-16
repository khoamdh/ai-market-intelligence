from data.data_loader import fetch_data
from core.analytics import compute_features

def get_sp500():
    return fetch_data("^GSPC")

def get_btc():
    return fetch_data("BTC-USD")

def get_correlation():
    sp500 = fetch_data("^GSPC")
    btc = fetch_data("BTC-USD")
    df = compute_features(sp500, btc)
    return df["correlation"].dropna().iloc[-1]