import os
from flask import escape, render_template
from services.visits_counter import VisitsCounterService

page_visits_counter = os.environ['PAGE_VISITS_COUNTER_URL']
counter = VisitsCounterService(url=page_visits_counter)


def home(request):
    counter.add_visit("home")
    return render_template('home.html', url= page_visits_counter + '/getVisits')

def about(request):
    counter.add_visit("about")
    return render_template('about.html', url= page_visits_counter + '/getVisits')

def jobs(request):
    counter.add_visit("jobs")
    return render_template('jobs.html', url= page_visits_counter + '/getVisits')