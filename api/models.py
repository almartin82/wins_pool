from flask.ext import restful
from api.data import nfl_teams

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

class nfl_teams(restful.Resource):
    def get(self):
        return nfl_teams.nfl_team_data