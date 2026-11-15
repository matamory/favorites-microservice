from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/favorites", methods=["GET"])
def get_favorites():
    return jsonify({"message": "Get favorites"})


@app.route("/favorites", methods=["POST"])
def add_favorite():
    return jsonify({"message": "Add favorite"})


@app.route("/favorites/<item_id>", methods=["DELETE"])
def remove_favorite(item_id):
    return jsonify({"message": "Remove favorite " + item_id})


if __name__ == "__main__":
    app.run(port=5002, debug=True)