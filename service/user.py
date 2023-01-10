import base64

import constants
from dao.user import UserDAO
import hashlib
import hmac


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_user(self, username):
        return self.dao.get_user(username)

    def create(self, user_data):
        user_data['password'] = self.pwd_hashing(user_data.get('password'))
        return self.dao.create(user_data)

    def update(self, user_data):
        user_data['password'] = self.pwd_hashing(user_data.get('password'))
        self.dao.update(user_data)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def pwd_hashing(self, password):
        pwd_hash = hashlib.pbkdf2_hmac(
            constants.HASH_NAME,
            password.encode('utf-8'),  # Convert the password to bytes
            constants.PWD_HASH_SALT,
            constants.PWD_HASH_ITERATIONS
        )
        return base64.b64encode(pwd_hash)

    def passwords_compare(self, hash_pwd, req_pwd):
        return hmac.compare_digest(base64.b64decode(hash_pwd),
                                   hashlib.pbkdf2_hmac(constants.HASH_NAME,
                                                       req_pwd.encode('utf-8'),
                                                       constants.PWD_HASH_SALT,
                                                       constants.PWD_HASH_ITERATIONS
                                                       )
                                   )
