#from flask import Flask, render_template
import os
from flask import escape, render_template
from services.visits_counter import VisitsCounterService

#app = Flask(__name__)
counter = VisitsCounterService(url=os.environ['PAGE_VISITS_COUNTER_URL'])

#@app.route('/home/')
def home(request):
    count = counter.add_visit("home")
    return render_template('home.html', counter=count)

#@app.route('/about/')
def about(request):
    count = counter.add_visit("about")
    return render_template('about.html', counter=count)

#@app.route('/jobs/')
def jobs(request):
    count = counter.add_visit("jobs")
    return render_template('jobs.html', counter=count)

#if __name__ == '__main__':
#    app.run(host="0.0.0.0", port="5000")