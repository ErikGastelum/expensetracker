import math
from dataclasses import dataclass
from datetime import date as date_type, datetime

DATE_FORMAT = "%Y-%m-%d"


@dataclass
class Expense:
    id: int
    amount: float
    category: str
    date: str
    description: str = ""

    def __post_init__(self):
        # id
        try:
            self.id = int(self.id)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid id: {self.id}. ID must be a whole number.")
        if self.id < 1:
            raise ValueError("ID must be a positive number.")

        # amount
        try:
            self.amount = float(self.amount)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid amount: {self.amount}. Amount must be a number.")
        if not math.isfinite(self.amount) or self.amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        self.amount = round(self.amount, 2)

        # category (trimmed and lowercase so "Food" and "food" match)
        self.category = str(self.category).strip().lower()
        if not self.category:
            raise ValueError("Category cannot be empty.")

        # date (accepts a YYYY-MM-DD string or a date/datetime object)
        if isinstance(self.date, (datetime, date_type)):
            self.date = self.date.strftime(DATE_FORMAT)
        try:
            parsed = datetime.strptime(str(self.date).strip(), DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date: {self.date}. Date must be in YYYY-MM-DD format.")
        self.date = parsed.strftime(DATE_FORMAT)

        # description
        self.description = "" if self.description is None else str(self.description).strip()

    def to_row(self):
        """Return the expense as a list, ready for csv.writer."""
        return [self.id, f"{self.amount:.2f}", self.category, self.date, self.description]

    @classmethod
    def from_row(cls, row):
        """Build an Expense from a list (one row read by csv.reader)."""
        if len(row) != 5:
            raise ValueError(f"Row must have exactly 5 elements. Got {len(row)}.")
        return cls(id=row[0], amount=row[1], category=row[2], date=row[3], description=row[4])
