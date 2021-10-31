from os import getenv


ENV = getenv('FLASK_ENV', 'development')
DEBUG = bool(getenv('FLASK_DEBUG', True))

# Installend Blueprints
BLUEPRINT_LIST = (
    {'package': 'tests', 'name': 'tests', 'version': 1},
)
