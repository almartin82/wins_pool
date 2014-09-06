import os
from flask import Flask
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
        return nfl_teams.nfl_teams

#endpoints
api.add_resource(HelloWorld, '/')
api.add_resource(nfl, '/nfl')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)