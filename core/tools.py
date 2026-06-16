from data.data_loader import fetch_data
from core.analytics import compute_features


# MARKET TOOLS
def get_sp500(period="5y"):
    return fetch_data("^GSPC", period=period)

def get_btc(period="5y"):
    return fetch_data("BTC-USD", period=period)


# ANALYTICS TOOL
def get_correlation(period="5y"):
    btc = fetch_data("BTC-USD", period=period)
    sp500 = fetch_data("^GSPC", period=period)

    df = compute_features(sp500, btc)

    corr_series = df["correlation"].dropna()

    if len(corr_series) == 0:
        return {
            "correlation": None,
            "samples": 0,
            "message": "Not enough data",
        }

    return {
        "correlation": round(float(corr_series.iloc[-1]), 4),
        "samples": len(df)
    }


# TOOL REGISTRY
TOOLS = {
    "get_sp500": get_sp500,
    "get_btc": get_btc,
    "get_correlation": get_correlation
}