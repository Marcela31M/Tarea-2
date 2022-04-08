from utilss.db import db

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(20))
    message = db.Column(db.String(20))

    def __init__(self,firstname,lastname, email, message):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.message = message
