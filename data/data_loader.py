import yfinance as yf

def fetch_data(ticker, start="2010-01-01"):
    df = yf.download(ticker, start=start)
    df = df.reset_index()
    df = df[["Date", "Close"]]
    df.columns = ["date", "price"]
    return df