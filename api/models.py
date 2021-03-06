from flask.ext import restful


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}


class MyFavoriteRobots(restful.Resource):
    def get(self):
        return {'R2-D2': 'R-Too Dee-Too',
                'Johny 5': 'Is alive!'}


class nfl_teams(restful.Resource):
    def get(self):
        teams = {
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
        return teams