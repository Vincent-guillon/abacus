from flask import request, current_app, Response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from database.database import *
import json

class Bills(Resource):
    root_parser = reqparse.RequestParser()

    @jwt_required()
    def get(self):
        jwt = get_token(current_app)
        return 'Worked'
        dddd

