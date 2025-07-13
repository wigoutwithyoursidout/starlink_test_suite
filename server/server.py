# server/server.py
from flask import Flask, jsonify
from datetime import datetime  # For timestamps
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'message': 'pong',
        'server_timestamp': datetime.now(ZoneInfo("Australia/Sydney")).isoformat(),
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)