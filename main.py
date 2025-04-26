import tkinter as tk
from tkinter import messagebox

# Importing functions from other modules
from auth import login_user, register_user
from transaction_manager import add_transaction_window
from summary_view import show_summary
from category_report import show_category_report
from data_handler import export_to_csv

# Variable to store the currently logged-in user
current_user = None


# Function to launch the main dashboard window after login
def launch_dashboard(user):
    root = tk.Tk()
    root.title(f"Finance Tracker - Logged in as {user}")  # Set window title
    root.geometry("400x400")  # Set window size
    root.config(bg="#f5f5f5")  # Light background color

    # Title label
    tk.Label(root, text="Personal Finance Tracker", font=("Arial", 18), bg="#f5f5f5").pack(pady=20)

    # Button to add an income
    tk.Button(root, text="➕ Add Income", width=25, command=lambda: add_transaction_window(user, "Income")).pack(pady=5)

    # Button to add an expense
    tk.Button(root, text="➖ Add Expense", width=25, command=lambda: add_transaction_window(user, "Expense")).pack(
        pady=5)

    # Button to view income/expense summary
    tk.Button(root, text="🥧 View Summary", width=25, command=lambda: show_summary(user)).pack(pady=5)

    # Button to view category-wise expense report (Pie Chart)
    tk.Button(root, text="📊 Category Report", width=25, command=lambda: show_category_report(user)).pack(pady=5)

    # Button to export all transactions to a CSV file
    tk.Button(root, text="📁 Export to CSV", width=25, command=lambda: export_to_csv(user)).pack(pady=5)

    # Button to logout (close dashboard)
    tk.Button(root, text="🚪 Logout", width=25, command=root.destroy).pack(pady=20)

    root.mainloop()  # Start the dashboard event loop


# Main logic to show login/register popup first
def main():
    global current_user  # Use the global variable

    root = tk.Tk()
    root.withdraw()  # Hide the default main window initially

    # Ask the user whether they already have an account
    choice = messagebox.askquestion("Login or Register", "Do you already have an account?")

    if choice == "yes":
        # If yes, proceed with login
        current_user = login_user()
    else:
        # If no, proceed with registration
        current_user = register_user()

    # If user login/register is successful, launch the dashboard
    if current_user:
        launch_dashboard(current_user)
    else:
        # If not, show exit message
        messagebox.showinfo("Exit", "Exiting application.")


# Entry point of the program
if __name__ == "__main__":
    main()
