# Expense Tracker

A command-line expense tracker that lets you log spending, organize it by category, and view summaries. Data is saved to a file so it persists between runs.

**Course:** CS 3350, Mini Project (lab05)
**Team:** Erik Gastelum, Jacob Micu, Maika Pangilinan, Jonathan Torres

## Features

### Core (implemented)
- [ ] Add an expense (amount, category, date, optional description)
- [ ] View all expenses in a readable list
- [ ] Edit and delete expenses
- [ ] Categorize expenses
- [ ] Summary of spending by category
- [ ] Monthly spending summary
- [ ] Save and load data from a file
- [ ] Input validation (no negative amounts, valid dates, etc.)

### Stretch goals
- [ ] Monthly budgets per category with over-budget warnings
- [ ] Search and filter (date range, category, amount)
- [ ] Export report to CSV or text file
- [ ] Recurring expenses
- [ ] Text bar chart of spending by category
- [ ] Custom user-defined categories
- [ ] Undo last action

> Update the checkboxes as features get finished. Change `[ ]` to `[x]`.

## Requirements

- Tested on Odin (Linux)

## Installation

```bash
git clone <your-repo-URL> lab05
cd lab05
```

<!-- If there are dependencies, add the install command here, e.g.: pip install -r requirements.txt -->

## How to Run

```bash
python3 main.py
```

## Usage

When the program starts, you'll see a menu like this:

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
Amount: 12.50
Category: food
Date (YYYY-MM-DD): 2026-10-02
Description (optional): lunch
Expense added!
```

## Data Storage

Expenses are saved to `<!-- expenses.csv or expenses.json -->` in the project folder. Each expense is stored with the following fields:

| Field | Type | Description |
|---|---|---|
| id | integer | Unique identifier |
| amount | decimal | Amount spent (must be positive) |
| category | text | Spending category |
| date | YYYY-MM-DD | Date of the expense |
| description | text | Optional note |

## Project Structure

```
lab05/
├── README.md
├── <!-- main file -->        # Menu and program entry point
├── <!-- data file/module --> # Expense data structure and save/load
├── <!-- logic file/module -->  # Add / edit / delete logic
├── <!-- summary file/module --> # Category and monthly summaries
└── tests/                    # Tests
```

## Team and Contributions

| Member | Responsibilities |
|---|---|
| Erik Gastelum | Data model and file save/load |
| <!-- Name --> | Add / edit / delete logic |
| <!-- Maika Pangilinan--> | Menu, user interface, input validation |
| <!-- Name --> | Summaries |
| Everyone | Testing, documentation, release |

Task planning and progress are tracked on our [GitHub Project board](<!-- link to your project board -->).

## Known Issues / Limitations

- <!-- e.g., Dates must be entered as YYYY-MM-DD -->
- <!-- Add anything that doesn't work yet -->

## Future Work

See the stretch goals above and the open issues in this repository.
