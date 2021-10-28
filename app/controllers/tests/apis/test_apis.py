from .. import tests

@tests.route('/tests', methods=['GET'])
def get_tests():
    return 'ok'
