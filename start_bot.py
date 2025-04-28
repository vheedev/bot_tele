
import time
import requests

# Setup bot token
TOKEN = "7722270521:AAGErN_FlV_7XVq8_yABGdHep-x2tVVEUGo"
URL_GET_UPDATES = f"https://api.telegram.org/bot7722270521:AAGErN_FlV_7XVq8_yABGdHep-x2tVVEUGo/getUpdates"
URL_SEND_MESSAGE = f"https://api.telegram.org/bot7722270521:AAGErN_FlV_7XVq8_yABGdHep-x2tVVEUGo/sendMessage"

def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    response = requests.get(f"{URL}/getUpdates", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(f"{URL}/sendMessage", data=payload)

print("✅ Bot polling dimulai.")
last_update_id = None

while True:
    data = get_updates(offset=last_update_id)
    if data and "result" in data:
        for update in data["result"]:
            update_id = update["update_id"]
            if last_update_id is None or update_id > last_update_id:
                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"]["text"]
                    print(f"📩 {chat_id}: {text}")

                    reply_text = "Morning Babe! 💬 Aku sudah online siap kerja 🚀❤️"
                    send_message(chat_id, reply_text)

                last_update_id = update_id + 1
    time.sleep(3)
