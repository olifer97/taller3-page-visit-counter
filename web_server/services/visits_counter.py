import requests

class VisitsCounterService:
    def __init__(self, url = "http://localhost:5005"):
        self.url = url
    
    def add_visit(self, key):
        return requests.post(self.url + '/addVisit', json={"key": key})