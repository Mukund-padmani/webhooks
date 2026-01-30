

from flask import Blueprint, request, jsonify, render_template
from extensions import collection

webhook_bp = Blueprint('webhook_bp', __name__)

# Home route
@webhook_bp.route("/")
def home():
    return render_template("index.html")  # do NOT include "./templates/"

# Webhook route
@webhook_bp.route("/webhook", methods=["POST"])
def github_webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.json

    data = None

    # PUSH EVENT
    if event_type == "push":
       data = {
            "request_id": payload["head_commit"]["id"],
            "author": payload["pusher"]["name"],
            "action": "PUSH",
            "from_branch": payload["ref"].split("/")[-1],
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": payload["head_commit"]["timestamp"]
        }

    # PULL REQUEST
    elif event_type == "pull_request":
        action = payload["action"]
        pr = payload["pull_request"]

        # Merge
        if action == "closed" and pr["merged"]:
            data = {
                "request_id": str(pr["id"]),
                "author": pr["user"]["login"],
                "action": "MERGE",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": pr["merged_at"]
            }

        # PR opened
        elif action == "opened":
            data = {
                "request_id": str(pr["id"]),
                "author": pr["user"]["login"],
                "action": "PULL_REQUEST",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": pr["created_at"]
            }

    if not data:
        return jsonify({"message": "Event ignored"}), 200

    collection.insert_one(data)
    return jsonify({"message": "Event stored"}), 200
    pass

# API for UI
@webhook_bp.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find({}, {"_id": 0}).sort("timestamp", -1))
    return jsonify(events)
    pass


@webhook_bp.route("/logs", methods=["GET"])
def get_events():
    events = list(collection.find({}, {"_id": 0}).sort("timestamp", -1))
    return jsonify(events)
    pass
