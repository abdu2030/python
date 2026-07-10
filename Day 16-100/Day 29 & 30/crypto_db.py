import base64
import json
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

current_dir = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(current_dir, "data.enc")

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 32-byte key from the master password and salt using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    # Fernet requires urlsafe base64-encoded key
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_data(data: dict, password: str) -> bytes:
    """Encrypt password dictionary into a single bytes payload: salt (16 bytes) + ciphertext."""
    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)
    json_bytes = json.dumps(data).encode("utf-8")
    ciphertext = fernet.encrypt(json_bytes)
    return salt + ciphertext

def decrypt_data(encrypted_payload: bytes, password: str) -> dict:
    """Decrypt the payload (salt + ciphertext) using the password.
    Raises ValueError or cryptography.fernet.InvalidToken on failure.
    """
    if len(encrypted_payload) < 16:
        raise ValueError("Database payload is too short.")
    salt = encrypted_payload[:16]
    ciphertext = encrypted_payload[16:]
    key = derive_key(password, salt)
    fernet = Fernet(key)
    decrypted_bytes = fernet.decrypt(ciphertext)
    return json.loads(decrypted_bytes.decode("utf-8"))

def db_exists() -> bool:
    """Check if the encrypted database file exists."""
    return os.path.exists(DB_FILE)

def load_db(password: str) -> dict:
    """Load and decrypt the database from disk.
    Raises exception if password incorrect or file doesn't exist.
    """
    with open(DB_FILE, "rb") as f:
        encrypted_payload = f.read()
    return decrypt_data(encrypted_payload, password)

def save_db(data: dict, password: str):
    """Encrypt and save the database to disk."""
    encrypted_payload = encrypt_data(data, password)
    with open(DB_FILE, "wb") as f:
        f.write(encrypted_payload)

def change_master_password(old_password: str, new_password: str) -> bool:
    """Decrypts database with old password, re-encrypts with new password, and saves.
    Returns True on success, False if old password incorrect.
    """
    try:
        data = load_db(old_password)
        save_db(data, new_password)
        return True
    except Exception:
        return False

def migrate_plaintext_db(password: str) -> bool:
    """Migrates existing data.json or data.txt to data.enc and deletes them.
    Returns True if migration took place, False otherwise.
    """
    migrated = False
    data = {}
    
    # 1. Try to read data.json
    json_file = os.path.join(current_dir, "data.json")
    if os.path.exists(json_file):
        try:
            with open(json_file, "r") as f:
                data = json.load(f)
            migrated = True
        except Exception:
            pass
        try:
            os.remove(json_file)
        except Exception:
            pass

    # 2. Try to read data.txt (pipe-separated)
    txt_file = os.path.join(current_dir, "data.txt")
    if os.path.exists(txt_file):
        try:
            with open(txt_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(" | ")
                    if len(parts) == 3:
                        web, email, pwd = parts
                        data[web] = {
                            "email": email,
                            "password": pwd
                        }
            migrated = True
        except Exception:
            pass
        try:
            os.remove(txt_file)
        except Exception:
            pass
            
    if migrated or not db_exists():
        save_db(data, password)
        return True
    return False
