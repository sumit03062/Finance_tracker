# summary_view.py

import tkinter as tk
from tkinter import simpledialog
from data_handler import get_user_data

# Function to show total income, total expenses, and balance for a user
def show_summary(username):
    # Load all transactions of the user
    transactions = get_user_data(username)

    # Ask user if they want to filter transactions by month (e.g., "2025-04")
    month_filter = simpledialog.askstring("Filter", "Enter month (YYYY-MM) or leave empty:")

    # Initialize counters for total income and total expenses
    total_income = 0
    total_expense = 0

    # Loop through each transaction
    for t in transactions:
        # If a month filter is applied, skip transactions not matching the month
        if month_filter and not t["date"].startswith(month_filter):
            continue

        # Sum incomes
        if t["type"] == "Income":
            total_income += t["amount"]
        # Sum expenses
        elif t["type"] == "Expense":
            total_expense += t["amount"]

    # Calculate remaining balance
    balance = total_income - total_expense

    # Create a popup window to display the summary
    window = tk.Toplevel()
    window.title("Summary")
    window.geometry("300x200")
    window.config(bg="#e6f2ff")  # Light blue background for better UI

    # Display the summary values inside the popup
    tk.Label(window, text="💼 Summary", font=("Arial", 16, "bold"), bg="#e6f2ff").pack(pady=10)
    tk.Label(window, text=f"Total Income: ₹ {total_income:.2f}", fg="green", font=("Arial", 12), bg="#e6f2ff").pack(pady=5)
    tk.Label(window, text=f"Total Expenses: ₹ {total_expense:.2f}", fg="red", font=("Arial", 12), bg="#e6f2ff").pack(pady=5)
    tk.Label(window, text=f"Balance: ₹ {balance:.2f}", font=("Arial", 12, "bold"), bg="#e6f2ff").pack(pady=5)

    # Close button to exit the popup
    tk.Button(window, text="Close", command=window.destroy).pack(pady=15)
