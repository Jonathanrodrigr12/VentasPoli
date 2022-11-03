from app.constants_file import Constants
from fastapi.param_functions import Header
from app.utils.entities.entity_customer import ResponseException
import jwt
import datetime


class SecurityUtil:

    @staticmethod
    def get_key():
        """Get key secret"""
        return Constants.secret
    
    @staticmethod
    def get_algorithms():
        """Get algorithm the encryption"""
        return  Constants.algoritm

    @staticmethod
    def get_token(value, expiration=28800):
        """Create token with expiration"""
        token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration), 'val': value}, 
                          SecurityUtil.get_key(), SecurityUtil.get_algorithms())
        return token

    @staticmethod
    def validate_token(token_passed: str = Header("token")):
        """Validate that the token is succesfull"""
        if token_passed:
            try:
                data = jwt.decode(token_passed,SecurityUtil.get_key(),
                            SecurityUtil.get_algorithms())
                return (True, token_passed, data['val'])
            except jwt.exceptions.ExpiredSignatureError:
                raise ResponseException(status=401, details=[{'message': "Expired token, please send a valid token", 'status': "error"}]
            , data=[])
            except Exception as e:
                raise ResponseException(status=401, details=[{'message': "Invalid Token", 'status': "error"}], data=[])
        raise ResponseException(status=401, details=[{'message': "Invalid Token", 'status': "error"}], data=[])