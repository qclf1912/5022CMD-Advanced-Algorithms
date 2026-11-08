"""Command-line Pharmacy Inventory System."""

from hashTable import LinearProbingHashTable
import hashLib


# Display the available operations in the inventory system.
def display_menu():
    """Display the main menu options."""
    print("\n==== Pharmacy Inventory System ====")
    print(" 1. Insert Product")
    print(" 2. Search Product")
    print(" 3. Edit Product")
    print(" 4. Delete Product")
    print(" 5. Display Hash Table")
    print(" 6. Run Performance Comparison (Hash Table vs Array)")
    print(" 7. Exit")


# Initialize the inventory system and process the user's selections.
def main():
    capacity = 23
    table = LinearProbingHashTable(capacity)
    array = []

    # Load sample products into both data structures at startup for comparison.
    for p in hashLib.sample_products():
        table.insert(p.product_id, p)
        array.append(p)

    choice = ""
    while choice != "7":
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        # Execute the operation based on the selected menu option.
        match choice:
            case "1":
                hashLib.insert_product(table, array)
            case "2":
                hashLib.search_product(table, array)
            case "3":
                hashLib.edit_product(table)
            case "4":
                hashLib.delete_product(table, array)
            case "5":
                print(f"\nHash table (capacity {table.size})")
                table.display()
            case "6":
                hashLib.run_comparison()
            case "7":
                print("\nExiting Pharmacy Inventory System. Goodbye! :D")
            case _:
                print("Invalid choice. Please enter a number from 1 to 7.")


# Start the program when this file is executed directly.
if __name__ == "__main__":
    main()
