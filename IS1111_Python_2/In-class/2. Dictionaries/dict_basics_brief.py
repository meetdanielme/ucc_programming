# EXERCISE A: DICTIONARY BASICS
# Complete each section by filling in the blanks.

product = {
    "name": "Wireless Mouse",
    "price": 29.99,
    "stock": 50,
    "category": "Electronics"
}

# 1) Print the product's price
print(product["price"])


# 2) Print the product's category
print(product["category"])


# 3) Check if "brand" exists in the dictionary
if "brand" in product:
    print("Brand is listed")
else:
    print("No brand specified")


# 4) Safely get the "discount" value (use 0 as default if missing)
discount = product.get("discount", 0)
print(f"Discount: {discount}")


# 5) The product sold 5 units. Update stock to 45.
product["stock"] -= 5


# 6) Add a new key "brand" with value "Logitech"
product["brand"] = "Logitech"


# 7) Print how many key-value pairs are in the dictionary
print(len(product))


# 8) Print the entire dictionary to verify changes
print(product)