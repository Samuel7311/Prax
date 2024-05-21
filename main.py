from flask import Flask, request


app = Flask(__name__)


@app.route('/performance', methods=['POST'])

def set_performance():
    print("Obdrzal som POST request na /performance...")
    payload = request.json
    
    return "Ok", 200

@app.route('/performance', methods=['GET'])
def show_performance():
    return "okok"

app.run(debug=True, host="0.0.0.0", port="3000")