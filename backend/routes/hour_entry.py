from flask import Blueprint, request, jsonify
from config import db
from models import HourEntry
from datetime import datetime

hour_entry = Blueprint("hour_entry", __name__, url_prefix="/api")


@hour_entry.route("/hour_entry", methods=["GET"])
def get_hour_entry():
    id = request.args.get("id")
    user = request.args.get("user")
    project = request.args.get("project")
    done_at = request.args.get("doneAt")

    query = HourEntry.query

    if id:
        query = query.filter_by(id=id)
    if user:
        query = query.filter_by(user=user)
    if project:
        query = query.filter_by(project=project)
    if done_at:
        try:
            done_at_date = datetime.strptime(done_at, "%Y-%m-%d").date()
            query = query.filter_by(done_at=done_at_date)
        except ValueError:
            return (
                jsonify({"message": "Invalid date format for doneAt. Use YYYY-MM-DD"}),
                400,
            )

    hour_entries = query.all()

    if not hour_entries:
        return jsonify({"message": "Hour entry not found"}), 404

    json_hour_entries = [entry.to_json() for entry in hour_entries]
    
    return jsonify({"hourEntry": json_hour_entries})


@hour_entry.route("/add_hour_entry", methods=["POST"])
def add_hour_entry():
    done_at = request.json.get("doneAt")
    project = request.json.get("project")
    quantity = request.json.get("quantity")
    user = request.json.get("user")

    if not done_at or not project or not quantity or not user:
        return jsonify({"message": "Hour entry is not valid"}), 400

    try:
        done_at_date = datetime.strptime(done_at, "%Y-%m-%d").date()
    except ValueError:
        return (
            jsonify({"message": "Invalid date format for doneAt. Use YYYY-MM-DD"}),
            400,
        )

    new_hour_entry = HourEntry(
        done_at=done_at_date,
        project=project,
        quantity=quantity,
        user=user,
        created_at=datetime.utcnow(),
        edited_at=datetime.utcnow(),
    )

    try:
        db.session.add(new_hour_entry)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Hour entry added"}), 201


@hour_entry.route("/update_hour_entry", methods=["PATCH"])
def edit_hour_entry():
    id = request.args.get("id")
    hour_entry = HourEntry.query.get(id)

    if not hour_entry:
        return jsonify({"message": "Hour entry not found"}), 404

    data = request.json

    done_at = data.get("doneAt")
    if done_at:
        try:
            hour_entry.done_at = datetime.strptime(done_at, "%Y-%m-%d").date()
        except ValueError:
            return (
                jsonify({"message": "Invalid date format for doneAt. Use YYYY-MM-DD"}),
                400,
            )

    hour_entry.project = data.get("project", hour_entry.project)
    hour_entry.quantity = data.get("quantity", hour_entry.quantity)
    hour_entry.user = data.get("user", hour_entry.user)
    hour_entry.edited_at = datetime.utcnow()

    db.session.commit()

    return jsonify({"message": "Hour entry updated"}), 200


@hour_entry.route("/delete_hour_entry", methods=["DELETE"])
def delete_hour_entry():
    id = request.args.get("id")
    hour_entry = HourEntry.query.get(id)

    if not hour_entry:
        return jsonify({"message": "Hour entry not found"}), 404

    db.session.delete(hour_entry)
    db.session.commit()

    return jsonify({"message": "Hour entry deleted"}), 200
