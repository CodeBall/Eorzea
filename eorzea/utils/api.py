from flask import jsonify


class APIStatus:

    OK = (200, 'Ok')
    BAD_REQUEST = (400, 'Bad request')
    UNAUTHORIZED = (401, 'Unauthorized')
    FORBIDDEN = (403, 'Forbidden')
    NOT_FOUND = (404, 'Not found')


def jsonify_with_data(status, **kwargs):
    resp = {'data': kwargs, 'message': status[1], 'code': status[0]}
    return jsonify(resp), status[0]


def jsonify_with_error(status, errors=None):
    resp = {'message': status[1], 'code': status[0]}
    if errors:
        resp['errors'] = errors
    return jsonify(resp), status[0]
