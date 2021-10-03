import requests
from flask import request
from flask_restful import Resource, reqparse
from flask import current_app
from core.utils import get_token
from database.database import *

class Login(Resource):
    root_parser = reqparse.RequestParser()
    def post(self):
        #Force the request to parse json
        request.get_json(force=True)

        Login.root_parser.add_argument('login', type=dict, required=True)
        root_args = Login.root_parser.parse_args()


        #Parse arguments inside health
        nested_login_parser = reqparse.RequestParser()
        nested_login_parser.add_argument('login', type=str, required=True, location=('login',))
        nested_login_parser.add_argument('password', type=str, required=True, location=('login',))
        nested_login_args = nested_login_parser.parse_args(req=root_args)

        login_json = {
            "email": nested_login_args.email,
            "password": nested_login_args.password
        }

        try:
            response = requests.post("http://"+chirpstackHost+":"+str(chirpstackPort)+"/api/internal/login", json=login_json)
            if response.status_code == 200:
                return response.json()
            else:
                return "Endpoint error :"+str(response.status_code)
        except:
            return "Error contacting Chirpstack. Please check your server status."
