from flask import Blueprint, request, jsonify, current_app
from .dalle_api_call import create_images
from .env.secrets import APP_USERNAME, APP_PASSWORD
import jwt
from datetime import datetime, timedelta
from functools import wraps


b0 = Blueprint('GenerateImages', __name__)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'error': 'token is missing'})
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
        except:
            jsonify({'error':'invalid token'})
    return decorator



@b0.route('/prompt')
@token_required
def getImages():
    return create_images(request.form['prompt'])


@b0.route('/login', methods=['POST'])
def login():
    if request.form['username'] == APP_USERNAME and request.form['password'] == APP_PASSWORD:
        
        token = jwt.encode({
          'user': request.form['username'],
          'expiration': str(datetime.utcnow() + timedelta(weeks=4))
        },
        current_app.config['SECRET_KEY']
        )
        return jsonify({'token': token.encode().decode('utf-8')})
    return jsonify({'error': 'unable to verify'})

  
