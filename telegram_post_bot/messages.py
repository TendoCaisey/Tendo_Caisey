import requests

# === Config ===
BOT_TOKEN = '7620169423:AAGviCcLrA_cRNE_jSP7zeyW3crd0qGNjj4'
CHAT_ID = 6642148010  # use '@channelusername' or numeric ID
MESSAGE = """
✅ Bot is working perfectly in the group again!
"""

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"  # You can also use Markdown
    }

    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("✅ Message sent successfully!")
    else:
        print("❌ Failed to send message")
        print(response.text)

# === Run ===
send_telegram_message(BOT_TOKEN, CHAT_ID, MESSAGE)
