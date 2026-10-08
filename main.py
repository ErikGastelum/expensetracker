
"""main.py - Menu and program entry point 

"""

from validation import ( 
    get_menu_choice,
    get_amount,
    get_category,
    get_date,
    get_description,
)

try:
    from expense_logic import add_expense, view_expenses
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


def main():
    expenses = []

    while True:  # repeats until the user chooses Quit
        print(MENU_TEXT)
        choice = get_menu_choice(VALID_CHOICES)

        if choice == "1":
            handle_add(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
        # Placeholder: each option gets wired up in a later commit.
            print("(not implemented yet)")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or Ctrl+D shouldn't dump a traceback on the user.
        print("\nGoodbye!")


