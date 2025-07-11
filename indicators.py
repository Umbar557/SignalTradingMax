import pandas as pd
import numpy as np

def compute_rsi(close, period=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def compute_macd(close):
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

def check_signal(df):
    df['ema8'] = df['close'].ewm(span=8).mean()
    df['ema21'] = df['close'].ewm(span=21).mean()
    df['rsi'] = compute_rsi(df['close'])
    df['macd'], df['macd_signal'] = compute_macd(df['close'])
    
    last = df.iloc[-1]
    if last['ema8'] > last['ema21'] and last['rsi'] > 50 and last['macd'] > last['macd_signal']:
        return 'BUY'
    elif last['ema8'] < last['ema21'] and last['rsi'] < 50 and last['macd'] < last['macd_signal']:
        return 'SELL'
    return None
