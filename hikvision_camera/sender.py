import requests


class Sender:
    def __init__(self, URL):
        self.url = URL

    def postStadionUhfCards(self, data):
        response = requests.post(self.url, json=data)
        return response
