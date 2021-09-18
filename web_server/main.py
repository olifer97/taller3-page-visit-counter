from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/')
@app.route('/home/<name>')
def home(name=None):
    return render_template('home.html', name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")