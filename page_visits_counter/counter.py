class VisitsCounter:
    def __init__(self):
        self.pages = {}
    
    def add_visit(self, key):
        self.pages[key] = self.pages.get(key, 0) + 1
        return self.pages[key]