from flask import request, jsonify
from . import bp as api
from app.blueprints.users.models import User
from .auth import token_auth

@api.route('/register', methods=['POST'])
def register_user():
    """
    [POST] /api/register
    """
    
    data = reques.get_json(force=True)
    print(type(request.get_json()))
    
    user = User(data['username'], data['displayname'], data['password'], data['email'])
    user = save()
    return jsonify(user.to_dict())

@api.route('/profile', methods['GET'])
@token_auth.login_required
def get_profile():
    """
    [GET] /profile
    """
    user=token_auth.current_user
    return jsonify(user.to_dict())

@api.route('/profile', methods=['PUT'])
@token_auth.login_required
def edit_profile():
    """
    [PUT] /profile/
    """
    user = token_auth.current_user()
    data = request.get_json(force=True)
    user.from_dict(data)
    user.save()
    return jsonify(user.to_dict())