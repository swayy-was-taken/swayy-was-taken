import requests
import json




discord_webhook_url = input("Enter webhook: ")
message = input("Enter message ")

Message = {
"content": message
}

while True:
    print("Message Sent!")
    requests. post(discord_webhook_url, data=Message)
