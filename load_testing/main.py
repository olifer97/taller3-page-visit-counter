from locust import HttpUser, TaskSet, task, events
from bs4 import BeautifulSoup

def is_static_file(f):
    if "web_server/assets/" in f:
        return True
    else:
        return False

'''
class AuthBrowsingUser(TaskSet):
    def on_start(l):
        response = l.client.get("/user/login", name="Login")
        soup = BeautifulSoup(response.text, "html.parser")
        drupal_form_id = soup.select('input[name="form_build_id"]')[0]["value"]
        r = l.client.post("/user/login", {"name":"nnewton", "pass":"hunter2", "form_id":"user_login_form", "op":"Log+in", "form_build_id":drupal_form_id})

    @task(10)
    def home(l):
        response = l.client.get("/home", name="Frontpage (Auth)")
        fetch_static_assets(l, response)

class WebsiteAuthUser(HttpLocust):
    task_set = AuthBrowsingUser  
'''  

class WebsiteAnonUser(HttpUser):

    def fetch_static_assets(self, response):
        resource_urls = set()
        soup = BeautifulSoup(response.text, "html.parser")

        for res in soup.find_all(src=True):
            url =  res['src']
            if is_static_file(url):
                resource_urls.add(url)
            else:
                print("Skipping: " + url)

        for res in soup.find_all(href=True):
            url =  res['href']
            if is_static_file(url):
                resource_urls.add(url)
            else:
                print("Skipping: " + url)

        for url in resource_urls:
            #Note: If you are going to tag different static file paths differently,
            #this is where I would normally do that.
            print(url)
            response = self.client.get(url, name="(Static File)")
            print(response.text)

    @task
    def home(self):
        response = self.client.get("/home")
        self.fetch_static_assets(response)