from flask import Flask, request, Response
from prometheus_client import Counter, Summary, generate_latest

REQUEST_COUNT=Counter("app_request_count", "Number of requests")

app = Flask(__name__)
REQUEST_LATENCY_TIME=Summary("app_request_latency_time", "Request latency time")
@app.route('/')
def hello_team():
    REQUEST_COUNT.inc()
    return 'Hello Team,This is from Docker WSGI'
@app.route('/metrics')
def metrics():
    return Response(generate_latest(),200, mimetype="text/plain")
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)