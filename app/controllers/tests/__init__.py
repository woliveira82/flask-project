from flask import Blueprint

tests = Blueprint('tests', __name__)

from .apis import *
