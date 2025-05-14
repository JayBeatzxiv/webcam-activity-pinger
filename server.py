from flask import Flask, request, jsonify

app = Flask(__name__)

camera_state = {
    "active": False
}

@app.route('/camera', methods=['PATCH'])
def camera_ping():
    camera_state["active"] = True
    print("📷 Camera is active.")
    return jsonify({"status": "active"}), 200

@app.route('/camera/stop', methods=['POST'])
def camera_stop():
    camera_state["active"] = False
    print("🛑 Camera stopped.")
    return jsonify({"status": "stopped"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
