import requests

telegram_bot_api = ""
channel_ids = [123,1234]
discord_webhook = "https://discord.com/api/webhooks/..."

def announce_discord(msg):
    payload=f"content={msg}"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", discord_webhook, headers=headers, data=payload)
    print(response.text)

def announce_telegram(msg):
    bannedwords = ["||@everyone||", "||@here||" ,"@everyone", "@here"] #Ignores discord special mentions so it won't be included on telegram messages.
    for x in bannedwords:
        msg = msg.replace(x, "")
    for i in channel_ids:
        response = requests.request("GET", f"https://api.telegram.org/bot{telegram_bot_api}/sendMessage?chat_id={i}&text={msg}")
        print(response.text) 

def execute(msg):
    announce_discord(msg)
    announce_telegram(msg)

message = input("Enter message: ")
execute(msg=message)
