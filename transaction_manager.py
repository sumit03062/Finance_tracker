# transaction_manager.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from data_handler import save_user_transaction

# Function to open a window for adding a transaction (either income or expense)
def add_transaction_window(username, transaction_type):
    # Create a new popup window
    window = tk.Toplevel()
    window.title(f"Add {transaction_type}")  # Set window title based on transaction type
    window.geometry("300x300")  # Set window size
    window.config(bg="#f0f0f0")  # Light grey background for a clean UI

    # Heading label
    tk.Label(window, text=f"Add {transaction_type}", font=("Arial", 14)).pack(pady=10)

    # Amount input field
    tk.Label(window, text="Amount:").pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()

    # Category input field
    tk.Label(window, text="Category:").pack()
    category_entry = tk.Entry(window)
    category_entry.pack()

    # Date input field (defaults to today's date)
    tk.Label(window, text="Date (YYYY-MM-DD):").pack()
    date_entry = tk.Entry(window)
    date_entry.insert(0, datetime.today().strftime("%Y-%m-%d"))  # Default to current date
    date_entry.pack()

    # Submit button logic
    def submit():
        try:
            # Collect and validate input values
            amount = float(amount_entry.get())
            category = category_entry.get().strip()
            date = date_entry.get().strip()

            # Basic input validation
            if amount <= 0 or not category or not date:
                raise ValueError("Invalid input")

            # Create transaction dictionary
            transaction = {
                "type": transaction_type,
                "amount": amount,
                "category": category,
                "date": date
            }

            # Save the transaction for the user
            save_user_transaction(username, transaction)

            # Show success message and close window
            messagebox.showinfo("Success", f"{transaction_type} added successfully!")
            window.destroy()

        except ValueError:
            # Show error message if input is invalid
            messagebox.showerror("Error", "Please enter valid details.")

    # Submit and Cancel buttons
    tk.Button(window, text="Submit", command=submit).pack(pady=15)
    tk.Button(window, text="Cancel", command=window.destroy).pack()

    window.mainloop()  # Keep the window running
