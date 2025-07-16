from flask import Blueprint, request, jsonify
from config import db
from models import Project
from datetime import datetime

project = Blueprint("project", __name__, url_prefix="/api")


@project.route("/sync_projects", methods=["POST"])
def sync_projects():
    pass


@project.route("/get_projects", methods=["POST"])
def get_projects():
    pass
