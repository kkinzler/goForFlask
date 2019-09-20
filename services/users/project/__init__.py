import os
#from flask import Flask, jsonify
#from flask_restful import Resource, Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




#the database object
db = SQLAlchemy()



def create_app(script_info=None):
    
    #the flask object
    app = Flask(__name__)

    #the configration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    #the blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    #the cli context for the flask and database objects
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}


    return app















"""

#the flask object
app = Flask(__name__)

#the (REST)Api object
api = Api(app)

#the configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

#the database
db = SQLAlchemy(app)



#the database model(structure)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


#the web page
class UsersPing(Resource):
    def get(self):
        return {
        'status': 'sucksass',
        'message': 'pong!'
        }

#the page to display and the route
api.add_resource(UsersPing, '/users/ping')

"""
