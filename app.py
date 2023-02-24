#!/usr/bin/python3
"""main app setup for Flask instance in REST API"""
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import app
from users.routes import create_authentication_routes

api = Api(app=app)
create_authentication_routes(api=api)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, threaded=True)
