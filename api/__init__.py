from flask import Flask
from flask.ext import restful
from endpoints import *

app = Flask(__name__)
api = restful.Api(app)

