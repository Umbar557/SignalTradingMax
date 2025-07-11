import requests
import pandas as pd
from config import TWELVE_API_KEY

def get_price_data(symbol='EURUSD', interval='1min'):
    url = f"https://api.twelvedata.com/time_series"
    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": 100,
        "apikey": TWELVE_API_KEY
    }
    r = requests.get(url, params=params)
    data = r.json()
    
    if "values" not in data:
        print("Gagal ambil data:", data.get("message"))
        return None

    df = pd.DataFrame(data["values"])
    df.rename(columns={
        "datetime": "time",
        "open": "open",
        "high": "high",
        "low": "low",
        "close": "close",
        "volume": "volume"
    }, inplace=True)

    df = df.astype(float, errors='ignore')
    df['time'] = pd.to_datetime(df['time'])
    df.sort_values('time', inplace=True)
    return df.reset_index(drop=True)
