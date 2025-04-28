
import time
import requests

# Setup bot token
TOKEN = "7722270521:AAGErN_FlV_7XVq8_yABGdHep-x2tVVEUGo"
URL_GET_UPDATES = f"https://api.telegram.org/bot7722270521:AAGErN_FlV_7XVq8_yABGdHep-x2tVVEUGo/getUpdates"
URL_SEND_MESSAGE = f"https://api.telegram.org/bot7722270521:AAGErN_FlV_7XVq8_yABGdHep-x2tVVEUGo/sendMessage"

def get_updates(offset=None):
    params = {"offset": offset}
    response = requests.get(URL_GET_UPDATES, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(URL_SEND_MESSAGE, data=payload)

print("✅ Bot polling dan auto-reply DIMULAI... Tunggu pesan dari Telegram...")
last_update_id = None

while True:
    data = get_updates(offset=last_update_id)
    if data and "result" in data:
        for update in data["result"]:
            update_id = update["update_id"]
            if last_update_id is None or update_id < update_id:
                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"]["text"]
                    print(f"📩 Pesan dari {chat_id}: {text}")

                    # AUTO REPLY
                    reply_text = "Halo Babe! 💬 Aku sudah online dan siap kerjain tugas kamu hari ini! 🚀❤️"
                    send_message(chat_id, reply_text)

                    # Keyword detection for "start"
                    if "start" in text.lower():
                        print(f"🚀 Keyword 'start' terdeteksi dari {chat_id}! Mulai automation!")
                        # Placeholder trigger action
                        # Replace with actual automation later

                last_update_id = update_id + 1
    time.sleep(3)
