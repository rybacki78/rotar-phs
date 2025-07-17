from flask import Blueprint, request, jsonify
from models import Project

project = Blueprint("project", __name__, url_prefix="/api")


@project.route("/sync_projects", methods=["POST"])
def sync_projects():
    pass


@project.route("/get_projects", methods=["GET"])
def get_projects():
    project = request.args.get("project")

    if project:
        query = Project.query.filter_by(project=project)

    projects = query.all()
    json_projects = [project.to_json() for project in projects]

    return jsonify({"project": json_projects})
