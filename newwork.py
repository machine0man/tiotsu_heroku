MAPBOX_ACCESS_TOKEN="sk.eyJ1IjoicGFwcHVzc3AxIiwiYSI6ImNqYndrZ3RrMTI2eDIzM3BjaXFtY2gzdmcifQ.B2sQFFPWo5tBrvcsL9cDVQ"

from mapbox import Datasets
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from sqlalchemy import create_engine
import requests


datasets = Datasets(access_token=MAPBOX_ACCESS_TOKEN)

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)
#engine = create_engine('postgresql+psycopg2://shankoibito:pappussp@localhost/tiotsudatamap')
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://shanbirsingh@toitsu:Ihope1lovemyself@toitsu.postgres.database.azure.com:5432/postgres'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vrtvapidqltuni:abf33013012ea480de6c1d50bc4230d6218296846ba8a5bd4b44c80fa7325859@ec2-54-227-250-33.compute-1.amazonaws.com:5432/d9p6o27d01ao21'
app.config['SECRET_KEY'] = 'oh_so_secret'

class tiotsu_users(db.Model):
    __tablename__ = "tiotsu_users"
    email = db.Column(db.String(120),nullable=False, primary_key=True)
    firstname = db.Column(db.String(100),nullable=False)
    yunk = db.Column(db.String(100))
    level = db.Column(db.String(50),nullable=False)
    aura = db.Column(db.String(100))
    houselevel = db.Column(db.String(50))
    mylocation = db.Column(db.String(150),nullable=False,unique=True)
    help = db.Column(db.String(100))

    def __init__(self, email,firstname,yunk,level,aura,houselevel,mylocation,help):
        self.email = email
        self.firstname = firstname
        self.yunk = yunk
        self.level = level
        self.aura = aura
        self.houselevel = houselevel
        self.mylocation = mylocation
        self.help = help

    def __repr__(self):
        return '<email %r>' % self.email

def getdatafromtiotsu():
    firstname=request.form['username']
    email=request.form['mymail']
    yunk=request.form['yunk']
    aura=request.form['aura']
    houselevel=request.form['houselevel']
    mylocation=request.form['Geolocation']

@app.route('/dealsdataupdate',methods=['POST'])
def dealsdataupdate():
    email=request.form['mymail']
    print(email)
    yunk=request.form['yunk']
    print(yunk)
    houselevel=request.form['houselevel']
    print(houselevel)
    update_this = tiotsu_users.query.filter_by(email = email).first()
    if(update_this):
        update_this.yunk = yunk
        update_this.houselevel = houselevel
        db.session.commit()
    return "OK"

@app.route('/windataupdate',methods=['POST'])
def windataupdate():
    email=request.form['mymail']
    print(email)
    yunk=request.form['yunk']
    print(yunk)
    aura=request.form['aura']
    print(aura)
    update_this = tiotsu_users.query.filter_by(email = email).first()
    if(update_this):
        update_this.yunk = yunk
        update_this.aura = aura
        db.session.commit()
    return "OK"

def createanduploaddata():
    update_this = tiotsu_users.query.filter_by(email = email).first()
    if(update_this):
        update_this.yunk = yunk
        update_this.aura = aura
        update_this.houselevel = houselevel
        db.session.commit()
    else:
        newuser=tiotsu_users(email,firstname,yunk,level,aura,houselevel,mylocation)
        db.session.add(newuser)
        db.session.commit()
    return "OK"

@app.route('/playerdatacheck/<mymail>',methods=['GET'])
def playerdatacheck(mymail):
    update_this = tiotsu_users.query.filter_by(email = mymail).first()
    if(update_this):
        playerstatus="0"
    else:
        playerstatus="1"
    print(playerstatus)
    return playerstatus

@app.route('/tiotsulocationcheck/<location>',methods=['GET'])
def checklocationuniqueness(location):
    update_this = tiotsu_users.query.filter_by(mylocation = location).first()
    if(update_this):
        locationstatus="0"
    else:
        locationstatus = "1"
    return locationstatus

@app.route('/tiotsudatasend/<mymail>',methods=['GET'])
def senddatatotiotsu(mymail):
    update_this = tiotsu_users.query.filter_by(email = mymail).first()
    if(update_this):
        auraattack=update_this.aura
        firstnameattack=update_this.firstname
        yunkattack=update_this.yunk
        houselevelattack=update_this.houselevel
    tiotsudata=auraattack+"\r\n"+firstnameattack+"\r\n"+yunkattack+"\r\n"+houselevelattack
    print(tiotsudata)
    return tiotsudata

@app.route('/tiotsudataget',methods=['POST'])
def getattackdatafromtiotsu():
    if (request.method == "POST"):
        emailattack=request.form['emailattack']
    return "OK"

@app.route('/alreadyuser',methods=['POST'])
def alreadyuserupdatedata():
    getdatafromtiotsu()
    update_this = tiotsu_users.query.filter_by(email = email).first()
    update_this.yunk = yunk
    update_this.level = level
    update_this.aura = aura
    update_this.houselevel = houselevel
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
    firstname=request.form['username']
    email=request.form['mymail']
    yunk=request.form['yunk']
    aura=request.form['aura']
    houselevel=request.form['houselevel']
    mylocation=request.form['mylocation']
    level=request.form['level']
    help="help"
    print(email)
    update_this = tiotsu_users.query.filter_by(email = email).first()
    if(update_this):
        update_this.yunk = yunk
        update_this.aura = aura
        update_this.houselevel = houselevel
        db.session.commit()
    else:
        newuser=tiotsu_users(email,firstname,yunk,level,aura,houselevel,mylocation,help)
        db.session.add(newuser)
        db.session.commit()
        feature=eval(Geolocation)
        datasets.update_feature('cjbwkjod422u233nx1xp8ltzr',email,feature)
        print("DatasetUploaded")
        TileSet()
    #feature = {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'MyHouse': 'Towntest'}, 'geometry': {'coordinates': [Geolocation], 'type': 'Point'}, 'id': 'feature-id'}]}
    #feature = {"type": "Feature", "id": Username, "properties": {'name": "Towntest"},"geometry": {Geolocation}}
    return "OK"
 
if __name__ == '__main__':
    app.run(debug=True)


