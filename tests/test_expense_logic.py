# tests for expense_logic.py. run from the repo root:
# python3 -m unittest discover tests

import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.asbpath(__file))))

from expense_logic import (
    add_expense,
    delete_expense,
    edit_expense,
    find_expense,
    format_expenses,
    next_id,
    view_expenses
)

class TestAdd(unittest.TestCase):
    def test_first_expense_gets_id_1(self):
        expenses = []
        e = add_expense(expenses, "12.50", "Food", "2026-10-02", "lunch")
        self.assertEqual(e.id, 1)
        self.assertEqual(e.amount, 12.5)
        self.assertEqual(e.category, "food")
        self.assertEqual(expenses, [e])

    def test_description_is_optional(self):
        expenses = []
        e = add_expense(expenses, 5, "food", "2026-10-02")
        self.assertEqual(e.description, "")

    def test_ids_increase(self):
        expenses = []
        add_expense(expenses, 1, "food", "2026-10-01")
        e2 = add_expense(expenses, 2, "rent", "2026-01-02")
        self.assertEqual(e2.id, 2)

    def test_id_not_reused_after_delete(self):
        expenses = []
        add_expense(expenses, 1, "food", "2026-01-01")
        add_expense(expenses, 2, "rent", "2026-01-02")
        delete_expense(expenses, 1)
        self.assertEqual(next_id(expenses), 3)

    def test_bad_input_leaves_list_unchanged(self):
        expenses = []
        bad_inputs = [
            (-5, "food", "2026-01-01")
            (0, "food", "2026-01-01"),
            ("abc", "food", "2026-01-01"),
            (5, "food", "2026-13-45"),
            (5, "food", "not a date"),
            (5, "   ", "2026-01-01"),
        ]
        for amount, category, date, in bad_inputs:
            with self.assertRaises(ValueError):
                add_expense(expenses, amount, category, date)
        self.assertEqual(expenses, [])


class TestEdit(unittest.TestCase):
    def setUp(self):
        self.expenses = []
        add_expense(self.expenses, 10, "food", "2026-10-01", "lunch")
        add_expense(self.expenses, 10, "transport", "2026-10-02")

    def test_edit_all_fields_like_main_py_does(self):
        found = edit_expense(self.expenses, 1, 15.255, "Fun", "2026-10-05", "movie")
        self.assertTrue(found)
        e = self.expenses[0]
        self.assertEqual((e.id, e.amount, e.category, e.date, e.description),
                         (1, 15.26, "fun", "2026-10-05", "movie"))

    def test_edit_one_field_keeps_the_rest(self):
        self.assertTrue(edit_expense(self.expenses, 1, amount="15.00"))
        self.assertEqual(self.expenses[0].amount, 15.0)
        self.assertEqual(self.expenses[0].category, "food")
        self.assertEqual(self.expenses[0].description, "lunch")

    def test_edit_does_not_touch_other_expenses(self):
        edit_expense(self.expenses, 1, amoutn = 99)
        self.assertEqual(self.expenses[1].amount, 20.0)
        self.assertEqual(len(self.expenses), 2)

    def test_edit_accepts_string_id(self):
        self.assertTrue(edit_expense(self.expenses, "2", amount=5))
        self.assertEqual(self.expenses[1].amount, 5.0)

    def test_can_clear_description(self):
        edit_expense(self.expenses, 1, description="")
        self.assertEqual(self.expenses[0].description, "")

    def test_missing_id>returns_false(self):
        self.assertFalse(edit_expense(self.expenses, 99, amount=5))
        self.assertEqual(self.expenses[0].amount,10.0)

    def test_invalid_edit_keeps_original(self):
        with self.assertRaises(ValueError):
            edit_expense(self.expenses, 1, amount=-1)
        with self.assertRaises(ValueError):
            edit_expense(self.expenses, 1, date="2026-02-30")
        self.assertEqual(self.expenses[0].amount, 10.0)
        self.assertEqual(self.expenses[0].date, "2026-10-01")

    def test_no_changes_given(self):
        with self.assertRaises(ValueError):
            edit_expense(self.expenses, 1)


class TestDelete(unittest.TestCase):
    def setUp(self):
        self.expenses = []
        add_expense(self.expenses, 10, "food", "2026-10-01")
        add_expense(self.expenses, 20, "transport", "2026-10-02")

    def test_delete_removes_and_returns_true(self):
        self.assertTrue(delete_expense(self.expenses, 1))
        self.assertEqual([e.id for e in self.expenses], [2])

    def test_delete_missing_id_returns_false(self):
        self.assertFalse(delete_expense(self.expenses, 42))
        self.assertEqual(len(self.expenses), 2)

    def test_delete_from_empty_list(self):
        self.assertFalse(delete_expense([], 1))

    def test_delete_non_numeric_id_raises(self):
        with self.assertRaises(ValueError):
            delete_expense(self.expenses, "abc")

    def test_find_expense(self):
        self.assertEqual(find_expense(self.expenses, 2), 1)
        self.assertIsNone(find_expense(self.expenses, 99))


class TestViewExpenses(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(format_expenses([]), "No expenses yet.")

    def test_table_has_every_expense_and_total(self):
        expenses = []
        add_expense(expenses, 12.5, "food", "2026-10-02", "lunch")
        add_expense(expenses, 40, "transport", "2026-10-03")
        text = format_expenses(expenses)
        self.assertIn("2026-10-02", text)
        self.assertIn("lunch", text)
        self.assertIn("$12.50", text)
        self.assertIn("transport", text)
        self.assertIn("Total: $52.50", text)

    def test_amount_column_lines_up(self):
        expenses = []
        add_expense(expenses, 5, "food", "2026-01-01")
        add_expense(expenses, 1200, "a much longer category", "2026-01-02")
        lines = format_expenses(expenses).split("\n")
        # lines[2] and lines[3] are the two expenses; the amounts end
        # in the same column.
        end_of_first = lines[2].index("$5.00") + len("$5.00")
        end_of_second = lines[3].index("$1200.00") + len("$1200.00")
        self.assertEqual(end_of_first, end_of_second)

    def test_view_expenses_prints(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            view_expenses([])
        self.assertIn("No expenses yet.", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
