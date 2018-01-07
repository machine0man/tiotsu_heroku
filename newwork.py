
from mapbox import Datasets
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from sqlalchemy import create_engine

access_token="sk.eyJ1Ijoic2hhbmtvaWJpdG8iLCJhIjoiY2pidGk1NHVyMWhsNDJxcm5qMzk1NjdjbSJ9.eVgFTGreLyiND18CkqNS8w"

datasets = Datasets() 

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

@app.route('/',methods=['GET','POST'])
def index():
    def GetGeolocationAndAddDatasetFeature():
    Geolocation = request.form.get('Geolocation')
    Username = request.form.get('Username')
    feature = {'type': 'Feature','id':Username,'properties': {'Town': 'Testall'},'geometry':{'type':'Point','coordinates':[Geolocation]}}
    datasets.update_feature('cjbwkjod422u233nx1xp8ltzr',Username,feature)

 
if __name__ == '__main__':
    app.run(debug=True)


