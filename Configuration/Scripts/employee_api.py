from flask import Flask, request, jsonify
import json

app = Flask(__name__)

GROUP_MAP_FILE = "/home/webadmin/cyberlab-identity/group_map.json"

@app.route("/get-policy", methods=["GET"])
def get_policy():

    email = request.args.get("email", "").lower()

    with open(GROUP_MAP_FILE, "r") as file:
        employees = json.load(file)

    employee = employees.get(email)

    if not employee:
        return jsonify({"error": "User not authorized"}), 403

    return jsonify({
        "name": employee["name"],
        "group": employee["group"],
        "port": employee["port"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)