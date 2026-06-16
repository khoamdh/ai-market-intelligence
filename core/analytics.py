import pandas as pd

def compute_features(sp500, btc):
    sp500 = sp500.copy()
    btc = btc.copy()

    sp500["return"] = sp500["close"].pct_change()
    btc["return"] = btc["close"].pct_change()

    merged = pd.merge(
        sp500,
        btc,
        on="date",
        suffixes=("_sp500", "_btc")
    )

    merged["correlation"] = merged["return_sp500"].rolling(30).corr(merged["return_btc"])

    return merged