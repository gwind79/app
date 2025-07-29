from flask import Flask, request, jsonify

app = Flask(__name__)
AUTH_TOKEN = "mio_token_sicuro"

@app.route('/press', methods=['POST'])
def press_key():
    token = request.headers.get('Authorization')
    if token != AUTH_TOKEN:
        return "Accesso negato", 403
    key = request.json.get('key')
    # Qui non esegui pyautogui, ma magari salvi o trasmetti il comando
    print(f"Comando ricevuto: {key}")
    return jsonify({"status": "ok", "key": key})

@app.route('/')
def home():
    return "Server Flask attivo!"

if __name__ == '__main__':
    app.run()
