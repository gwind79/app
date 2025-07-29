from flask import Flask, request
import pyautogui
import subprocess
import time

app = Flask(__name__)
AUTH_TOKEN = "mio_token_sicuro"

@app.route('/start', methods=['GET'])
def start_calculator():
    subprocess.Popen(['python', 'script_locale.py'], shell=True)
    time.sleep(1)
    return "Applicazione avviata"

@app.route('/press', methods=['POST'])
def press_key():
    token = request.headers.get('Authorization')
    if token != AUTH_TOKEN:
        return "Accesso negato", 403
    key = request.json.get('key')
    if key:
        pyautogui.press(key)
        return f"Premuto: {key}"
    return "Chiave non valida", 400

if __name__ == '__main__':
    app.run()
