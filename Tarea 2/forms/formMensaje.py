from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms.fields import StringField, SubmitField

class MessageForm(FlaskForm):
    firstname = StringField(
            "Firstname",
            validators=[
                InputRequired()
                ]
            )

    lastname = StringField(
            "lastname",
            validators=[
                InputRequired()
                ]
            )

    email= StringField(
            "email",
            validators=[
                InputRequired()
                ]
            )

    message= StringField(
            "message",
            validators=[
                InputRequired()
                ]
            )

    submit=SubmitField()

