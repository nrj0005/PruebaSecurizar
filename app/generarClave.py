from cryptography.fernet import Fernet

# Generar clave
key = Fernet.generate_key()
f = Fernet(key)

# Secreto en texto plano
secret = "me gustan las tostadas".encode()

# Cifrarlo
cipher = f.encrypt(secret)

print("FERNET_KEY =", key.decode())
print("SECRET_CIPHERTEXT =", cipher.decode())
