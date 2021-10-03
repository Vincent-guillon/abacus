from flask import Flask, jsonify, Blueprint, send_from_directory
from flask_jwt_extended import JWTManager
from api.api import api_bp
from database.database import *

from api.api import init_swagger


app = Flask(__name__)
app.register_blueprint(api_bp)
#app.config["JWT_SECRET_KEY"] = "I4gc/Yv3P27d/m7Qczbe+JadO+G6cu9DnA7WXEbTfqo="
JWT_DECODE_ALGORITHMS = ['HS512', 'RS256']
jwt = JWTManager(app)

with app.app_context():
    init_swagger(app)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

def create_app():
    conn = init_databases()
    app.run(debug=True)

if __name__ == "__main__":
    create_app()