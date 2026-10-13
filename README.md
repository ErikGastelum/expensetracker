# Expense Tracker

A command-line expense tracker written in Python. Log your spending, organize it by category, edit or delete entries, and view summaries by category and by month. Expenses are saved to a CSV file, so your data is still there the next time you run the program.

**Course:** CS 3350, Mini Project (lab05)
**Team:** Erik Gastelum, Jacob Micu, Maika Pangilinan, Jonathan Torres

## Features

### Core (complete)
- [x] Add an expense (amount, category, date, optional description)
- [x] View all expenses in a readable table with a running total
- [x] Edit and delete expenses
- [x] Categorize expenses (food, rent, transport, fun, other)
- [x] Summary of spending by category (with percentages)
- [x] Monthly spending summary (with a category breakdown per month)
- [x] Save and load data from a file (`expenses.csv`)
- [x] Input validation (positive amounts, real dates, valid categories, valid menu choices)

### Stretch goals
- [ ] Monthly budgets per category with over-budget warnings
- [ ] Search and filter (date range, category, amount)
- [ ] Export report to CSV or text file
- [ ] Recurring expenses
- [ ] Text bar chart of spending by category (the function exists in `summary.py` but is not in the menu yet)
- [ ] Custom user-defined categories
- [ ] Undo last action

## Requirements

- Python 3.8 or newer
- No external libraries (standard library only)
- Tested on Odin (Linux)

## Installation

```bash
git clone https://github.com/ErikGastelum/expensetracker.git mini-project
cd mini-project
```

There are no dependencies to install.

## How to Run

Run the program from the project folder (the one that contains `main.py`):

```bash
python3 main.py
```

To run the tests:

```bash
python3 -m unittest discover tests
```

## Usage

When the program starts, you'll see this menu:

```
=== Expense Tracker ===
1. Add expense
2. View all expenses
3. Edit expense
4. Delete expense
5. Summary by category
6. Monthly summary
7. Quit
Choose an option:
```

### Example: adding an expense

```
Choose an option: 1
Amount: 12.50
Categories:
  1. food
  2. rent
  3. transport
  4. fun
  5. other
Choose a category (number or name): 1
Date (YYYY-MM-DD): 2026-10-02
Description (optional): lunch
Expense added! You now have 1 expense(s).
```

### Example: viewing expenses

```
 ID  Date        Category        Amount  Description
  1  2026-10-02  food        $    12.50  lunch
  2  2026-10-01  rent        $   900.00  october rent
-----------------------------------------------
Total: $912.50
```

Edit and delete ask for an expense ID, which is shown in the table. If you type something invalid (a negative amount, a made-up date, a category that is not on the list), the program explains the problem and asks again instead of crashing. Press Ctrl+C at any time to exit.

## Data Storage

Expenses are saved to `expenses.csv` in the folder you run the program from. The file is created automatically the first time you add, edit, or delete an expense, and it is loaded every time the program starts.

| Field | Type | Description |
|---|---|---|
| id | integer | Unique identifier |
| amount | decimal | Amount spent (must be greater than 0) |
| category | text | Spending category (stored lowercase) |
| date | YYYY-MM-DD | Date of the expense |
| description | text | Optional note |

Example file:

```csv
id,amount,category,date,description
1,12.50,food,2026-10-02,lunch
2,900.00,rent,2026-10-01,october rent
```

See [docs/DATA_FORMAT.md](docs/DATA_FORMAT.md) for the full format and rules.

## Project Structure

```
lab05/
├── README.md
├── main.py              # Menu and program entry point
├── expense.py           # Expense data model and validation
├── storage.py           # Save/load expenses to expenses.csv
├── expense_logic.py     # Add / edit / delete / view logic
├── summary.py           # Category and monthly summaries
├── validation.py        # Input prompts that re-ask until valid
├── categories.py        # The list of allowed categories
├── tests/               # Unit tests
└── docs/
    └── DATA_FORMAT.md   # CSV file format documentation
```

## Team and Contributions

| Member | Responsibilities |
|---|---|
| Erik Gastelum | Data model (`expense.py`) and file save/load (`storage.py`) |
| Jacob Micu | Add / edit / delete logic (`expense_logic.py`) |
| Maika Pangilinan | Menu, user interface, input validation (`main.py`, `validation.py`, `categories.py`) |
| Jonathan Torres | Summaries (`summary.py`) |
| Everyone | Testing, documentation, release |

Task planning and progress are tracked on our [GitHub Project board](https://github.com/users/ErikGastelum/projects/3).

## Known Issues / Limitations

- Dates must be entered as `YYYY-MM-DD`.
- Categories come from a fixed list in `categories.py`; custom categories are not supported yet.
- Amounts are capped at 1,000,000.
- Rows in `expenses.csv` with invalid data are skipped with a warning when the file is loaded.
- `expenses.csv` is created in the folder you run the program from, so always run it from the project folder.

## Future Work

See the stretch goals above and the open issues in this repository.