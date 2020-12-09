"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/users', methods=['GET'])
def list_users():
    users = []

    for user in User.query.all():
        users.append(user.serialize())

    return jsonify(users), 200


@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)

    if not user:
        return "User not found", 404

    return jsonify(user.serialize()), 200


@api.route('/users', methods=['POST'])
def create_user():
    payload = request.get_json()
    user = User(**payload)

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 201


@api.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    if not user:
        return "User not found", 404

    payload = request.get_json()

    user.first_name = payload['first_name']
    user.email = payload['email']
    user.password = payload['password']
    user.is_active = payload['is_active']

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 200


@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    if not user:
        return "User not found", 404

    data = user.serialize()

    db.session.delete(user)
    db.session.commit()

    return jsonify(data), 200