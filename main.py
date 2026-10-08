
"""main.py - Menu and program entry point 

"""

from validation import ( 
    get_menu_choice,
    get_amount,
    get_category,
    get_date,
    get_description,
    get_expense_id,
)
from summary import print_category_summary, print_monthly_summary  # Jonathan's code


try:
    from expense_logic import add_expense, view_expenses, edit_expense, delete_expense
except ImportError:
    print("[temp] expense_logic.py not found - using stand-ins")
    from expense import Expense  # Erik's data model

    def add_expense(expenses, amount, category, date, description):
        new_id = max([e.id for e in expenses], default=0) + 1
        expenses.append(Expense(new_id, amount, category, date, description))

    def view_expenses(expenses):
        if not expenses:
            print("No expenses yet.")
            return
        print(f"\n{'ID':>3}  {'Date':<10}  {'Category':<10}  {'Amount':>10}  Description")
        for e in expenses:
            print(f"{e.id:>3}  {e.date:<10}  {e.category:<10}  "
                  f"${e.amount:>9.2f}  {e.description}")

    def edit_expense(expenses, expense_id, amount, category, date, description):
        for i, e in enumerate(expenses):
            if e.id == expense_id:
                expenses[i] = Expense(expense_id, amount, category, date, description)
                return True
        return False

    def delete_expense(expenses, expense_id):
        for e in expenses:
            if e.id == expense_id:
                expenses.remove(e)
                return True
        return False




MENU_TEXT = """
=== Expense Tracker ===
1. Add expense
2. View all expenses
3. Edit expense
4. Delete expense
5. Summary by category
6. Monthly summary
7. Quit"""

VALID_CHOICES = ["1", "2", "3", "4", "5", "6", "7"]

def handle_add(expenses):
    """Collect validated input and add a new expense."""
    amount = get_amount()
    category = get_category()
    date = get_date()
    description = get_description()
    try:
        add_expense(expenses, amount, category, date, description)
    except ValueError as error:  # Erik's Expense class double-checks the data
        print(f"Invalid input: {error}")
        return
    print(f"Expense added! You now have {len(expenses)} expense(s).")

def handle_edit(expenses):
    """Pick an expense by ID and replace its values with new validated ones."""
    if not expenses:
        print("No expenses to edit.")
        return
    view_expenses(expenses)
    expense_id = get_expense_id()
    print("Enter the new values:")
    amount = get_amount()
    category = get_category()
    date = get_date()
    description = get_description()
    try:
        found = edit_expense(expenses, expense_id, amount, category, date, description)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return
    if found:
        print("Expense updated!")
    else:
        print(f"No expense found with ID {expense_id}.")


def handle_delete(expenses):
    """Pick an expense by ID and delete it."""
    if not expenses:
        print("No expenses to delete.")
        return
    view_expenses(expenses)
    expense_id = get_expense_id()
    if delete_expense(expenses, expense_id):
        print("Expense deleted!")
    else:
        print(f"No expense found with ID {expense_id}.")

def main():
    expenses = []

    while True:  # repeats until the user chooses Quit
        print(MENU_TEXT)
        choice = get_menu_choice(VALID_CHOICES)

        if choice == "1":
            handle_add(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            handle_edit(expenses)
        elif choice == "4":
            handle_delete(expenses)
        elif choice == "5":
            print_category_summary(expenses)
        elif choice == "6":
            print_monthly_summary(expenses)
        elif choice == "7":
            print("Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or Ctrl+D shouldn't dump a traceback on the user.
        print("\nGoodbye!")


