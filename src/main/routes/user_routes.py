from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.login_enabler_composer import login_enabler_composer
from src.main.composer.list_users_composer import list_users_composer

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/user/registry", methods =["POST"])
def registry():
    http_request = HttpRequest(body=request.json)
    view = user_register_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route("/user/login", methods =["POST"])
def login():
    http_request = HttpRequest(body=request.json)
    view = login_enabler_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route("/user/list", methods =["GET"])
def list_all():
    http_request = HttpRequest()
    view = list_users_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
