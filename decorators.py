from flask import request
from flask_restx import abort
import jwt

import constants


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)  # Access denied

        data = request.headers['Authorization']
        # Выделение токена из заголовка Authorization
        token = data.split("Bearer ")[-1]
        # Попытка декодирования токена
        try:
            jwt.decode(token, constants.TKN_SECRET, algorithms=[constants.TKN_ALGO])
        except Exception as e:
            print(f'Token decode failure - ({e})\nAborting')
            abort(401)
        return func(*args, **kwargs)  # продолжение работы, если токен декодирован успешно
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)  # Access denied

        data = request.headers['Authorization']
        # Выделение токена из заголовка Authorization
        token = data.split("Bearer ")[-1]
        # Попытка декодирования токена
        try:
            user = jwt.decode(token, constants.TKN_SECRET, algorithms=[constants.TKN_ALGO])
            role = user.get('role')
            if role != 'admin':
                print(f'Role {role} is not admin\nAborting')
                abort(401)
        except Exception as e:
            print(f'Token decode failure - ({e})\nAborting')
            abort(401)
        return func(*args, **kwargs)
    return wrapper
