from flask import Blueprint, request, jsonify
from models import User
from user_sync import start_user_sync

user = Blueprint("user", __name__, url_prefix="/api")


@user.route("/sync_users", methods=["POST"])
def sync_users():

    success, message = start_user_sync()

    if success:
        return jsonify({"message": message}), 200

    else:
        return jsonify({"message": message}), 400


@user.route("/get_users", methods=["GET"])
def get_users():
    exact_number = request.args.get("exactNumber")
    in_phs = request.args.get("inPhs")

    query = User.query

    if exact_number:
        query = query.filter_by(exact_number=exact_number)

    if in_phs:
        query = query.filter_by(in_phs=in_phs)

    users = query.all()
    json_users = [user.to_json() for user in users]

    return jsonify({"user": json_users}), 200
