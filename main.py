from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/performance')
def get_performance():
    payload = {
        "current_date": "2024-05-23",
        "current_time": "7:57:22.10"
    }
    return jsonify(payload)   


app.run(debug=True)