MAPBOX_ACCESS_TOKEN="sk.eyJ1IjoicGFwcHVzc3AxIiwiYSI6ImNqYndrZ3RrMTI2eDIzM3BjaXFtY2gzdmcifQ.B2sQFFPWo5tBrvcsL9cDVQ"

from mapbox import Datasets
from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from sqlalchemy import create_engine
import requests


datasets = Datasets(access_token=MAPBOX_ACCESS_TOKEN)

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)
#engine = create_engine('postgresql+psycopg2://shankoibito:pappussp@localhost/tiotsudatamap')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vrtvapidqltuni:abf33013012ea480de6c1d50bc4230d6218296846ba8a5bd4b44c80fa7325859@ec2-54-227-250-33.compute-1.amazonaws.com:5432/d9p6o27d01ao21'
def getdatafromtiotsu():
    username=requests.form['username']
    email=requests.form['email']
    yunk=requests.form['yunk']
    aura=requests.form['aura']
    houselevel=requests.form['houselevel']
    mylocation=requests.form['mylocation']

def cleardatafromtiotsu():
    username=null
    email=null
    yunk=null
    aura=null
    houselevel=null
    mylocation=null
    return "OK"

class tiotsu_users(db.Model):
    __tablename__ = "tiotsu_users"
    email = db.Column(db.String(120),nullable=False, primary_key=True)
    firstname = db.Column(db.String(100),nullable=False)
    yunk = db.Column(db.String(100))
    level = db.Column(db.String(50),nullable=False)
    aura = db.Column(db.String(100))
    houselevel = db.Column(db.String(50))
    mylocation = db.Column(db.String(150),nullable=False,unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<email %r>' % self.email

    
@app.route('/user',methods=['POST'])
def createanduploaddata():
    getdatafromtiotsu()
    newuser=tiotsu_users(email,firstname,yunk,level,aura,houselevel,mylocation)
    db.session.add(newuser)
    db.session.commit()
    cleardatafromtiotsu()
    return "OK"
    
def TileSet():
    r = requests.post('https://tiotsu-js.herokuapp.com/', data = {'UserName':'Username'})
    return "OK"

@app.route('/',methods=['POST'])
def GetGeolocationAndAddDatasetFeature():
    Geolocation = request.form['Geolocation']
    print(Geolocation)
    Username = request.form['Username']
    #feature = {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'MyHouse': 'Towntest'}, 'geometry': {'coordinates': [Geolocation], 'type': 'Point'}, 'id': 'feature-id'}]}
    #feature = {"type": "Feature", "id": Username, "properties": {'name": "Towntest"},"geometry": {Geolocation}}
    feature=eval(Geolocation)
    datasets.update_feature('cjbwkjod422u233nx1xp8ltzr',Username,feature)
    TileSet()
    return "OK"
 
if __name__ == '__main__':
    app.run(debug=True)


