from flask import Blueprint, request, jsonify, current_app
from dalle_api_call import create_images
from env.secrets import APP_USERNAME, APP_PASSWORD
import jwt
from datetime import datetime, timedelta
from functools import wraps


b0 = Blueprint('GenerateImages', __name__)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'token is missing'}), 401 #unauthorized
        try:
            data = jwt.decode(token.split()[1], current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except Exception as e:
            return jsonify({'error':'invalid token'}), 403 #forbidden
        return f(*args, **kargs)
    return decorator



@b0.route('/prompt/<string:prompt>')
@token_required
def getImages(prompt):
    return create_images(prompt)


@b0.route('/login', methods=['POST'])
def login():
    if request.form['username'] == APP_USERNAME and request.form['password'] == APP_PASSWORD:
        
        token = jwt.encode({
          'user': request.form['username'],
          'exp': datetime.utcnow() + timedelta(days=30)
        },
        current_app.config['SECRET_KEY']
        )
        return jsonify({'token': token.encode().decode('utf-8')})
    return jsonify({'error': 'unable to verify'}), 401 #unauthorized

  
