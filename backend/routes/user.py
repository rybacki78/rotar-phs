from flask import Blueprint, request, jsonify
from config import db
from models import User
from user_sync import start_user_sync

user = Blueprint("user", __name__, url_prefix="/api")


@user.route("/sync_users", methods=["POST"])
def sync_users():

    try:
        start_user_sync()

    except Exception as e:

        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Users has been synced"}), 200


@user.route("/get_users", methods=["GET"])
def get_users():
    exact_number = request.args.get("exactNumber")

    query = User.query

    if exact_number:
        query = query.filter_by(exact_number=exact_number)

    users = query.all()
    json_users = [user.to_json() for user in users]

    return jsonify({"user": json_users})
