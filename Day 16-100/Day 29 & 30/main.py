import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog
import customtkinter as ctk
import pyperclip
import csv
import string
import secrets
from PIL import Image

# Import cryptography helper
import crypto_db

# Set theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Get absolute path to the directory containing main.py
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "logo.png")


# ----------------------------- HELPERS ------------------------------------- #

def check_password_strength(password: str) -> tuple[float, str, str]:
    """Evaluates password strength and returns (progress_val, text, color)."""
    if not password:
        return 0.0, "Empty", "gray"
    
    score = 0
    length = len(password)
    
    # Length check
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
        
    # Content checks
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" for c in password):
        score += 1
        
    # Map score (max 6) to progress and display color
    if score <= 2:
        return 0.25, "Weak", "#e74c3c"  # Red
    elif score <= 4:
        return 0.6, "Medium", "#f39c12"  # Orange
    else:
        return 1.0, "Strong", "#2ecc71"  # Green


def generate_custom_password(length=16, use_upper=True, use_digits=True, use_symbols=True) -> str:
    """Generate a cryptographically secure random password based on user constraints."""
    # Always include lowercase letters
    chars = string.ascii_lowercase
    mandatory = [secrets.choice(string.ascii_lowercase)]
    
    if use_upper:
        chars += string.ascii_uppercase
        mandatory.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        mandatory.append(secrets.choice(string.digits))
    if use_symbols:
        symbols = "!#$%'()*+,-./:;<=>?@[]^_{|}~"
        chars += symbols
        mandatory.append(secrets.choice(symbols))
        
    # Fill rest of the password length
    remaining_len = length - len(mandatory)
    if remaining_len < 0:
        remaining_len = 0
    password_list = mandatory + [secrets.choice(chars) for _ in range(remaining_len)]
    
    # Shuffle cryptographically
    secrets.SystemRandom().shuffle(password_list)
    return "".join(password_list)


def copy_to_clipboard_with_clear(controller, password_text: str, delay_ms=30000):
    """Copies text to clipboard and schedules a clear action after delay_ms."""
    pyperclip.copy(password_text)
    
    def clear_clipboard():
        try:
            # Only clear if the clipboard still contains this password
            if pyperclip.paste() == password_text:
                pyperclip.copy("")
                # Find the dashboard and update status
                for child in controller.container.winfo_children():
                    if isinstance(child, DashboardFrame):
                        child.show_status("Clipboard cleared for security.")
                        break
        except Exception:
            pass
            
    if hasattr(controller, "_clipboard_timer_id") and controller._clipboard_timer_id:
        controller.after_cancel(controller._clipboard_timer_id)
        
    controller._clipboard_timer_id = controller.after(delay_ms, clear_clipboard)


def export_csv(data: dict):
    """Export decrypted passwords to a CSV file chosen by the user."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
        title="Export Decrypted Passwords"
    )
    if not file_path:
        return
    
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Website", "Email/Username", "Password"])
            for site, details in data.items():
                writer.writerow([site, details["email"], details["password"]])
        messagebox.showinfo("Success", f"Passwords exported successfully to {os.path.basename(file_path)}.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export CSV: {e}")


def import_csv(current_data: dict) -> tuple[dict, int]:
    """Import passwords from a CSV file into the database."""
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
        title="Import Passwords"
    )
    if not file_path:
        return current_data, 0
    
    imported_count = 0
    new_data = current_data.copy()
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            
            # Try to map columns if header is present
            web_idx, email_idx, pwd_idx = 0, 1, 2
            if header and len(header) >= 3:
                headers = [h.strip().lower() for h in header]
                if "website" in headers: web_idx = headers.index("website")
                if "email" in headers: email_idx = headers.index("email")
                elif "username" in headers: email_idx = headers.index("username")
                if "password" in headers: pwd_idx = headers.index("password")
            
            for row in reader:
                if len(row) < 3:
                    continue
                site = row[web_idx].strip()
                email = row[email_idx].strip()
                pwd = row[pwd_idx].strip()
                if site and email and pwd:
                    new_data[site] = {
                        "email": email,
                        "password": pwd
                    }
                    imported_count += 1
        return new_data, imported_count
    except Exception as e:
        messagebox.showerror("Error", f"Failed to import CSV: {e}")
        return current_data, 0


# ----------------------------- FRAMES -------------------------------------- #

class SetupFrame(ctk.CTkFrame):
    """Shown when no encrypted database exists. Prompts to set Master Password."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        title_label = ctk.CTkLabel(
            self, 
            text="Set Up Master Password", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=(50, 10))
        
        desc_label = ctk.CTkLabel(
            self,
            text="Create a strong Master Password. This password will encrypt all your logins.\nIf you lose it, your data cannot be recovered.",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        desc_label.pack(pady=(0, 25))
        
        inputs_frame = ctk.CTkFrame(self, fg_color="transparent")
        inputs_frame.pack(pady=10)
        
        self.pwd_entry = ctk.CTkEntry(
            inputs_frame, 
            placeholder_text="Enter Master Password", 
            show="*", 
            width=300,
            height=40
        )
        self.pwd_entry.pack(pady=10)
        
        self.confirm_entry = ctk.CTkEntry(
            inputs_frame, 
            placeholder_text="Confirm Master Password", 
            show="*", 
            width=300,
            height=40
        )
        self.confirm_entry.pack(pady=10)
        
        self.error_label = ctk.CTkLabel(
            self, 
            text="", 
            text_color="#e74c3c", 
            font=ctk.CTkFont(size=13)
        )
        self.error_label.pack(pady=5)
        
        setup_btn = ctk.CTkButton(
            self, 
            text="Set Password & Start", 
            font=ctk.CTkFont(weight="bold"),
            width=200,
            height=40,
            command=self.submit_setup
        )
        setup_btn.pack(pady=(15, 50))
        
        self.pwd_entry.bind("<Return>", lambda e: self.submit_setup())
        self.confirm_entry.bind("<Return>", lambda e: self.submit_setup())

    def submit_setup(self):
        pwd = self.pwd_entry.get()
        confirm = self.confirm_entry.get()
        
        if not pwd:
            self.error_label.configure(text="Password cannot be empty.")
            return
        if len(pwd) < 8:
            self.error_label.configure(text="Password must be at least 8 characters long.")
            return
        if pwd != confirm:
            self.error_label.configure(text="Passwords do not match.")
            return
            
        # Create database and migrate any existing plaintext files
        crypto_db.migrate_plaintext_db(pwd)
        
        # Load the newly created database and transition
        decrypted_data = crypto_db.load_db(pwd)
        self.controller.login_success(pwd, decrypted_data)


class LoginFrame(ctk.CTkFrame):
    """Shown when an encrypted database is found. Requires Master Password to unlock."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        title_label = ctk.CTkLabel(
            self, 
            text="Welcome Back", 
            font=ctk.CTkFont(size=26, weight="bold")
        )
        title_label.pack(pady=(70, 10))
        
        desc_label = ctk.CTkLabel(
            self,
            text="Enter your Master Password to unlock your credentials.",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        desc_label.pack(pady=(0, 30))
        
        inputs_frame = ctk.CTkFrame(self, fg_color="transparent")
        inputs_frame.pack(pady=10)
        
        self.pwd_entry = ctk.CTkEntry(
            inputs_frame, 
            placeholder_text="Master Password", 
            show="*", 
            width=300,
            height=40
        )
        self.pwd_entry.pack(pady=10)
        self.pwd_entry.focus()
        
        self.error_label = ctk.CTkLabel(
            self, 
            text="", 
            text_color="#e74c3c", 
            font=ctk.CTkFont(size=13)
        )
        self.error_label.pack(pady=5)
        
        login_btn = ctk.CTkButton(
            self, 
            text="Unlock Database", 
            font=ctk.CTkFont(weight="bold"),
            width=200,
            height=40,
            command=self.submit_login
        )
        login_btn.pack(pady=(15, 70))
        
        self.pwd_entry.bind("<Return>", lambda e: self.submit_login())

    def submit_login(self):
        pwd = self.pwd_entry.get()
        if not pwd:
            self.error_label.configure(text="Please enter your password.")
            return
            
        try:
            decrypted_data = crypto_db.load_db(pwd)
        except Exception:
            self.error_label.configure(text="Incorrect Master Password. Please try again.")
            return
            
        self.controller.login_success(pwd, decrypted_data)


class DashboardFrame(ctk.CTkFrame):
    """Main dashboard showing credentials list and interactive CRUD controls."""
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        
        # Grid layout: Sidebar (col 0), Main Panel (col 1)
        self.grid_columnconfigure(0, weight=0, minsize=280)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.pwd_hidden = True
        
        self.create_sidebar()
        self.create_main_panel()
        self.update_sidebar_list()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=280, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew", padx=(0, 2), pady=0)
        sidebar.grid_propagate(False)
        
        title_label = ctk.CTkLabel(
            sidebar, 
            text="🔑 Password Safe", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=(20, 15), padx=20, anchor="w")
        
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.filter_sidebar())
        self.search_entry = ctk.CTkEntry(
            sidebar, 
            placeholder_text="🔍 Search websites...", 
            textvariable=self.search_var
        )
        self.search_entry.pack(fill="x", padx=15, pady=(5, 10))
        
        self.scroll_frame = ctk.CTkScrollableFrame(sidebar)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Dark / Light selector at bottom
        mode_label = ctk.CTkLabel(sidebar, text="Appearance Mode:", font=ctk.CTkFont(size=12))
        mode_label.pack(pady=(10, 2), padx=20, anchor="w")
        
        self.mode_menu = ctk.CTkOptionMenu(
            sidebar, 
            values=["System", "Dark", "Light"],
            command=self.change_appearance_mode
        )
        self.mode_menu.pack(fill="x", padx=15, pady=(0, 20))

    def create_main_panel(self):
        main_panel = ctk.CTkFrame(self, corner_radius=0)
        main_panel.grid(row=0, column=1, sticky="nsew")
        
        main_panel.grid_columnconfigure(0, weight=1)
        main_panel.grid_rowconfigure(0, weight=1)

        # Scrollable container to prevent packing issues on small screen resolutions
        content_scroll = ctk.CTkScrollableFrame(main_panel, fg_color="transparent")
        content_scroll.pack(fill="both", expand=True, padx=20, pady=(10, 5))
        
        content_scroll.grid_columnconfigure(0, weight=1)
        content_scroll.grid_columnconfigure(1, weight=3)
        
        # Logo Image
        try:
            logo_img = ctk.CTkImage(
                light_image=Image.open(logo_path),
                dark_image=Image.open(logo_path),
                size=(110, 110)
            )
            logo_label = ctk.CTkLabel(content_scroll, image=logo_img, text="")
            logo_label.grid(row=0, column=0, columnspan=2, pady=(10, 15))
        except Exception:
            logo_label = ctk.CTkLabel(content_scroll, text="🛡️ SECURE DATABASE", font=ctk.CTkFont(size=24, weight="bold"))
            logo_label.grid(row=0, column=0, columnspan=2, pady=(10, 15))
            
        # Website field
        lbl_web = ctk.CTkLabel(content_scroll, text="Website:", font=ctk.CTkFont(weight="bold"))
        lbl_web.grid(row=1, column=0, sticky="e", padx=(10, 15), pady=8)
        
        self.website_entry = ctk.CTkEntry(content_scroll, placeholder_text="e.g. google.com")
        self.website_entry.grid(row=1, column=1, sticky="ew", padx=(0, 10), pady=8)
        
        # Email field
        lbl_email = ctk.CTkLabel(content_scroll, text="Email/Username:", font=ctk.CTkFont(weight="bold"))
        lbl_email.grid(row=2, column=0, sticky="e", padx=(10, 15), pady=8)
        
        self.email_entry = ctk.CTkEntry(content_scroll, placeholder_text="username or email")
        self.email_entry.grid(row=2, column=1, sticky="ew", padx=(0, 10), pady=8)
        self.email_entry.insert(0, "abdulkerim@email.com")
        
        # Password field
        lbl_pwd = ctk.CTkLabel(content_scroll, text="Password:", font=ctk.CTkFont(weight="bold"))
        lbl_pwd.grid(row=3, column=0, sticky="e", padx=(10, 15), pady=8)
        
        pwd_input_frame = ctk.CTkFrame(content_scroll, fg_color="transparent")
        pwd_input_frame.grid(row=3, column=1, sticky="ew", padx=(0, 10), pady=8)
        pwd_input_frame.grid_columnconfigure(0, weight=1)
        pwd_input_frame.grid_columnconfigure(1, weight=0)
        
        self.password_entry = ctk.CTkEntry(pwd_input_frame, placeholder_text="password", show="*")
        self.password_entry.grid(row=0, column=0, sticky="ew")
        self.password_entry.bind("<KeyRelease>", lambda e: self.check_strength())
        
        self.show_hide_btn = ctk.CTkButton(
            pwd_input_frame, 
            text="👁", 
            width=40,
            command=self.toggle_password_visibility
        )
        self.show_hide_btn.grid(row=0, column=1, padx=(5, 0))
        
        # Password Strength Bar
        lbl_strength = ctk.CTkLabel(content_scroll, text="Strength:", font=ctk.CTkFont(size=12))
        lbl_strength.grid(row=4, column=0, sticky="e", padx=(10, 15), pady=2)
        
        strength_frame = ctk.CTkFrame(content_scroll, fg_color="transparent")
        strength_frame.grid(row=4, column=1, sticky="ew", padx=(0, 10), pady=2)
        strength_frame.grid_columnconfigure(0, weight=1)
        
        self.strength_bar = ctk.CTkProgressBar(strength_frame, height=8)
        self.strength_bar.grid(row=0, column=0, sticky="ew", pady=5)
        self.strength_bar.set(0.0)
        
        self.strength_label = ctk.CTkLabel(strength_frame, text="Empty", font=ctk.CTkFont(size=11), text_color="gray")
        self.strength_label.grid(row=0, column=1, padx=(10, 0))
        
        # Password Generator Section
        gen_frame = ctk.CTkLabelFrame(content_scroll, text="Password Generator Settings")
        gen_frame.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=15)
        
        gen_frame.grid_columnconfigure(0, weight=1)
        gen_frame.grid_columnconfigure(1, weight=1)
        gen_frame.grid_columnconfigure(2, weight=1)
        
        length_label_frame = ctk.CTkFrame(gen_frame, fg_color="transparent")
        length_label_frame.grid(row=0, column=0, columnspan=3, sticky="ew", padx=15, pady=5)
        
        self.length_val_label = ctk.CTkLabel(length_label_frame, text="Length: 16", font=ctk.CTkFont(weight="bold"))
        self.length_val_label.pack(side="left")
        
        self.length_slider = ctk.CTkSlider(
            length_label_frame, 
            from_=8, 
            to=32, 
            number_of_steps=24,
            command=self.update_length_label
        )
        self.length_slider.pack(side="right", fill="x", expand=True, padx=(15, 0))
        self.length_slider.set(16)
        
        self.chk_upper = ctk.CTkCheckBox(gen_frame, text="Uppercase (A-Z)")
        self.chk_upper.grid(row=1, column=0, padx=15, pady=10, sticky="w")
        self.chk_upper.select()
        
        self.chk_digits = ctk.CTkCheckBox(gen_frame, text="Numbers (0-9)")
        self.chk_digits.grid(row=1, column=1, padx=15, pady=10, sticky="w")
        self.chk_digits.select()
        
        self.chk_symbols = ctk.CTkCheckBox(gen_frame, text="Symbols (!#$%)")
        self.chk_symbols.grid(row=1, column=2, padx=15, pady=10, sticky="w")
        self.chk_symbols.select()
        
        self.gen_btn = ctk.CTkButton(
            gen_frame, 
            text="⚡ Generate Password", 
            command=self.generate_password
        )
        self.gen_btn.grid(row=2, column=0, columnspan=3, sticky="ew", padx=15, pady=(5, 12))
        
        # CRUD Actions Buttons Frame
        actions_frame = ctk.CTkFrame(content_scroll, fg_color="transparent")
        actions_frame.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        
        actions_frame.grid_columnconfigure(0, weight=1)
        actions_frame.grid_columnconfigure(1, weight=1)
        actions_frame.grid_columnconfigure(2, weight=1)
        
        self.save_btn = ctk.CTkButton(
            actions_frame, 
            text="💾 Save / Update", 
            fg_color="#2ecc71", 
            hover_color="#27ae60",
            text_color="white",
            command=self.save_entry
        )
        self.save_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.delete_btn = ctk.CTkButton(
            actions_frame, 
            text="🗑 Delete", 
            fg_color="#e74c3c", 
            hover_color="#c0392b",
            text_color="white",
            command=self.delete_entry
        )
        self.delete_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.clear_btn = ctk.CTkButton(
            actions_frame, 
            text="🧹 Clear Fields", 
            fg_color="gray",
            hover_color="darkgray",
            command=self.clear_fields
        )
        self.clear_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        
        # Import, Export, Change Master Password Utilities
        utils_frame = ctk.CTkFrame(content_scroll, fg_color="transparent")
        utils_frame.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        utils_frame.grid_columnconfigure(0, weight=1)
        utils_frame.grid_columnconfigure(1, weight=1)
        utils_frame.grid_columnconfigure(2, weight=1)
        
        self.import_btn = ctk.CTkButton(
            utils_frame, 
            text="📥 Import CSV", 
            command=self.import_passwords
        )
        self.import_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.export_btn = ctk.CTkButton(
            utils_frame, 
            text="📤 Export CSV", 
            command=self.export_passwords
        )
        self.export_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.change_master_btn = ctk.CTkButton(
            utils_frame, 
            text="🔑 Change Master Pwd", 
            command=self.change_master_password
        )
        self.change_master_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        
        # Status Label at the very bottom
        self.status_bar = ctk.CTkLabel(
            main_panel, 
            text="Ready", 
            font=ctk.CTkFont(size=12, slant="italic"),
            anchor="w",
            padx=10,
            fg_color=("gray90", "gray15"),
            height=25
        )
        self.status_bar.pack(fill="x", side="bottom")

    def change_appearance_mode(self, new_mode):
        ctk.set_appearance_mode(new_mode)
        
    def update_length_label(self, val):
        self.length_val_label.configure(text=f"Length: {int(val)}")
        
    def toggle_password_visibility(self):
        if self.pwd_hidden:
            self.password_entry.configure(show="")
            self.show_hide_btn.configure(text="🙈")
            self.pwd_hidden = False
        else:
            self.password_entry.configure(show="*")
            self.show_hide_btn.configure(text="👁")
            self.pwd_hidden = True

    def check_strength(self):
        pwd = self.password_entry.get()
        progress, text, color = check_password_strength(pwd)
        self.strength_bar.set(progress)
        self.strength_bar.configure(progress_color=color)
        self.strength_label.configure(text=text, text_color=color)

    def show_status(self, text):
        self.status_bar.configure(text=text)

    def update_sidebar_list(self):
        for child in self.scroll_frame.winfo_children():
            child.destroy()
            
        websites = sorted(self.controller.db_data.keys())
        filter_text = self.search_entry.get().strip().lower()
        
        for web in websites:
            if not filter_text or filter_text in web.lower():
                btn = ctk.CTkButton(
                    self.scroll_frame,
                    text=web,
                    anchor="w",
                    fg_color="transparent",
                    text_color=("gray10", "gray90"),
                    hover_color=("gray80", "gray25"),
                    command=lambda w=web: self.load_website(w)
                )
                btn.pack(fill="x", padx=5, pady=2)

    def filter_sidebar(self):
        self.update_sidebar_list()

    def load_website(self, website_name):
        data = self.controller.db_data.get(website_name, {})
        if data:
            self.website_entry.delete(0, tk.END)
            self.website_entry.insert(0, website_name)
            
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, data.get("email", ""))
            
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, data.get("password", ""))
            self.check_strength()
            self.show_status(f"Loaded credentials for {website_name}")

    def clear_fields(self):
        self.website_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.check_strength()
        self.show_status("Fields cleared")

    def generate_password(self):
        length = int(self.length_slider.get())
        use_upper = self.chk_upper.get() == 1
        use_digits = self.chk_digits.get() == 1
        use_symbols = self.chk_symbols.get() == 1
        
        pwd = generate_custom_password(length, use_upper, use_digits, use_symbols)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, pwd)
        self.check_strength()
        
        # Copy to clipboard with auto clear
        copy_to_clipboard_with_clear(self.controller, pwd)
        self.show_status("Generated & copied to clipboard! (Clears in 30s)")

    def save_entry(self):
        website = self.website_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not website or not email or not password:
            messagebox.showwarning("Warning", "Please fill in all fields (Website, Email, Password).")
            return
            
        if website in self.controller.db_data:
            ans = messagebox.askyesno("Confirm Update", f"Credentials for {website} already exist. Overwrite?")
            if not ans:
                return
                
        self.controller.db_data[website] = {
            "email": email,
            "password": password
        }
        
        crypto_db.save_db(self.controller.db_data, self.controller.master_pwd)
        self.update_sidebar_list()
        self.show_status(f"Saved credentials for {website}.")
        
    def delete_entry(self):
        website = self.website_entry.get().strip()
        if not website:
            messagebox.showwarning("Warning", "Please enter the website name to delete.")
            return
            
        if website not in self.controller.db_data:
            messagebox.showwarning("Warning", f"No credentials found for {website}.")
            return
            
        ans = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete credentials for {website}?")
        if ans:
            del self.controller.db_data[website]
            crypto_db.save_db(self.controller.db_data, self.controller.master_pwd)
            self.clear_fields()
            self.update_sidebar_list()
            self.show_status(f"Deleted credentials for {website}.")

    def export_passwords(self):
        export_csv(self.controller.db_data)

    def import_passwords(self):
        new_data, count = import_csv(self.controller.db_data)
        if count > 0:
            self.controller.db_data = new_data
            crypto_db.save_db(self.controller.db_data, self.controller.master_pwd)
            self.update_sidebar_list()
            self.show_status(f"Successfully imported {count} credentials.")
            messagebox.showinfo("Success", f"Imported {count} credentials successfully.")

    def change_master_password(self):
        dialog = ctk.CTkInputDialog(text="Enter Current Master Password:", title="Verify Identity")
        curr_pwd = dialog.get_input()
        if not curr_pwd:
            return
            
        if curr_pwd != self.controller.master_pwd:
            messagebox.showerror("Error", "Incorrect current password.")
            return
            
        new_dialog1 = ctk.CTkInputDialog(text="Enter New Master Password:", title="Change Password")
        new_pwd = new_dialog1.get_input()
        if not new_pwd:
            return
            
        if len(new_pwd) < 8:
            messagebox.showwarning("Warning", "New password must be at least 8 characters long.")
            return
            
        new_dialog2 = ctk.CTkInputDialog(text="Confirm New Master Password:", title="Change Password")
        new_pwd_confirm = new_dialog2.get_input()
        if new_pwd != new_pwd_confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return
            
        success = crypto_db.change_master_password(self.controller.master_pwd, new_pwd)
        if success:
            self.controller.master_pwd = new_pwd
            messagebox.showinfo("Success", "Master Password changed successfully.")
            self.show_status("Master Password changed successfully.")
        else:
            messagebox.showerror("Error", "Failed to change Master Password.")


# ----------------------------- APP CLASS ----------------------------------- #

class PasswordManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Antigravity Secure Password Manager")
        self.geometry("900x600")
        self.resizable(False, False)
        
        # Center the window
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")

        self.master_pwd = None
        self.db_data = {}
        self._clipboard_timer_id = None
        
        # Container frame for page transitions
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        self.show_auth_flow()

    def show_auth_flow(self):
        for child in self.container.winfo_children():
            child.destroy()
            
        if crypto_db.db_exists():
            self.show_login_frame()
        else:
            self.show_setup_frame()

    def show_setup_frame(self):
        setup_frame = SetupFrame(self.container, self)
        setup_frame.pack(fill="both", expand=True, padx=40, pady=40)

    def show_login_frame(self):
        login_frame = LoginFrame(self.container, self)
        login_frame.pack(fill="both", expand=True, padx=40, pady=40)

    def login_success(self, master_pwd, decrypted_data):
        self.master_pwd = master_pwd
        self.db_data = decrypted_data
        
        # Clear frame and show Dashboard
        for child in self.container.winfo_children():
            child.destroy()
            
        dashboard = DashboardFrame(self.container, self)
        dashboard.pack(fill="both", expand=True)


# ----------------------------- MAIN ENTRY ---------------------------------- #

if __name__ == "__main__":
    app = PasswordManagerApp()
    app.mainloop()