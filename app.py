import subprocess
import time
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

@app.route('/')
def home():
    return "Server Flask attivo su Render!"
app = Flask(__name__)
CORS(app)  # Abilita CORS

@app.route('/start', methods=['GET'])
def start_calculator():
    if os.environ.get("RUNNING_ON_RENDER") != "1":
        subprocess.Popen(['python', 'righello_adv.py'], shell=True)
    time.sleep(1)
    return "Roboclick avviato"

@app.route('/press', methods=['POST'])
def press_key():
    key = request.json.get('key')
    if key:
        return jsonify({"status": "ok", "key": key})
    return "Chiave non valida", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Porta dinamica su Render
    app.run(host='0.0.0.0', port=port)
