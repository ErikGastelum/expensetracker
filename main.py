
"""main.py - Menu and program entry point 

"""

from validation import get_menu_choice

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


def main():
    while True:  # repeats until the user chooses Quit
        print(MENU_TEXT)
        choice = get_menu_choice(VALID_CHOICES)

        if choice == "7":
            print("Goodbye!")
            break

        # Placeholder: each option gets wired up in a later commit.
        print("(not implemented yet)")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or Ctrl+D shouldn't dump a traceback on the user.
        print("\nGoodbye!")


