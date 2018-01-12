MAPBOX_ACCESS_TOKEN="sk.eyJ1IjoicGFwcHVzc3AxIiwiYSI6ImNqYndrZ3RrMTI2eDIzM3BjaXFtY2gzdmcifQ.B2sQFFPWo5tBrvcsL9cDVQ"

from mapbox import Datasets
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from sqlalchemy import create_engine
from mapbox import Uploader

service = Uploader(access_token=MAPBOX_ACCESS_TOKEN)
from time import sleep
from random import randint
import urllib.request

datasets = Datasets(access_token=MAPBOX_ACCESS_TOKEN)

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)
#engine = create_engine('postgresql+psycopg2://shankoibito:pappussp@localhost/tiotsudatamap')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shankoibito:pappussp@localhost/tiotsudatamap'
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    Geolocation = db.Column(db.String(120), unique=True)
    UserName= db.Column(db.String)

    def __init__(self, Geolocation):
        self.Geolocation = Geolocation

    def __repr__(self):
        return '<Geolocation %r>' % self.Geolocation

@app.route('/',methods=['POST'])
def GetGeolocationAndAddDatasetFeature():
    Geolocation = request.form['Geolocation']
    print(Geolocation)
    Username = request.form['Username']
    #feature = {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'MyHouse': 'Towntest'}, 'geometry': {'coordinates': [Geolocation], 'type': 'Point'}, 'id': 'feature-id'}]}
    #feature = {"type": "Feature", "id": Username, "properties": {'name": "Towntest"},"geometry": {Geolocation}}
    feature=eval(Geolocation)
    datasets.update_feature('cjbwkjod422u233nx1xp8ltzr',Username,feature)
    with urllib.request.urlopen('https://drive.google.com/uc?export=download&id=149UYcRpfqVfga4nQk9ODnTgpB4hqHRqG') as src:
        upload_resp = service.upload(src.read(), 'pappussp1.data')
    if upload_resp.status_code == 422:
        for i in range(5):
            sleep(5)
            with urllib.request.urlopen('https://drive.google.com/uc?export=download&id=149UYcRpfqVfga4nQk9ODnTgpB4hqHRqG') as src:
                upload_resp = service.upload(src.read(), 'pappussp1.data')
            if upload_resp.status_code != 422:
                break
    return "OK"
 
if __name__ == '__main__':
    app.run(debug=True)


