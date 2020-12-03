from schemas.user import user_schema

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'eveproj'


RESOURCE_METHODS = ['GET', 'POST']

ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

users = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'schema': user_schema,
}

DOMAIN = {
    'users': users
}