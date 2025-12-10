from cryptography.fernet import Fernet
import os

def main():
    key = os.environ.get("FERNET_KEY")
    ciphertext = os.environ.get("SECRET_CIPHERTEXT")

    if not key or not ciphertext:
        print("ERROR: faltan variables de entorno.")
        return

    f = Fernet(key.encode())
    secret = f.decrypt(ciphertext.encode()).decode()

    print(f"Hola nrj0005, tu secreto es: {secret}")

if __name__ == "__main__":
    main()
