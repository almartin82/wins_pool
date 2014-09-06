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

class nfl_teams(restful.Resource):
    def get(self):
        return jsonify(nfl_teams)

#endpoints
api.add_resource(HelloWorld, '/')
api.add_resource(nfl_teams, '/nfl')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)