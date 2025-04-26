import json
import os
import csv

# Path where the user's finance data will be stored
DATA_FILE = "finance_tracker/finance_data.json"


# Load all user transaction data from the JSON file
def load_data():
    # If the file does not exist, return an empty dictionary
    if not os.path.exists(DATA_FILE):
        return {}

    # If file exists, open and load the data as a dictionary
    with open(DATA_FILE, "r") as file:
        return json.load(file)


# Save the full data dictionary to the JSON file
def save_data(data):
    # Write the data dictionary to the JSON file with indentation for readability
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Get all transactions for a specific user
def get_user_data(username):
    data = load_data()  # Load the full data
    return data.get(username, [])  # Return the list of transactions for the user


# Save a new transaction for a user
def save_user_transaction(username, transaction):
    data = load_data()  # Load existing data

    # If user doesn't have any transaction yet, create an empty list
    if username not in data:
        data[username] = []

    # Append the new transaction (income/expense) to user's list
    data[username].append(transaction)

    # Save the updated data back to the file
    save_data(data)


# Export all transactions of the user to a CSV file
def export_to_csv(username):
    data = get_user_data(username)  # Get the user's transactions
    if not data:
        return  # If no data, do nothing

    # Create a CSV filename based on username
    filename = f"{username}_finance_data.csv"

    # Write the transactions to a CSV file
    with open(filename, mode="w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["type", "amount", "category", "date"])
        writer.writeheader()  # Write column headers
        writer.writerows(data)  # Write each transaction as a row

    # Show success message to user
    from tkinter import messagebox
    messagebox.showinfo("Exported", f"Data exported to {filename}")
