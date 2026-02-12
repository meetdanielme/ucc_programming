# ══════════════════════════════════════════════════════════════════
# EXERCISE B: LIBRARY CATALOGUE
# Client: "PageTurner Community Library"
#
# Background:
# PageTurner is a small community library that tracks its book
# collection using a dictionary. Each book has a unique ID and a
# record containing title, genre, author, and copies owned.
#
# The librarian needs tools to answer specific questions about
# the collection. Each task uses patterns from the live demo
# but combines them in different ways.
# ══════════════════════════════════════════════════════════════════

catalogue = {
    "B001": {"title": "Normal People",       "genre": "Fiction",  "author": "Sally Rooney",    "copies": 4},
    "B002": {"title": "Dune",                "genre": "Sci-Fi",   "author": "Frank Herbert",   "copies": 2},
    "B003": {"title": "Milk and Honey",      "genre": "Poetry",   "author": "Rupi Kaur",       "copies": 3},
    "B004": {"title": "The Midnight Library", "genre": "Fiction",  "author": "Matt Haig",       "copies": 5},
    "B005": {"title": "Neuromancer",         "genre": "Sci-Fi",   "author": "William Gibson",  "copies": 1},
    "B006": {"title": "Intermezzo",          "genre": "Fiction",  "author": "Sally Rooney",    "copies": 6},
}


# ══════════════════════════════════════════════════════════════════
# TASK 1: find_books_by_author(catalogue, author_name)
# ══════════════════════════════════════════════════════════════════
# The librarian wants to find all books by a specific author.
#
# Rules:
#   - Partial match, case-insensitive (e.g. "rooney" finds
#     both "Sally Rooney" books)
#   - Return a dictionary (not a list!) mapping book_id to the
#     book's title
#   - If no matches, return an empty dictionary
#
# This uses the search pattern but the OUTPUT is a dict, not a
# list — you have to think about what the keys and values should be.
#
# Expected:
#   find_books_by_author(catalogue, "rooney")
#   → {"B001": "Normal People", "B006": "Intermezzo"}
#
#   find_books_by_author(catalogue, "tolkien")
#   → {}
# ──────────────────────────────────────────────────────────────────

def find_books_by_author(catalogue, author_name):
    pass


# Test it
print("--- Task 1: Find by Author ---")
result = find_books_by_author(catalogue, "rooney")
print("Search 'rooney':", result)

result = find_books_by_author(catalogue, "herbert")
print("Search 'herbert':", result)

result = find_books_by_author(catalogue, "tolkien")
print("Search 'tolkien':", result)

result = find_books_by_author(catalogue, "i")
print("Search 'i' (broad):", result)
print()


# ══════════════════════════════════════════════════════════════════
# TASK 2: author_summary(catalogue)
# ══════════════════════════════════════════════════════════════════
# Group books by AUTHOR (not genre) and show how many titles each
# author has and the total copies across their books.
#
# Rules:
#   - Build a summary dict: author → {"titles": n, "copies": n}
#   - Use the check-then-create-then-accumulate pattern
#   - Display a formatted table sorted by author name
#   - Also find and display which author has the MOST total copies
#     (use the best-so-far pattern on the summary you already built)
#   - Return the summary dict
#
# This combines the grouping pattern with the best-so-far pattern
# in ONE function — A2 keeps them separate.
#
# Expected output (roughly):
#   Author           Titles   Copies
#   ================================
#   Frank Herbert    1        2
#   Matt Haig        1        5
#   Rupi Kaur        1        3
#   Sally Rooney     2        10
#   William Gibson   1        1
#   ================================
#   Total            6        21
#
#   Author with most copies: Sally Rooney (10)
# ──────────────────────────────────────────────────────────────────

def author_summary(catalogue):
    pass


# Test it
print("--- Task 2: Author Summary ---")
summary = author_summary(catalogue)
print("\nReturned:", summary)
print()


# ══════════════════════════════════════════════════════════════════
# TASK 3: suggest_restock(catalogue, min_copies=3)
# ══════════════════════════════════════════════════════════════════
# Find books that have fewer copies than a threshold and display
# how many additional copies are needed to reach that threshold.
#
# Rules:
#   - Default threshold is 3 (but the caller can change it)
#   - Loop through catalogue, find books where copies < min_copies
#   - For each, calculate: needed = min_copies - current copies
#   - Display a table with book ID, title, current copies, and
#     number needed
#   - Return the total number of copies that need to be ordered
#     across all understocked books
#   - If nothing is understocked, print a message and return 0
#
# This practises: nested dict access, default parameters,
# comparisons on nested values, and accumulating a total.
#
# Expected (with default min_copies=3):
#   B002  Dune          2 copies   (need 1 more)
#   B005  Neuromancer   1 copies   (need 2 more)
#   Total copies to order: 3
#
# Expected (with min_copies=5):
#   B001  Normal People       4 copies  (need 1 more)
#   B002  Dune                2 copies  (need 3 more)
#   B003  Milk and Honey      3 copies  (need 2 more)
#   B005  Neuromancer         1 copies  (need 4 more)
#   Total copies to order: 10
# ──────────────────────────────────────────────────────────────────

def suggest_restock(catalogue, min_copies=3):
    pass


# Test it
print("--- Task 3: Restock Suggestions ---")
print("Default threshold (3):")
total = suggest_restock(catalogue)
print(f"Total to order: {total}\n")

print("Higher threshold (5):")
total = suggest_restock(catalogue, 5)
print(f"Total to order: {total}\n")

print("Very low threshold (1 — everything should be fine):")
total = suggest_restock(catalogue, 1)
print(f"Total to order: {total}\n")