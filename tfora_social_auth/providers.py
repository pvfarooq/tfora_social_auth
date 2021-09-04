from google.auth.transport import requests
from google.oauth2 import id_token
import facebook
from .utils import get_social_app_credentials


class Google:
    @staticmethod
    def validate(auth_token):
        idinfo = id_token.verify_oauth2_token(
            auth_token, requests.Request(), get_social_app_credentials("google").client_id)
        if 'accounts.google.com' in idinfo['iss']:
            return idinfo


class Facebook:
    @staticmethod
    def validate(auth_token):
        try:
            graph = facebook.GraphAPI(access_token=auth_token)
            profile = graph.request(
                '/me?fields=name,email,first_name,last_name,middle_name,picture,id')
            return profile
        except:
            return "The token is either invalid or has expired"