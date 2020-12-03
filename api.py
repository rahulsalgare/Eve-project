from eve import Eve
from my_auth import Authenticate
from hooks.users import create_user

app = Eve(auth=Authenticate)
app.on_insert_users += create_user

if __name__ == '__main__':
    app.run()