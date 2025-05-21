from flask import Blueprint

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/user/registry", methods =["POST"])
def registry():
    pass