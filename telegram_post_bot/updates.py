import requests

BOT_TOKEN = '7620169423:AAGviCcLrA_cRNE_jSP7zeyW3crd0qGNjj4'  # from BotFather

response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates")
print(response.json())
