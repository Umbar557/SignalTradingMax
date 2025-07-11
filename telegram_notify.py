import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from datetime import datetime

def send_telegram_signal(pair, signal, entry, tp, sl, note):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"""
📢 *Forex Scalping Signal*
📍Pair: {pair}
🕒 Time: {time_now}
📈 Signal: *{signal}*
💰 Entry: `{entry}`
🎯 TP: `{tp}`
🛑 SL: `{sl}`
🧠 Note: {note}
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"})
  
