from flask import Blueprint, jsonify

task_routes = Blueprint("tasks", __name__)

tasks = []

@task_routes.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)
