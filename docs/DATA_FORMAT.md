# Data Format

This document is the agreement every module codes against. If it needs to
change, post in issue #2 first so everyone stays in sync.

## Decision

- **File format:** CSV (`expenses.csv`, UTF-8, comma-separated, with a header row)
- **Data model:** the `Expense` class in `expense.py`
- **Save/load:** handled separately in `storage.py` (its own issue)

## Expense fields

| Field | Python type | CSV example | Rules |
|---|---|---|---|
| `id` | `int` | `1` | Positive whole number, unique. |
| `amount` | `float` | `12.50` | Greater than 0. Rounded to 2 decimals. |
| `category` | `str` | `food` | Not empty. Stored lowercase and trimmed. |
| `date` | `str` | `2026-10-02` | Real calendar date in `YYYY-MM-DD`. |
| `description` | `str` | `lunch` | Optional. May be empty. Commas and quotes are allowed. |

## Example file

```csv
id,amount,category,date,description
1,12.50,food,2026-10-02,lunch
2,900.00,rent,2026-10-01,October rent
3,9.99,transport,2026-10-04,bus pass
4,25.00,fun,2026-10-05,"movie, popcorn included"
```

## Using the Expense class

```python
from expense import Expense

e = Expense(1, 12.50, "food", "2026-10-02", "lunch")
print(e.amount, e.category)   # use attributes, not e["amount"]
```

## Validation

Creating an `Expense` with invalid data raises `ValueError` with a readable
message (for example `amount must be greater than 0`). The menu code should
catch it and ask the user to try again:

```python
try:
    expense = Expense(new_id, amount_text, category, date_text, note)
except ValueError as error:
    print(f"Invalid input: {error}")
```