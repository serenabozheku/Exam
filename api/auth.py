from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/', methods=['GET', 'POST'])

def get_param(param):
    if param='Test': 
        return'Success', 200
    return'Fail', 403

def post_param(param):
    return param

def params():
    if request.method == 'GET':
        return get_param()
    return post_param()