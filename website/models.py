from . import db  # . means we can access anything from init file
# usermixin is a custom class which we are inheriting that will give our user object something specific for our flask login
from flask_login import UserMixin 
# this will automatically help us in adding the date 
from sqlalchemy.sql import func

# this is a one-to-many model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # referencing the primary key id of the user

class User(db.Model, UserMixin): # just for user object we are also inheriting UserMixin
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #last_name = db.Column(db.String(150))
    notes = db.relationship('Note')