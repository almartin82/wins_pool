from . import app, api
from models import *

api.add_resource(HelloWorld, '/')
api.add_resource(nfl_teams, '/nfl')

