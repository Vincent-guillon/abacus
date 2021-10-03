from flask import Flask, request, jsonify, Blueprint, current_app
from flask_restful import Resource, Api, reqparse
from api.resources.Bills import Bills

from flask_swagger_ui import get_swaggerui_blueprint


#Creer un blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

def init_swagger(app):
    ### swagger specific ###
    SWAGGER_URL = '/api'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Abacus"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

api.add_resource(Bills, '/bills')

