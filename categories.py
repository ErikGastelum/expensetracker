"""categories.py - The list of categories an expense is allowed to use.

Every expense must use one of these. Validation (validation.py) reads this
list, so if you ever want to add a category, this is the only place to edit.
"""

DEFAULT_CATEGORIES = ["food", "rent", "transport", "fun", "other"]
