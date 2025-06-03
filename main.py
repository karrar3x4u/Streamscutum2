from flask import Flask, render_template
import threading
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def run_server():
    local_ip = socket.gethostbyname(socket.gethostname())
    app.run(host=local_ip, port=5000)

threading.Thread(target=run_server).start()