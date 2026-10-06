"""validation.py - Input helpers that keep asking until the answer is valid.

Every function here loops with `while True` and only returns once the user
types something acceptable, so bad input can never crash the program.
"""

from datetime import datetime
from decimal import Decimal, InvalidOperation

from categories import DEFAULT_CATEGORIES

MAX_AMOUNT = Decimal("1000000")  # sanity cap so absurd numbers are rejected


def get_menu_choice(valid_choices):
    """Ask for a menu option; re-prompt until it is one of valid_choices."""
    while True:
        choice = input("Choose an option: ").strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(valid_choices)}")


def get_amount(prompt="Amount: "):
    """Return a positive float rounded to 2 decimal places."""
    while True:
        raw = input(prompt).strip().replace("$", "")
        try:
            amount = Decimal(raw)
        except InvalidOperation:
            print("Invalid amount. Please enter a number like 12.50.")
            continue

        # Decimal("nan") and Decimal("inf") parse successfully, so block them.
        if not amount.is_finite():
            print("Invalid amount. Please enter a number like 12.50.")
            continue
        if amount < Decimal("0.01"):
            print("Amount must be positive (at least 0.01).")
            continue
        if amount > MAX_AMOUNT:
            print(f"Amount is too large (max {MAX_AMOUNT}).")
            continue

        # The team's Expense class stores amount as a float.
        return float(amount.quantize(Decimal("0.01")))


def get_date(prompt="Date (YYYY-MM-DD): "):
    """Return a valid date as a 'YYYY-MM-DD' string."""
    while True:
        raw = input(prompt).strip()
        try:
            parsed = datetime.strptime(raw, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, like 2026-10-02.")
            continue
        # isoformat() gives a consistent format, e.g. "2026-1-5" -> "2026-01-05"
        return parsed.date().isoformat()


def get_category():
    """Show the category list and return one chosen from it (by number or name)."""
    print("Categories:")
    for number, name in enumerate(DEFAULT_CATEGORIES, start=1):
        print(f"  {number}. {name}")

    while True:
        raw = input("Choose a category (number or name): ").strip().lower()
        if raw == "":
            print("Category cannot be empty.")
        elif raw.isdecimal() and 1 <= int(raw) <= len(DEFAULT_CATEGORIES):
            return DEFAULT_CATEGORIES[int(raw) - 1]
        elif raw in DEFAULT_CATEGORIES:
            return raw
        else:
            print(f"'{raw}' is not a valid category. Pick one from the list.")


def get_description(prompt="Description (optional): "):
    """Description is optional, so anything (including blank) is accepted."""
    return input(prompt).strip()


def get_expense_id(prompt="Expense ID: "):
    """Return a positive whole number (used for edit and delete)."""
    while True:
        raw = input(prompt).strip()
        if raw.isdecimal() and int(raw) > 0:
            return int(raw)
        print("Invalid ID. Please enter a positive whole number.")