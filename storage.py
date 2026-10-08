import csv
import os

from expense import Expense

DEFAULT_FILE = "expenses.csv"
HEADER = ["id", "amount", "category", "date", "description"]

def load_expenses(file_path=DEFAULT_FILE):
    expenses = []
    if not os.path.exists(file_path):
        return expenses

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        for line_number, row in enumerate(reader, start=2):
            if not row:
                continue  # Skip empty rows
            try:
                expenses.append(Expense.from_row(row))
            except ValueError as error:
                print(f"Warning: skipped bad row on line {line_number}: {error}")
    return expenses

def save_expenses(expenses, file_path=DEFAULT_FILE):
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)  # Write header
        for expense in expenses:
            writer.writerow([
                expense.id,
                expense.amount,
                expense.category,
                expense.date,
                expense.description
            ])

def next_id(expenses):
    if not expenses:
        return 1
    return max(expense.id for expense in expenses) + 1