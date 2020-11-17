from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mail import Mail
from ..constants import SECRET_KEY, ENVIRONMENT, DATABASE_NAME, DATABASE_HOST, DATABASE_PORT, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_USE_SSL, MAIL_USE_TLS
import os

app = Flask(__name__, template_folder=os.path.dirname(__file__) + "/../templates")

app.secret_key = SECRET_KEY
app.env = ENVIRONMENT
app.config['MONGODB_SETTINGS'] = {
    "db": DATABASE_NAME,
    "host": DATABASE_HOST,
    "port": int(DATABASE_PORT)
}

app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS

mail = Mail(app)

mongo = MongoEngine(app)
