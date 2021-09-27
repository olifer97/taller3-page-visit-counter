from google.cloud import firestore

from distributed_counters import DistributedCounter

KEYS = ['home', 'about', 'jobs']
class VisitsCounter:
    def __init__(self):
        self.db = firestore.Client()
        
        self.counter = DistributedCounter(2)

        self.docs = {}
        col = self.db.collection("counters")
        for key in KEYS:
            self.docs[key] = col.document(key)

        for doc_ref in self.docs.values():
            self.counter.init_counter(doc_ref)
        #self.pages = {}
    
    def add_visit(self, key):
        self.counter.increment_counter(self.docs[key])
        #self.pages[key] = self.pages.get(key, 0) + 1

    def get_visits(self, key):
        return self.counter.get_count(self.docs[key])
        #return self.pages.get(key, 0)