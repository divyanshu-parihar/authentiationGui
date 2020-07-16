from flask import Flask
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
#Model
class Users(db.Model):
    name=db.Column("names",db.String(15),nullable=False,primary_key=True)
    password=db.Column("passcodes",db.String(15),nullable=False)

    def __repr__(self):
        return f'Username={name} ,views={password}'
#creaiting resouce
class AddUser(Resource):
    def post(self,user,pwd):
        if user== Users.query.filter_by(name=user):
            messaage='already exist'
        else:
            newUser=Users(name=user,password=pwd)
            db.session.add(newUser)
            db.session.commit()
            message='done!!!!!!'
        return {'message': message}

class LoginCheck(Resource):
    def post(self,username,password):
        if  Users.query.filter_by(name=username,password =password):
            message='ACCESS GRANTED'
        else:
            message='Not Found'
        return {'message': message}

class welcome(Resource):
    def get(self,username,password):
        message='Hello world'
        return {'message': message}
#adding resource intialization
api.add_resource(welcome,'/')
api.add_resource(AddUser,'/adduser/<string:user>/<string:pwd>')
api.add_resource(LoginCheck,'/check/<string:username>/<string:password>')




if __name__=="__main__":
    app.run(debug=True)
