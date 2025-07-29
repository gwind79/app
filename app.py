from flask import Flask, request
import subprocess
import pyautogui
import time

app = Flask(__name__)

@app.route('/start', methods=['GET'])
def start_calculator():
    #subprocess.Popen('calc.exe')
    path = os.getcwd()
    path1 = os.path.join('python', "righello_adv.py") 
    subprocess.Popen(path1)
    time.sleep(1)
    return "Roboclick avviato"

@app.route('/press', methods=['POST'])
def press_key():
    key = request.json.get('key')
    if key:
        pyautogui.press(key)
        return f"Premuto: {key}"
    return "Chiave non valida", 400

if __name__ == '__main__':
    app.run(host='https://app-1-anm0.onrender.com/', port=5000)
    #app.run(host='80.21.248.146', port=5000)
    
