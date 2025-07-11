def analyze_candle(df):
    last = df.iloc[-1]
    body = abs(last['close'] - last['open'])
    wick = (last['high'] - last['low']) - body
    if body > wick and last['close'] > last['open']:
        return "Bullish candle"
    elif body > wick and last['close'] < last['open']:
        return "Bearish candle"
    return "Uncertain"
