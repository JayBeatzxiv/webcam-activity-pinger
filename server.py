from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
import logging

app = Flask(__name__)

logging.basicConfig(filename='camera_events.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

camera_state = {
    "active": False,
    "last_update": None
}

@app.route('/camera', methods=['PATCH'])
def camera_ping():
    camera_state["active"] = True
    camera_state["last_update"] = datetime.utcnow()
    log_message = "📷 Camera is active."
    print(log_message)
    logging.info(log_message)
    return jsonify({"status": "active"}), 200

@app.route('/camera/stop', methods=['POST'])
def camera_stop():
    camera_state["active"] = False
    camera_state["last_update"] = datetime.utcnow()
    log_message = "🛑 Camera stopped."
    print(log_message)
    logging.info(log_message)
    return jsonify({"status": "stopped"}), 200

@app.route('/status', methods=['GET'])
def status():
    status_text = "ON ✅" if camera_state["active"] else "OFF ❌"
    last_updated = camera_state["last_update"].strftime('%Y-%m-%d %H:%M:%S') if camera_state["last_update"] else "Never"
    html = f"""
    <html>
        <head><title>Camera Status</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>Camera is currently: <span style="color:{'green' if camera_state["active"] else 'red'}">{status_text}</span></h1>
            <p>Last update: {last_updated} UTC</p>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
