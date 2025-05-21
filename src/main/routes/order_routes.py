from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.middleware.authentication import jwt_auth_verification
from src.main.composer.order_register_composer import order_register_composer
from src.main.composer.list_orders_composer import list_orders_composer
from src.errors.error_handler import error_handler

order_routes_bp = Blueprint("order_routes", __name__)

@order_routes_bp.route("/order/registry/<user_id>", methods =["POST"])
def registry(user_id):
    try:
        token_info = jwt_auth_verification()
        http_request = HttpRequest(
                            body=request.json,
                            params={"user_id": user_id},
                            headers=request.headers, 
                            token_infos=token_info
                        )
        view = order_register_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = error_handler(exception)
        return jsonify(http_response.body), http_response.status_code

@order_routes_bp.route("/order/list/<user_id>", methods =["GET"])
def list_orders(user_id):
    try:
        token_info = jwt_auth_verification()
        http_request = HttpRequest(
                            params={"user_id": user_id},
                            headers=request.headers, 
                            token_infos=token_info
                        )
        view = list_orders_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = error_handler(exception)
        return jsonify(http_response.body), http_response.status_code
