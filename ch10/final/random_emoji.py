import random
import requests
class EmojiAPI:
    def __init__(self):
        self.url = "https://emojihub.yurace.pro/api/random"
    
    def random_emoji():
        url = "https://emojihub.yurace.pro/api/random"
        response = requests.get(url)
        print(response.status_code)
        print(response.text)
        # data = response.json()
        # return data['results']