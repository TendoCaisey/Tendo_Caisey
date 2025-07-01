import requests

TOKEN = '7620169423:AAGviCcLrA_cRNE_jSP7zeyW3crd0qGNjj4'
updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates').json()
print(updates)
