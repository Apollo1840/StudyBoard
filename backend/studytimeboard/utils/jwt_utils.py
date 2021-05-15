import jwt
import datetime
from dotenv import load_dotenv
import os

# JWT Constants
ALGORITHM = 'HS256'
# Load environments from .env into os
load_dotenv()
JWT_DURATION = os.getenv('JWT_DURATION')
JWT_SECRET = os.getenv('JWT_SECRET')

# Encode user id, user name into a json web token 
def jwt_encode(id,username):
    return jwt.encode({'id': str(id),
                      'username': username,
                      'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=int(JWT_DURATION))},
                      JWT_SECRET,
                      algorithm = 'HS256')

# Decode user id, user name from json web token
def jwt_decode(encoded_jwt):
    return jwt.decode(encoded_jwt, JWT_SECRET, algorithms=[ALGORITHM])

# Twins implementation of jwt_decode to have pythonic return value
def jwt_decode_identity(encoded_jwt):
    jwt_decoded = jwt_decode(encoded_jwt)
    return jwt_decoded["username"], jwt_decoded["id"]

# Check authentication of http reques by extracting and validate the jwt
def jwt_verify(jwt_encoded):
    try:
        jwt.decode(jwt_encoded, JWT_SECRET, algorithms = [ALGORITHM])
        return True
    except Exception as err: #there could be incalid signature or expire excaptions
        return False
