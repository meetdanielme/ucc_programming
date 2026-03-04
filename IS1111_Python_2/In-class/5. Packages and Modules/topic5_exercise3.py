# topic5_lecture2_exercise3.py
# Lecture 2 | Exercise 3: Fix the import bugs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Time: ~10 minutes
#
# Below are 5 independent code snippets. Each contains exactly one
# bug related to imports, module organisation, or the if __name__
# guard. The rest of the code in each snippet is correct.
#
# For each snippet:
#   1. Identify what is wrong.
#   2. Write the corrected version in the space provided.
#
# All snippets are from a fictional bookshop system split across:
#   main.py, shop_operations.py, data_handler.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ═══════════════════════════════════════════════════════════════════
# BUG 1 - Wrong import syntax
# ═══════════════════════════════════════════════════════════════════
# File: main.py
#
# BROKEN:
#   import from shop_operations get_book_price
#   print(get_book_price("B001"))
#
# What is wrong?
# import from is not correct syntax for importing in Python. The correct syntax is either:
#   from shop_operations import get_book_price
#   import shop_operations
#
# Fixed version:
# from shop_operations import get_book_price
# print(get_book_price("B001"))


# ═══════════════════════════════════════════════════════════════════
# BUG 2 - Importing the module but forgetting to qualify the call
# ═══════════════════════════════════════════════════════════════════
# File: main.py
#
# BROKEN:
#   import shop_operations
#   print(get_book_price("B001"))    # <-- this line causes a NameError
#
# What is wrong?
# The function call is not complete. It needs to include the module name as a qualifier, since we imported the whole module and not the function directly.
#
# Two ways to fix it (write both):
# Fix A (change the import):
# 
# from shop_operations import get_book_price
#
# Fix B (change the function call, keep the import):
#
# print(shop_operations.get_book_price("B001"))


# ═══════════════════════════════════════════════════════════════════
# BUG 3 - Importing a function that does not exist in that module
# ═══════════════════════════════════════════════════════════════════
# File: main.py
#
# shop_operations.py contains:  get_book_price(), add_book(), search_books()
# data_handler.py   contains:  save_catalogue(), load_catalogue()
#
# BROKEN:
#   from data_handler import get_book_price
#   price = get_book_price("B001")
#
# What is wrong?
# The function `get_book_price` does not exist in `data_handler.py`. It exists in `shop_operations.py`.
#
# Fixed version:
# from shop_operations import get_book_price
# price = get_book_price("B001")


# ═══════════════════════════════════════════════════════════════════
# BUG 4 - Missing if __name__ guard causes unintended side effects
# ═══════════════════════════════════════════════════════════════════
# These are the complete contents of two files.
#
# shop_operations.py:
#   def get_book_price(book_id):
#       prices = {"B001": 12.99, "B002": 8.50}
#       return prices.get(book_id, 0.0)
#
#   print("Testing get_book_price...")
#   print(get_book_price("B001"))
#
# main.py:
#   from shop_operations import get_book_price
#   print(f"Price: €{get_book_price('B002'):.2f}")
#
# PART A - Predict the output
# When main.py is run, what is printed to the console?
# Write your prediction before discussing with a neighbour.
#
# TODO: Write the exact output here, one line per printed value:
# Line 1: Testing get_book_price...
# Line 2: 12.99
# Line 3: Price: €8.50
#
# Were you surprised? Why or why not?
# TODO: No, because the print statements in shop_operations.py are executed during import, which is not intended.
#
# PART B - Identify and fix
# What is wrong with shop_operations.py, and how do you fix it so
# that the test output only appears when shop_operations.py is run
# directly?
#
# What is wrong?
# TODO: The print statements in shop_operations.py are executed when the module is imported, not when it's run directly.
#
# Fixed shop_operations.py:
# TODO: Add if __name__ == "__main__": guard
# shop_operations.py:
# def get_book_price(book_id):
#     prices = {"B001": 12.99, "B002": 8.50}
#     return prices.get(book_id, 0.0)
#
# if __name__ == "__main__":
#     print("Testing get_book_price...")
#     print(get_book_price("B001"))


# ═══════════════════════════════════════════════════════════════════
# BUG 5 - Circular import
# ═══════════════════════════════════════════════════════════════════
# File structure:
#   main.py             imports from shop_operations and data_handler
#   shop_operations.py  imports from data_handler
#   data_handler.py     imports from shop_operations   <-- problem
#
# BROKEN (data_handler.py):
#   from shop_operations import get_book_price   # <-- circular!
#
#   def save_catalogue(catalogue, filename):
#       with open(filename, "w") as f:
#           for book_id in catalogue:
#               price = get_book_price(book_id)   # calls shop_operations!
#               f.write(f"{book_id},{price}\n")
#
# What is wrong?
# TODO: The circular import occurs because data_handler.py imports from shop_operations.py, and shop_operations.py imports from data_handler.py.
#
# How do you fix the design so the circular import is not needed?
# TODO: Refactor the code to eliminate the circular dependency, possibly by creating a third module for shared functionality or moving the necessary functions to one of the existing modules.