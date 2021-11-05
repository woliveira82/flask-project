from flask import jsonify, request
from webargs import fields
from webargs.flaskparser import parser

from .. import tests


@tests.route('/tests', methods=['GET'])
def get_tests():
    return 'ok'


@tests.route('/test-params', methods=['GET'])
def get_tests_params():
    query = parser.parse({
        'param': fields.Str(required=True)
    }, request, location='query')

    return jsonify(query)
