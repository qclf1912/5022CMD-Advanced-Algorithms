"""Helper functions: sample data, input validation, array search, and benchmark."""

import time
from product import Product
from hashTable import LinearProbingHashTable


# Return sample pharmacy products to initialize the inventory system.
def sample_products():
    return [
        Product(1001, "Panadol 500mg", 8.50, 200),
        Product(1042, "Paracetamol 500mg", 5.90, 120),
        Product(1055, "Amoxicillin 250mg", 14.20, 60),
        Product(1068, "Ibuprofen 400mg", 9.80, 90),
        Product(1073, "Cetirizine 10mg", 7.30, 150),
        Product(1089, "Vitamin C 1000mg", 22.00, 80),
        Product(1094, "Loratadine 10mg", 11.50, 70),
        Product(1107, "Omeprazole 20mg", 18.90, 45),
        Product(1112, "Antacid Tablets", 6.40, 110),
        Product(1126, "Cough Syrup 100ml", 12.60, 55),
        Product(1131, "ORS Sachet", 2.50, 300),
        Product(1149, "Salbutamol Inhaler", 25.00, 30),
    ]


# Read an integer input and check whether it meets the minimum requirement.
def read_int(prompt, minimum=0):
    try:
        value = int(input(prompt))
    except ValueError:
        print("Invalid input! Please enter a whole number!")
        return None

    if value < minimum:
        print(f"Invalid input! Value cannot be less than {minimum}!")
        return None

    return value


# Read a numeric input that allows decimal values and validate its minimum.
def read_float(prompt, minimum=0.0):
    try:
        value = float(input(prompt))
    except ValueError:
        print("Invalid input! Please enter a number!")
        return None

    if value < minimum:
        print(f"Invalid input! Value cannot be less than {minimum}!")
        return None

    return value


# Read text input and reject empty or whitespace-only values.
def read_text(prompt):
    text = input(prompt).strip()

    if not text:
        print("Invalid input! Text cannot be empty!")
        return None

    return text


# Perform linear search by checking each product ID in the array.
def array_search(array, product_id):
    """Linear search through a 1D array/list. O(n)."""
    for product in array:
        if product.product_id == product_id:
            return product

    return None


# Compare the searching performance of a hash table and a normal array.
def run_comparison(n_records=20000, searches=2000):

    # Create both data structures and store the same generated products.
    table = LinearProbingHashTable(n_records * 2 + 1)
    array = []

    for i in range(n_records):
        p = Product(10000 + i, f"Item-{i}", 1.0 + i % 50, i % 500)
        table.insert(p.product_id, p)
        array.append(p)

    # Generate search keys near the end of the stored records.
    keys = [10000 + n_records - 1 - (i % 100) for i in range(searches)]

    # Measure the total execution time of hash table searching.
    t0 = time.perf_counter()
    for k in keys:
        table.get(k)
    hash_time = time.perf_counter() - t0

    # Measure the total execution time of linear array searching.
    t0 = time.perf_counter()
    for k in keys:
        array_search(array, k)
    array_time = time.perf_counter() - t0

    # Display the total and average searching times for both data structures.
    print("\n=== Performance comparison: Hash Table vs Array ===")
    print(f"Records stored          : {n_records}")
    print(f"Searches performed      : {searches}")
    print(f"Hash Table total time   : {hash_time:.6f} seconds ({hash_time / searches:.7f} s/search)")
    print(f"Array total time        : {array_time:.6f} seconds ({array_time / searches:.7f} s/search)")

    # Calculate the approximate speed difference if the hash table time is valid.
    if hash_time > 0:
        print(f"Hash table was approx. {array_time / hash_time:,.1f}x faster")


# Insert a new product into both the hash table and the array.
def insert_product(table, array):
    pid = read_int("Enter Product ID: ", 1)

    if pid is None:
        return

    # Prevent duplicate product IDs from being inserted.
    if table.get(pid) is not None:
        print("A product with this ID already exists. Use Edit to change it.")
        return

    # Collect product information with validation before creating the object.
    name = read_text("Enter Product Name: ")
    price = read_float("Enter Price: ") if name else None
    stock = read_int("Enter Stock Quantity: ") if price is not None else None

    if stock is None:
        return

    product = Product(pid, name, price, stock)

    # Insert the product into the hash table and check whether insertion succeeds.
    slot = table.insert(pid, product)
    if slot == -1:
        print("Hash table is full. Product not inserted.")
        return

    # Keep the array synchronized with the hash table.
    array.append(product)
    print(f"Product inserted successfully into slot [{slot}]")


# Search for a product and compare the execution time of both data structures.
def search_product(table, array):
    pid = read_int("Enter Product ID to search: ", 1)

    if pid is None:
        return

    # Measure hash table searching time and retrieve the product's slot index.
    t0 = time.perf_counter()
    product, slot = table.search(pid)
    hash_time = time.perf_counter() - t0

    # Measure the time taken to find the same product using linear search.
    t0 = time.perf_counter()
    array_search(array, pid)
    array_time = time.perf_counter() - t0

    if product is None:
        print("Product not found.")
        return

    print(f"Product Found! (slot [{slot}])")
    print(product)
    print(f"Search completed in {hash_time:.6f} seconds (Hash Table)")
    print(f"Search completed in {array_time:.6f} seconds (Array - same record)")


# Update the information of an existing product without changing its ID.
def edit_product(table):
    pid = read_int("Enter Product ID to edit: ", 1)

    if pid is None:
        return

    product = table.get(pid)

    if product is None:
        print("Product not found.")
        return

    # Allow users to leave fields blank to retain their current values.
    print("Leave a field blank to keep its current value.")
    name = input(f"New name [{product.name}]: ").strip()
    price = input(f"New price [{product.price:.2f}]: ").strip()
    stock = input(f"New stock [{product.stock}]: ").strip()

    try:
        new_price = float(price) if price else product.price
        new_stock = int(stock) if stock else product.stock
    except ValueError:
        print("Invalid number entered. No changes made.")
        return

    # Reject negative prices and stock quantities before updating the product.
    if new_price < 0 or new_stock < 0:
        print("Price and stock cannot be negative. No changes made.")
        return

    if name:
        product.name = name

    product.price = new_price
    product.stock = new_stock
    print("Product updated.")


# Delete a product from both the hash table and the array.
def delete_product(table, array):
    pid = read_int("Enter Product ID to delete: ", 1)

    if pid is None:
        return

    # Remove the product from the array only if hash table deletion succeeds.
    if table.delete(pid):
        array[:] = [p for p in array if p.product_id != pid]
        print("Product deleted.")
    else:
        print("Product not found.")
