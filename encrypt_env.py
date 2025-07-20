from cryptography.fernet import Fernet

# Generate and save encryption key
key = Fernet.generate_key()
with open("env.key", "wb") as key_file:
    key_file.write(key)

# Read the .env file to encrypt
with open(".env", "rb") as f:
    env_data = f.read()

# Encrypt the .env content
fernet = Fernet(key)
encrypted_data = fernet.encrypt(env_data)

# Save the encrypted result
with open("encrypted.env", "wb") as enc_file:
    enc_file.write(encrypted_data)

print("✅ .env has been encrypted → encrypted.env")
print("🔑 Key saved as env.key — keep it secure!")
