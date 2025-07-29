from flask import Flask, request, jsonify
from flask_cors import CORS  # <--- IMPORTA QUESTO

app = Flask(__name__)
CORS(app)  # <--- ABILITA CORS PER TUTTE LE ROTTE

AUTH_TOKEN = "mio_token_sicuro"

@app.route('/')
def home():
    return "Server Flask attivo su Render!"

@app.route('/press', methods=['POST'])
def press_key():
    token = request.headers.get('Authorization')
    if token != AUTH_TOKEN:
        return "Accesso negato", 403
    key = request.json.get('key')
    print(f"Comando ricevuto: {key}")
    return jsonify({"status": "ok", "key": key})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
