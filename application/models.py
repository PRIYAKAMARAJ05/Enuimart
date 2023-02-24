from application.database import db
from flask_login import UserMixin

# registration class
class information(db.model,UserMixin):
    __tablename__ = 'registration'
    UserId = db.Column(db.Integer(),primary_key=True,autoincrement=False)
    firstname = db.Column(db.String(),nullable=False)
    middlename = db.Column(db.String(),nullable=True)
    lastname = db.Column(db.String(),nullable=True)
    email = db.Column(db.String(),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    phonenumber = db.Column(db.Integer(),nullable=False)
    gender = db.Column(db.String(),nullable=False)
    age = db.Column(db.Integer(),nullable=False)
    # profile = db.relationship('Profile',lazy=true,uselist=false)
    # post = db.relationship('Posts',lazy='dyanmic')

    def __init__(self,uid,fname,mname,lname,email1,password1,phn,gender1,age1):
        self:userId=uid
        self.firstname=fname
        self.middlename=mname
        self.lastname=lname
        self.email=email1
        self.password=password1
        self.phonenumber=phn
        self.gender=gender1
        self.age=age1

# tweet_message class        
class tweet_message(db.model,UserMixin):
    __tablename__='tweet_message'
    tweetId = db.Column(db.Integer(),primary_key=True,autoincrement=False)
    title = db.Column(db.String(),nullable=True)
    description = db.Column(db.String(),nullable=False)
    date = db.Column(db.String(),nullable=False)
    UserId = db.Column(db.Integer(),nullable=False)

    def __init__(self,id,t,desc,dt,uid):
        self.tweetId=id
        self.title=t
        self.description=desc
        self.date=dt 
        self.UserId=uid