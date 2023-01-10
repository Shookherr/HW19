from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthService(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('username')
        pwd_req = req_json.get('password')

        if None in [username, pwd_req]:
            return 'Username or password is missing.', 401

        return auth_service.token_generate(username, pwd_req), 201

    def put(self):
        req_json = request.json
        token = req_json.get('refresh_token')  # токен из запроса
        tokens = auth_service.approve_refresh_token(token)  # генерация токенов
        return tokens, 201
