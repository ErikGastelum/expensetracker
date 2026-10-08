import csv
import os

from expense import Expense

DEFAULT_FILE = "expenses.csv"
HEADER = ["id", "amount", "category", "date", "description"]

def load_expenses(file_path=DEFAULT_FILE):
    expenses = []
    if not os.path.exists(file_path):
        return expenses

    with open(file_path, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) == 5:
                expense = Expense(
                    id=int(row[0]),
                    amount=float(row[1]),
                    category=row[2],
                    date=row[3],
                    description=row[4]
                )
                expenses.append(expense)
    return expenses

def save_expenses(expenses, file_path=DEFAULT_FILE):
    with open(file_path, mode="w", newline="") as file:
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