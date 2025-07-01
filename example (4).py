# Created on iPhone.

print("Hello World!")
import requests
import time

# إعدادات تليجرام
TOKEN = "8107757640:AAHUsXacd_ETikwX43Q2NZuhIsnIW-fefEs"
CHAT_ID = "5123594919"

# حدود التنبيه
TAKE_PROFIT = 0.30
STOP_LOSS = 0.26

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=SEIUSDT"
    data = requests.get(url).json()
    return float(data["price"])

# حالة التذكير حتى ما تتكرر الرسائل
tp_sent = False
sl_sent = False

print("✅ SEI Bot Started...")

while True:
    try:
        price = get_price()
        print(f"🔄 السعر الحالي: {price}")

        if price >= TAKE_PROFIT and not tp_sent:
            send_telegram(f"🎯 السعر وصل {price} ✅ قرب الهدف (0.33)، فكر تغلق الصفقة!")
            tp_sent = True

        elif price <= STOP_LOSS and not sl_sent:
            send_telegram(f"⚠️ السعر نزل {price} ❌ قرب وقف الخسارة (0.255)، راجع الصفقة!")
            sl_sent = True

        time.sleep(30)  # يفحص كل 30 ثانية

    except Exception as e:
        print("❌ حصل خطأ:", e)
        time.sleep(60)