import matplotlib.pyplot as plt
from tkinter import simpledialog, messagebox
from data_handler import get_user_data

# Show a pie chart of expenses grouped by category
def show_category_report(username):
    # Fetch all transactions for the logged-in user
    transactions = get_user_data(username)

    # Ask user if they want to filter by a specific month (YYYY-MM format)
    month_filter = simpledialog.askstring("Filter", "Enter month (YYYY-MM) or leave empty:")

    # Dictionary to store total amount spent per category
    category_totals = {}

    # Loop through each transaction
    for t in transactions:
        # Only include expenses, not income
        if t["type"] != "Expense":
            continue

        # If user provided a month filter, skip transactions not matching that month
        if month_filter and not t["date"].startswith(month_filter):
            continue

        # Group the amount by category
        category = t["category"]
        amount = t["amount"]
        # Add amount to the existing total for the category
        category_totals[category] = category_totals.get(category, 0) + amount

    # If no expenses found, show a message and return
    if not category_totals:
        messagebox.showinfo("No Data", "No expenses found for the selected period.")
        return

    # Prepare labels and sizes for the pie chart
    labels = list(category_totals.keys())  # Category names
    sizes = list(category_totals.values())  # Amounts spent in each category

    # Create the pie chart
    plt.figure(figsize=(6, 6))
    plt.title(f"Expense Distribution by Category\nUser: {username}", fontsize=12)
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.axis("equal")  # Make the pie chart a perfect circle
    plt.tight_layout()
    plt.show()
