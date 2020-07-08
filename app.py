from flask import Flask
from datetime import datetime
import http.client
app = Flask(__name__)

@app.route('/')
def homepage():

    headers = {'client_id': 'test','client_secret': 'test'}

    conn = http.client.HTTPConnection('test-exp-heroku.us-e2.cloudhub.io')
    conn.request('GET','/api/test/A00000000000000001', headers)
    res = conn.getresponse()

    data = res.read().decode('utf-8')
    print(res.status, res.reason)
    print(res.getheaders())

    return data

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)





