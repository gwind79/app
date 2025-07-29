import subprocess
import time
from flask import Flask, request, jsonify
from flask_cors import CORS  # <--- IMPORTA QUESTO

app = Flask(__name__)

@app.route('/start', methods=['GET'])
def start_calculator():
    if os.environ.get("RUNNING_ON_RENDER") != "1":
      subprocess.Popen(['python', 'script_locale.py'], shell=True)
    time.sleep(1)
    return "Roboclick avviato"

@app.route('/press', methods=['POST'])
def press_key():
    key = request.json.get('key')
    if key:
        return f"Premuto: {key}"
    return "Chiave non valida", 400

if __name__ == '__main__':
    app.run(host='https://app-1-anm0.onrender.com/', port=5000)
    #app.run(host='80.21.248.146', port=5000)
    
