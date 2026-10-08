"""
summary.py
Owner: Jonathan Torres

Works with the Expense class in expense.py. By the time an Expense
reaches this module, expense.py has already:
  - rounded amount to 2 decimals (always a float > 0)
  - trimmed and lowercased category
  - stored date as a "YYYY-MM-DD" string
so the summaries can rely on those fields directly.
"""

from collections import defaultdict


def _month(expense):
    """Return 'YYYY-MM' for an expense."""
    return expense.date[:7]


# ---------- Calculations (return data, no printing) ----------

def summary_by_category(expenses):
    """Return {category: total}, highest total first."""
    totals = defaultdict(float)
    for e in expenses:
        totals[e.category] += e.amount
    rounded = {cat: round(total, 2) for cat, total in totals.items()}
    return dict(sorted(rounded.items(), key=lambda kv: (-kv[1], kv[0])))


def monthly_summary(expenses):
    """Return {'YYYY-MM': total}, oldest month first."""
    totals = defaultdict(float)
    for e in expenses:
        totals[_month(e)] += e.amount
    return {month: round(totals[month], 2) for month in sorted(totals)}


def category_breakdown_for_month(expenses, month):
    """Return {category: total} for one month, given as 'YYYY-MM'."""
    return summary_by_category([e for e in expenses if _month(e) == month])


def total_spent(expenses):
    """Return the total of all expenses."""
    return round(sum(e.amount for e in expenses), 2)


# ---------- Display (what the menu calls) ----------

def print_category_summary(expenses):
    """Menu option 5: Summary by category."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    totals = summary_by_category(expenses)
    grand_total = total_spent(expenses)
    print("\n=== Spending by Category ===")
    for category, total in totals.items():
        pct = total / grand_total * 100
        print(f"{category:<15} ${total:>10.2f}  ({pct:5.1f}%)")
    print("-" * 36)
    print(f"{'TOTAL':<15} ${grand_total:>10.2f}\n")


def print_monthly_summary(expenses):
    """Menu option 6: Monthly summary, with a category breakdown per month."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n=== Monthly Summary ===")
    for month, total in monthly_summary(expenses).items():
        print(f"{month}   ${total:>10.2f}")
        for category, cat_total in category_breakdown_for_month(expenses, month).items():
            print(f"    {category:<13} ${cat_total:>8.2f}")
    print("-" * 24)
    print(f"{'TOTAL':<7}   ${total_spent(expenses):>10.2f}\n")


def print_category_bar_chart(expenses, width=30):
    """Stretch goal: text bar chart of spending by category."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    totals = summary_by_category(expenses)
    largest = max(totals.values())
    print("\n=== Spending Chart ===")
    for category, total in totals.items():
        bar = "#" * max(1, int(total / largest * width))
        print(f"{category:<15} {bar} ${total:.2f}")
    print()


if __name__ == "__main__":
    # Quick manual demo: python3 summary.py
    from expense import Expense

    sample = [
        Expense(1, 12.50, "food", "2026-10-02", "lunch"),
        Expense(2, 45.00, "gas", "2026-10-05"),
        Expense(3, 8.25, "Food", "2026-09-28", "coffee"),
        Expense(4, 60.00, "bills", "2026-09-15", "phone"),
    ]
    print_category_summary(sample)
    print_monthly_summary(sample)
    print_category_bar_chart(sample)
