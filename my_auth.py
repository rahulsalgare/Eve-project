import bcrypt
from eve.auth import BasicAuth
from flask import current_app as app

class Authenticate(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        if resource == 'users' and method == 'GET':
            users = app.data.driver.db['users']
            user = users.find_one({'username': username})

            # return True if user else False
            salt = bcrypt.gensalt()
            pswd = password.encode('utf-8')
            hashed = bcrypt.hashpw(pswd, salt)

            return user and bcrypt.hashpw(pswd, user['password']) == user['password']
                

        else:
            return True
