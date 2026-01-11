from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    html = "<h3>Hello de mon app personnalisée!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Message:</b> {msg}"
    return html.format(
        hostname=socket.gethostname(),
        msg=os.getenv("APP_MSG", "Pas de message configuré")
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
