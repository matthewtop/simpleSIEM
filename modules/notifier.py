import requests
import yaml

def load_config():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config

config = load_config()

TELEGRAM_TOKEN = config['telegram']['token'] 
CHAT_ID = config['telegram']['chat_id']

def send_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"[ALERT] {message}"
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"[!] Nie udało się wysłać alertu: {response.text}")
    except Exception as e:
        print(f"[!] Błąd wysyłania alertu: {e}")