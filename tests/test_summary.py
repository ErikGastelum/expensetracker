"""Tests for summary.py. Run from the repo root:
    python3 -m unittest discover tests
"""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout

# Let the tests import modules from the repo root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from expense import Expense
from summary import (
    summary_by_category,
    monthly_summary,
    category_breakdown_for_month,
    total_spent,
    print_category_summary,
    print_monthly_summary,
    print_category_bar_chart,
)


def sample():
    return [
        Expense(1, 12.50, "food", "2026-10-02", "lunch"),
        Expense(2, 45.00, "gas", "2026-10-05"),
        Expense(3, 8.25, "Food", "2026-09-28", "coffee"),
        Expense(4, 60.00, "bills", "2026-09-15", "phone"),
    ]


class TestCategorySummary(unittest.TestCase):
    def test_totals(self):
        result = summary_by_category(sample())
        self.assertEqual(result, {"bills": 60.00, "gas": 45.00, "food": 20.75})

    def test_sorted_highest_first(self):
        self.assertEqual(list(summary_by_category(sample())), ["bills", "gas", "food"])

    def test_ties_sorted_alphabetically(self):
        data = [Expense(1, 10, "zoo", "2026-01-01"), Expense(2, 10, "art", "2026-01-01")]
        self.assertEqual(list(summary_by_category(data)), ["art", "zoo"])

    def test_no_float_drift(self):
        data = [Expense(i, 0.10, "x", "2026-01-01") for i in range(1, 4)]
        self.assertEqual(summary_by_category(data)["x"], 0.30)

    def test_empty(self):
        self.assertEqual(summary_by_category([]), {})


class TestMonthlySummary(unittest.TestCase):
    def test_totals(self):
        self.assertEqual(monthly_summary(sample()), {"2026-09": 68.25, "2026-10": 57.50})

    def test_sorted_oldest_first(self):
        self.assertEqual(list(monthly_summary(sample())), ["2026-09", "2026-10"])

    def test_months_across_years(self):
        data = [Expense(1, 5, "x", "2027-01-03"), Expense(2, 5, "x", "2026-12-30")]
        self.assertEqual(list(monthly_summary(data)), ["2026-12", "2027-01"])

    def test_breakdown_for_month(self):
        self.assertEqual(category_breakdown_for_month(sample(), "2026-10"),
                         {"gas": 45.00, "food": 12.50})

    def test_breakdown_for_empty_month(self):
        self.assertEqual(category_breakdown_for_month(sample(), "2025-01"), {})

    def test_total_spent(self):
        self.assertEqual(total_spent(sample()), 125.75)
        self.assertEqual(total_spent([]), 0)


class TestPrinting(unittest.TestCase):
    def capture(self, func, data):
        buf = io.StringIO()
        with redirect_stdout(buf):
            func(data)
        return buf.getvalue()

    def test_empty_messages(self):
        for func in (print_category_summary, print_monthly_summary, print_category_bar_chart):
            self.assertIn("No expenses recorded yet.", self.capture(func, []))

    def test_category_output(self):
        out = self.capture(print_category_summary, sample())
        self.assertIn("bills", out)
        self.assertIn("125.75", out)

    def test_monthly_output(self):
        out = self.capture(print_monthly_summary, sample())
        self.assertIn("2026-09", out)
        self.assertIn("68.25", out)


if __name__ == "__main__":
    unittest.main()
