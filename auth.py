import os
import json
from tkinter import messagebox
from tkinter import simpledialog

# Directory and file where user information will be saved
USER_DIR = "finance_tracker"
USER_FILE = os.path.join(USER_DIR, "users.json")


# Function to load all users from the JSON file
def load_users():
    # Ensure the user data directory exists
    if not os.path.exists(USER_DIR):
        os.makedirs(USER_DIR)  # Create the directory if it doesn't exist

    # If the user file doesn't exist yet, return an empty dictionary
    if not os.path.exists(USER_FILE):
        return {}

    # If file exists, open and load the JSON data into Python dictionary
    with open(USER_FILE, "r") as file:
        return json.load(file)


# Function to save users back to the JSON file
def save_users(users):
    # Ensure the user data directory exists
    if not os.path.exists(USER_DIR):
        os.makedirs(USER_DIR)  # Create the directory if it doesn't exist

    # Save the given users dictionary to the file with proper indentation
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


# Function to register a new user
def register_user():
    # Ask user for a username through a popup dialog
    username = simpledialog.askstring("Register", "Enter a username:")
    if not username:
        messagebox.showerror("Error", "Username cannot be empty!")
        return None

    # Ask user for a password through a popup dialog
    password = simpledialog.askstring("Register", "Enter a password:", show="*")
    if not password:
        messagebox.showerror("Error", "Password cannot be empty!")
        return None

    # Load existing users
    users = load_users()

    # Check if the username already exists
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
        return None

    # Save the new user (store username and password)
    users[username] = {"password": password}
    save_users(users)

    # Show success message
    messagebox.showinfo("Success", f"User {username} registered successfully!")
    return username


# Function to login an existing user
def login_user():
    # Ask for the username
    username = simpledialog.askstring("Login", "Enter your username:")
    if not username:
        messagebox.showerror("Error", "Username cannot be empty!")
        return None

    # Ask for the password
    password = simpledialog.askstring("Login", "Enter your password:", show="*")
    if not password:
        messagebox.showerror("Error", "Password cannot be empty!")
        return None

    # Load all users from file
    users = load_users()

    # Validate: Check if username exists and the password matches
    if username in users and users[username]["password"] == password:
        messagebox.showinfo("Success", f"Welcome back, {username}!")
        return username
    else:
        # Show error if login fails
        messagebox.showerror("Error", "Invalid username or password!")
        return None
