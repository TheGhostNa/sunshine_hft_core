import os

from cryptography.fernet import Fernet


def load_encrypted_env(enc_file="encrypted.env", key_file="env.key"):
    with open(key_file, "rb") as kf:
        key = kf.read()

    fernet = Fernet(key)

    with open(enc_file, "rb") as ef:
        encrypted_data = ef.read()

    decrypted = fernet.decrypt(encrypted_data).decode()

    # Load decrypted lines as environment variables
    for line in decrypted.splitlines():
        if "=" in line:
            key, val = line.strip().split("=", 1)
            os.environ[key] = val

    print("🔓 Environment variables successfully loaded from encrypted.env")
