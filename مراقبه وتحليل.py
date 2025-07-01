# Created on iPhone.

print("مرحبا بلال ❤️!")
import requests
import time

# بيانات تليجرام
TOKEN = "8143588448:AAGLz640AfAQBPgI1PbKHD-VKsZiAO7fpZQ"
CHAT_ID = "5123594919"

# العملة المطلوبة
symbol = "SEIUSDT"

# دالة لجلب الأسعار الأخيرة
def get_price(symbol):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m&limit=20"
    response = requests.get(url)
    data = response.json()
    closes = [float(candle[4]) for candle in data]  # إغلاق الشموع
    return closes

# دالة لإرسال رسالة تليجرام
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

# دالة تحليل الاتجاه
def analyze_trend(prices):
    ma_5 = sum(prices[-5:]) / 5
    ma_20 = sum(prices) / len(prices)
    current_price = prices[-1]

    if ma_5 > ma_20:
        return f"🔼 SEI صاعدة!\n📈 السعر الحالي: {current_price:.4f}"
    elif ma_5 < ma_20:
        return f"🔽 SEI نازلة!\n📉 السعر الحالي: {current_price:.4f}"
    else:
        return f"⚠️ اتجاه غير واضح\nالسعر الحالي: {current_price:.4f}"

# تكرار كل دقيقة
while True:
    try:
        prices = get_price(symbol)
        signal = analyze_trend(prices)
        send_telegram_message(signal)
        time.sleep(60)
    except Exception as e:
        print("Error:", e)
        time.sleep(60)