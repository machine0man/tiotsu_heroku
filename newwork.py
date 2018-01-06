<<<<<<< HEAD

from mapbox import Datasets
from flask import Flask, request
import requests

access_token="sk.eyJ1Ijoic2hhbmtvaWJpdG8iLCJhIjoiY2pidGk1NHVyMWhsNDJxcm5qMzk1NjdjbSJ9.eVgFTGreLyiND18CkqNS8w"

datasets = Datasets() 

app = Flask(__name__)
@app.route('/', methods=['GET'])

def datasetprocess(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    datasets.update_feature('cjbphbl3008s833ntx1t5psea', 'feature-id', data)
    #resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    #print(resp.content)
 
 
@app.route('/', methods=['POST'])
def handle_incoming_data():
    data = request.json
    print(data)
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    print(sender)
    message = data['entry'][0]['messaging'][0]['message']['text']
    print(message)
    datasetprocess(sender, message[::1])
 
    return "ok"
 
 
if __name__ == '__main__':
    app.run(debug=True)

=======
from mapbox import Datasets
from flask import Flask, request
import requests

access_token="sk.eyJ1Ijoic2hhbmtvaWJpdG8iLCJhIjoiY2pidGk1NHVyMWhsNDJxcm5qMzk1NjdjbSJ9.eVgFTGreLyiND18CkqNS8w"

datasets = Datasets() 

app = Flask(__name__)
@app.route('/', methods=['GET'])

def datasetprocess(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    datasets.update_feature('cjbphbl3008s833ntx1t5psea', 'feature-id', data)
    #resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    #print(resp.content)
 
 
@app.route('/', methods=['POST'])
def handle_incoming_data():
    data = request.json
    print(data)
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    print(sender)
    message = data['entry'][0]['messaging'][0]['message']['text']
    print(message)
    datasetprocess(sender, message[::1])
 
    return "ok"
 
 
if __name__ == '__main__':
    app.run(debug=True)

>>>>>>> d6bedb31c4a4bdb0b05a27458ca73d455fb16e4d

#datasets.list_features("cjbphbl3008s833ntx1t5psea").json()
