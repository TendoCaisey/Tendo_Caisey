import schedule
import time
from messages import BOT_TOKEN, CHAT_ID, MESSAGE

def job():
    send_telegram_message(BOT_TOKEN, CHAT_ID, MESSAGE)

# Schedule to run every day at 9:00 AM
schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
