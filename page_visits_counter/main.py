from flask import Response
from counter import VisitsCounter
import json

counter = VisitsCounter()

def add_visit(request):
    body = request.get_json(silent=True)
    counter.add_visit(body["key"])
    return Response({}, status=201, mimetype='application/json')

def get_visits(request):
    params = request.args
    count = counter.get_visits(params["key"])
    response_body = json.dumps({"visits": count})
    return Response(response_body, status=200, mimetype='application/json')
