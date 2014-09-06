import os
from flask import Flask, jsonify
from flask.ext import restful
import nfl_teams

app = Flask(__name__)
api = restful.Api(app)


#objects
class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}


class nfl(restful.Resource):
    def get(self):

        foo = {
            'SEA': 'Seattle Seahawks',
            'DEN': 'Denver Broncos',
            'NE': 'New England Patriots',
            'GB': 'Green Bay Packers',
            'PHI': 'Philadelphia Eagles',
            'NO': 'New Orleans Saints',
            'SF': 'San Francisco 49ers',
            'SD': 'San Diego Chargers',
            'CIN': 'Cincinnati Bengals',
            'IND': 'Indianapolis Colts',
            'ATL': 'Atlanta Falcons',
            'BAL': 'Baltimore Ravens',
            'CHI': 'Chicago Bears',
            'MIA': 'Miami Dolphins',
            'PIT': 'Pittsburgh Steelers',
            'TB': 'Tampa Bay Buccaneers',
            'CAR': 'Carolina Panthers',
            'TEN': 'Tennessee Titans',
            'MIN': 'Minnesota Vikings',
            'KC': 'Kansas City Chiefs',
            'DET': 'Detroit Lions',
            'HOU': 'Houston Texans',
            'NYG': 'New York Giants',
            'DAL': 'Dallas Cowboys',
            'ARI': 'Arizona Cardinals',
            'CLE': 'Cleveland Browns',
            'BUF': 'Buffalo Bills',
            'WAS': 'Washington Redskins',
            'STL': 'St. Louis Rams',
            'OAK': 'Oakland Raiders',
            'NYJ': 'New York Jets',
            'JAX': 'Jacksonville Jaguars'
        }
        return foo

#endpoints
api.add_resource(HelloWorld, '/')
api.add_resource(nfl, '/nfl')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)