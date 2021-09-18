import requests

class VisitsCounterService:
    def __init__(self, url = "http://localhost:5005"):
        self.url = url
    
    def add_visit(self, key):
        response = requests.post(self.url + '/visits', json={"key": key})
        return response.json()['visits']