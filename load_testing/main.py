from locust import HttpUser, TaskSet, task, events
from bs4 import BeautifulSoup

def is_static_file(f):
    if "web_server/assets/" in f:
        return True
    else:
        return False

class WebsiteAnonUser(HttpUser):

    def fetch_static_assets(self, response, key):
        resource_urls = set()
        soup = BeautifulSoup(response.text, "html.parser")

        for res in soup.find_all(src=True):
            url =  res['src']
            if is_static_file(url):
                resource_urls.add(url)
                if 'getVisits' in url:
                    resource_urls.add(res['counter-url'] + '?key=' + res['key'])
                    #print(res['counter-url'])
                    #print(res['key'])
            else:
                print("Skipping: " + url)

        for res in soup.find_all(href=True):
            url =  res['href']
            if is_static_file(url):
                resource_urls.add(url)
            else:
                print("Skipping: " + url)

        for url in resource_urls:
            if 'getVisits?key=' in url:
                response = self.client.get(url, name="/getVisits")
            else:
                response = self.client.get(url, name=f"({key} Static File)")
            print(response.text)

    @task(1)
    def home(self):
        response = self.client.get("/home")
        self.fetch_static_assets(response, 'home')

    @task(2)
    def about(self):
        response = self.client.get("/about")
        self.fetch_static_assets(response, 'about')

    @task(3)
    def jobs(self):
        response = self.client.get("/jobs")
        self.fetch_static_assets(response, 'jobs')