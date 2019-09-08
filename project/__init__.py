import os
from flask import Flask, jsonify
from flask_swagger import swagger
from .config import Config
from flask_restful import Api
from .user.endpoint import UserItem
from .user.endpoint import UserIndex
from .app import app, api
from .agencies.endpoint import AgenciesItem
from .agencies.endpoint import AgenciesIndex
from .token import Token # token is a view

# app = Flask(Config.APP_NAME)
# api = Api(app)

# ALL API resource
api.add_resource(UserItem, '/user/<int:user_id>')
api.add_resource(UserIndex, '/user')

@app.route("/")
def spec():
    return jsonify(swagger(app))
