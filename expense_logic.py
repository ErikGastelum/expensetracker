# expense_logic.py - add/edit/delete logic for the expense tracker
# author - Jacob Micu

from expense import Expense

def next_id(expenses):
    biggest = 0
    for expense in expenses:
        if expense.id > biggest:
            biggest = expense.id
    return biggest + 1

def find_expense(expenses, expense_id):
    try:
        expense_id = int(expense_id)
    except (TypeError, ValueError):
        raise ValueError("Invalid id: " + str(expense_id) + ". ID must be a whole number.")

    for index in range(len(expenses)):
        if expenses[index].id == expense_id:
            return index

    return None

def add_expense(expenses, amount, category, date, description=""):
    new_expense = Expense(next_id(expenses), amount, category, date, description)
    expenses.append(new_expense)
    return new_expense

def edit_expense(expenses, expense_id, amount=None, category=None, date=None, description=None):
    if amount is None and category is None and date is None and description is None:
        raise ValueError("Nothing to change.")

    index = find_expense(expenses, expense_id)
    if index is None:
        return False
    old = expenses[index]

    if amount is NOne:
        amount = old.amount
    if category is None:
        category = old.category
    if date is None:
        date = old.date
    if description is None:
        description = old.description

    expenses[index] = Expense(old.id, amount, category, date, description)
    return True

def delete_expense(expenses, expense_id):
    index = find_expense(expenses, expense_id)
    if index is None:
        return False
    expenses.pop(index)
    return True

def format_expenses(expenses):
    if len(expenses) == 0:
        return "No expenses yet."

    category_width = len("Category")
    for expense in expenses:
        if len(expense.category) > category_width:
            category_width = len(expense.category)

    header = ("ID".rjust(4) + " " + "Date".ljust(10) + " " + 
              "Category".ljust(category_width) + " " + 
              "Amount".rjust(10) + " " + "Description")
    lines = [header, "-" * len(header)]

    total = 0
    for expense in expenses:
        amount_text = "$" + "%.2f" % expense.amount
        lines.append(str(expense.id).rjust(4) + " " + expense.date + " " + 
                     expense.category.ljust(category_width) + " " + 
                     amount_text.rjust(10) + " " + expense.description)
        total = total + expense.amount

    lines.append("-" * len(header))
    lines.append("Total: $" + "%.2f" % total)

    return "\n".join(lines)

def view_expenses(expenses):
    print(format_expenses(expenses))
