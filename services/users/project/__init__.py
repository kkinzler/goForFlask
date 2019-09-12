from flask import Flask, jsonify
from flask_restful import Resource, Api

#the flask object
app = Flask(__name__)

#the (REST)Api object
api = Api(app)

#the configuration
app.config.from_object('project.config.DevelopmentConfig')


class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
        }

api.add_resource(UsersPing, '/users/ping')
