from flask import Flask
from flask_restful import Api
from .endpoints import GenerateImages

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(GenerateImages, '/<string:prompt>')
    return app