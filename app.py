from flask import Flask
import http.client
import mimetypes

app = Flask(__name__)

@app.route('/')
def homepage():
    
    conn = http.client.HTTPConnection("test-exp-heroku.us-e2.cloudhub.io")
    payload = ''
    headers = {'client_id': 'test','client_secret': 'test'}
    conn.request("GET", "/api/test/A00000000000000001", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    return data.decode("utf-8")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

