class VisitsCounter:
    def __init__(self):
        self.pages = {}
    
    def add_visit(self, key):
        self.pages[key] = self.pages.get(key, 0) + 1

    def get_visits(self, key):
        return self.pages.get(key, 0)