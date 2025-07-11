from indicators import check_signal
from candle_analysis import analyze_candle
from telegram_notify import send_telegram_signal
from twelvedata_api import get_price_data
from utils import calculate_atr
from config import PAIR, TIMEFRAME

def main():
    df = get_price_data(PAIR, TIMEFRAME)
    if df is None or len(df) < 50:
        print("❌ Data tidak cukup.")
        return

    signal = check_signal(df)
    candle_note = analyze_candle(df)
    atr = calculate_atr(df)

    if signal:
        entry = df['close'].iloc[-1]
        tp = round(entry + atr * 2, 5) if signal == 'BUY' else round(entry - atr * 2, 5)
        sl = round(entry - atr * 1.5, 5) if signal == 'BUY' else round(entry + atr * 1.5, 5)
        send_telegram_signal(PAIR, signal, entry, tp, sl, candle_note)
      
