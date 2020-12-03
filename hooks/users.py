import bcrypt

def create_user(documents):
    '''
    hash the password before storing it to db
    '''
    for document in documents:
        document['salt'] = bcrypt.gensalt()
        password =  document['password'].encode('utf-8')
        document['password'] = bcrypt.hashpw(password, document['salt'])