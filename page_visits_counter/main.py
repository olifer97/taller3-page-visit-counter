from flask import Flask, request, Response
from counter import VisitsCounter
import json

app = Flask(__name__)
counter = VisitsCounter()

@app.route('/visits', methods=['POST'])
def add_visit():
    body = request.json
    count = counter.add_visit(body["key"])
    response_body = json.dumps({"visits": count})
    return Response(response_body, status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5005")