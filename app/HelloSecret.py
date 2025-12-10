from cryptography.fernet import Fernet
import os
from flask import Flask, Response

app = Flask(__name__)

FERNET_KEY = os.environ.get("FERNET_KEY")
SECRET_CIPHERTEXT = os.environ.get("SECRET_CIPHERTEXT")

if not FERNET_KEY or not SECRET_CIPHERTEXT:
    raise ValueError("Faltan variables de entorno")

fernet = Fernet(FERNET_KEY.encode())
secret = fernet.decrypt(SECRET_CIPHERTEXT.encode()).decode()

@app.route("/")
def index():
    return Response(f"Hola nrj0005, tu secreto es: {secret}", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
