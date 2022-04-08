from flask import Blueprint, render_template
from flask.templating import render_template
from forms.formMensaje import MessageForm
from models.messages import Messages
from utilss.db import db

spa = Blueprint("spa", __name__)

@spa.route("/", methods=["GET", "POST"])
def home():
    form = MessageForm() 
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        message = form.message.data
        newMsg = Messages(firstname, lastname, email, message)
        db.session.add(newMsg)
        db.session.commit()
        
    return render_template("spa/home.html", form=form) 

@spa.route("/messages")
def messages():
    messages = Messages.query.all()
    return render_template("spa/messages.html", messages=messages)
