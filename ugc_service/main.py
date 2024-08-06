from flask import Flask
from api.tracking import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/tracking')
