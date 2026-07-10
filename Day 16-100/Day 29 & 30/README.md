# 🔑 AKA Secure Password Manager

A modern, highly secure, and feature-rich desktop password manager built using Python's **CustomTkinter** library for a sleek user interface and **AES-256 (Fernet) encryption** for cryptographic security.

---

## ✨ Features

### 🛡️ Core Security
*   **AES-256 Symmetric Encryption**: All credentials are encrypted in a local database binary file (`data.enc`). Passwords are never saved in plain text.
*   **PBKDF2 Key Derivation**: Derives a strong 32-byte key from your Master Password using a randomized 16-byte salt and 100,000 iterations of SHA256.
*   **Zero-Knowledge Architecture**: Your Master Password is never saved to the disk. It is only held in memory temporarily to perform decryption and encryption operations.
*   **Clipboard Auto-Clear**: Automatically deletes generated passwords from your system clipboard after 30 seconds to prevent accidental leaks.
*   **Legacy Database Migration**: Seamlessly imports and encrypts legacy plaintext credential files (`data.txt` or `data.json`) during the first-time setup, then securely deletes the unencrypted source files.

### 🎨 Modern UI & UX
*   **CustomTkinter Theme**: Sleek look with rounded inputs, custom button colors, and smooth hover animations.
*   **Responsive Sidebar**: A sorted, scrollable list of all saved websites with a real-time search filter.
*   **Dynamic Strength Meter**: Automatically evaluates and displays password strength (Weak, Medium, Strong) as you type, using a color-coded bar.
*   **Show/Hide Toggle**: Mask input values by default (`show="*"`) and toggle visibility using the eye button (`👁` / `🙈`).
*   **Dark/Light Mode**: Toggle between Light, Dark, or System default window appearances on the fly.

### ⚡ Database Operations
*   **Full CRUD Support**: Add new credentials, search, update existing records, and delete accounts directly from the UI.
*   **Custom Generator Settings**: A length slider (8 to 32 characters) and checkbox filters (Include uppercase, numbers, and symbols) to generate passwords satisfying specific requirements.
*   **CSV Import/Export**: Export your credentials to plain text CSV files for backups or import credentials from external platforms.
*   **Change Master Password**: Securely re-encrypt the entire database under a new Master Password.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

### 2. Dependencies
Install the required packages using `pip`:
```bash
pip install customtkinter cryptography pillow pyperclip
```

---

## 🚀 How to Use

### 1. Run the Application
Navigate to the directory and run the main entry file:
```bash
python main.py
```

### 2. First-Time Setup
1. If no database (`data.enc`) is found, the app displays the **Set Up Master Password** screen.
2. Choose a strong Master Password (minimum 8 characters).
3. If you have a legacy `data.txt` or `data.json` file in the folder, the application will automatically migrate your entries into the encrypted database and delete the plaintext source files for security.

### 3. Unlock Database
On subsequent launches, type your Master Password to unlock the vault. Incorrect passwords will block entry.

### 4. Search, Add, & Manage Credentials
*   **Search**: Use the search bar in the left sidebar to filter through website names. Click any sidebar entry to autofill the details on the main panel.
*   **Add/Update**: Fill in the Website, Username, and Password fields and click `💾 Save / Update`.
*   **Delete**: Select an entry and click `🗑 Delete` to remove it from the vault.
*   **Generate**: Set your length and character criteria, click `⚡ Generate Password`, and the result is filled and copied to your clipboard (which clears in 30 seconds).

---

## ⚠️ Important Security Notice
Your **Master Password** is the sole key to decrypting your database. There is **no password reset button** and no recovery mechanism. If you forget your Master Password, your encrypted credentials cannot be retrieved. **Write down your Master Password and keep it in a safe, physical location.**
