"""Entity class for a pharmacy product."""
class Product:
    """A single pharmacy product."""
    # Initialize a product with its ID, name, price, and stock quantity.
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id   # int   : unique key used by the hash table
        self.name = name               # str   : human-readable product name
        self.price = price             # float : price in RM (2 decimal places)
        self.stock = stock             # int   : whole units in stock

    # Return product details in a readable format when the object is printed.
    def __str__(self):
        return (f"ID: {self.product_id} | Name: {self.name} | "
                f"Price: RM{self.price:.2f} | Stock: {self.stock}")