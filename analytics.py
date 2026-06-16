def compute_features(sp500, btc):
    df = sp500.merge(btc, on="date", suffixes=("_sp500", "_btc"))

    df["sp500_return"] = df["price_sp500"].pct_change()
    df["btc_return"] = df["price_btc"].pct_change()

    df["corr_30d"] = df["sp500_return"].rolling(30).corr(df["btc_return"])

    return df