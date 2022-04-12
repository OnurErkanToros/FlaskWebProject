from datetime import datetime
from atmacaFlask import db, loginManager
from flask_login import UserMixin


@loginManager.user_loader
def loadUser(userId):
    return User.query.get(userId)


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User: {self.name}'


class Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String)
    text = db.Column(db.String, nullable=False)
    activityDate = db.Column(db.DateTime, nullable=False)
    activityAddDate = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, title, subtitle, text, activityDate, activityAddDate):
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.activityDate = activityDate
        self.activityAddDate = activityAddDate

    def __repr__(self) -> str:
        return f'activity: {self.title}'


class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String)
    text = db.Column(db.String, nullable=False)
    announcementDate = db.Column(db.Date, nullable=False)
    announcementAddDate = db.Column(
        db.Date, nullable=False, default=datetime.now())

    def __init__(self, title, subtitle, text, announcementDate, announcementAddDate):
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.announcementDate = announcementDate
        self.announcementAddDate = announcementAddDate

    def __repr__(self) -> str:
        return f'announcement: {self.title}'


class AnaHizmet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    baslik = db.Column(db.String, nullable=False)
    slogan = db.Column(db.String, nullable=False)
    aciklama = db.Column(db.String, nullable=False)
    resimYolu = db.Column(db.String, nullable=False)
    altHizmetler = db.relationship('AltHizmet', backref='ana_hizmet')


class AltHizmet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metin = db.Column(db.String, nullable=False)
    anaHizmetId = db.Column(db.Integer, db.ForeignKey('ana_hizmet.id'))

    
    
