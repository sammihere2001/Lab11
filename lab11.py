import datetime

expenses = []

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.date.today().isoformat()
    category = input("Enter category (e.g., Food, Travel, Bills): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Expense not added.")
        return
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return
    print("\n--- All Expenses ---")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. {exp['date']} | {exp['category']} | ${exp['amount']} | {exp['description']}")
    print()

def total_by_category():
    category = input("Enter category to view total: ")
    total = sum(exp["amount"] for exp in expenses if exp["category"].lower() == category.lower())
    print(f"Total expenses in '{category}': ${total:.2f}\n")

def delete_expense():
    view_expenses()
    try:
        num = int(input("Enter entry number to delete: "))
        if 1 <= num <= len(expenses):
            removed = expenses.pop(num - 1)
            print(f"Deleted expense: {removed['category']} - ${removed['amount']}")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("=== Simple Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
