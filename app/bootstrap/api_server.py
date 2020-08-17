from flask import Flask
from ..constants import SECRET_KEY, ENVIRONMENT

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.env = ENVIRONMENT
