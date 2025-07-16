from flask import request, jsonify
from config import app, db
from models import HourEntry
from datetime import datetime


@app.route("/hourentry", methods=["GET"])
def get_hourentry():
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
    json_hour_entries = [entry.to_json() for entry in hour_entries]
    return jsonify({"hourEntry": json_hour_entries})


@app.route("/addhourentry", methods=["POST"])
def add_hourentry():
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
    )

    try:
        db.session.add(new_hour_entry)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"meassge": "Hour entry added"}), 201

@app.route("/updatehourentry", methods=["PATCH"])
def edit_entry():
    id = request.args.get("id")
    hour_entry = HourEntry.query.get(id)
    
    if not hour_entry:
        return jsonify({"message": "Hour entry not found"}), 404
    
    