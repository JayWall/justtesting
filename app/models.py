from . import db
from datetime import datetime

def timeinfo():
    format = "%d %b %Y"    
    return datetime.today().strftime(format)

# Holdover from lab 5 for the login system
# Not really needed for this project but kept
# just for feature completeness
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    password = db.Column(db.String(255))
    username = db.Column(db.String(80), unique=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

# Actual database model for this project
class UserProfileNew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    age = db.Column(db.Integer)
    bio = db.Column(db.String(140))
    datecreated = db.Column(db.DateTime)
    gender = db.Column(db.String(10))
    image = db.Column(db.String(255))

    def __init__(self, fName, lName, username, age, bio, image, gender):
        self.first_name = fName
        self.last_name = lName
        self.username = username
        self.age = age
        self.bio = bio
        self.gender = gender
        self.image = image
        self.datecreated = timeinfo()
