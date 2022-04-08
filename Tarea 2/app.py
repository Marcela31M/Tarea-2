from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.spa import spa

app = Flask(__name__)
app.config.from_object("config.BaseConfig")

app.register_blueprint(spa)
SQLAlchemy(app)


