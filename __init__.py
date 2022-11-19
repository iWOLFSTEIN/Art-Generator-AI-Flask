from flask import Flask
from .endpoints import b0
from .env.secrets import SECRET_KEY

def create_app():
    app = Flask(__name__)


    app.config['SECRET_KEY'] = SECRET_KEY


    app.register_blueprint(b0)


    return app