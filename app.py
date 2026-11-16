from flask import Flask, jsonify, request
from store import init_db, list_favorites
from favorites import add_favorite, remove_favorite

app = Flask(__name__)

init_db()


@app.route("/favorites", methods=["GET"])
def get_favorites():
    app_id = request.args.get("app_id")
    username = request.args.get("username")

    missing_fields = [
        name
        for name, value in [("app_id", app_id), ("username", username)]
        if not value
    ]


    if missing_fields:
        return jsonify({
            "success": False,
            "error": "Invalid fields",
            "fields": missing_fields
        }), 400

    favorites = list_favorites(app_id, username)

    return jsonify({"favorites": favorites}), 200


@app.route("/favorites", methods=["POST"])
def post_favorite():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(success=False, error="Invalid or missing JSON"), 400

    app_id = data.get("app_id")
    username = data.get("username")
    item_id = data.get("item_id")

    missing_fields = [
        name
        for name, value in [
            ("app_id", app_id),
            ("username", username),
            ("item_id", item_id)
        ]
        if not value
    ]

    if missing_fields:
        return jsonify(success=False, error="Invalid fields", fields=missing_fields), 400

    result = add_favorite(app_id, username, item_id)

    if result == "added":
        return jsonify({"success": True}), 201

    if result == "duplicate":
        return jsonify({
            "success": False,
            "error": "duplicate"
        }), 409


@app.route("/favorites/<item_id>", methods=["DELETE"])
def delete_favorite(item_id):
    app_id = request.args.get("app_id")
    username = request.args.get("username")

    missing_fields = [
        name
        for name, value in [
            ("app_id", app_id),
            ("username", username)
        ]
        if not value
    ]

    if missing_fields:
        return jsonify(success=False, error="Invalid fields", fields=missing_fields), 400

    result = remove_favorite(app_id, username, item_id)

    if result == "removed":
        return jsonify({"success": True}), 200

    if result == "not_found":
        return jsonify({
            "success": False,
            "error": "not_found"
        }), 404


if __name__ == "__main__":
    app.run(port=5002, debug=True)