"""Hash table implementation using open addressing and linear probing."""

class LinearProbingHashTable:

    # Initialize separate lists for keys, product values, and deleted slots.
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.deleted = [False] * size  # Track deleted slots using tombstone markers.

    # Calculate the hash index using the modulo operation.
    def _hash(self, key):
        """Internal integer modulo hash function for numeric product IDs."""
        return key % self.size

    # Search for a key by following the linear probing sequence.
    def find_index(self, key):
        index = self._hash(key)

        # Check each slot until the key is found or a completely empty slot is reached.
        for _ in range(self.size):
            if self.keys[index] == key:
                return index

            # Stop searching if the slot is empty and was never deleted.
            # Tombstones must be skipped because the key may exist further along.
            if self.keys[index] is None and not self.deleted[index]:
                return -1

            # Move to the next slot and wrap around when reaching the end.
            index = (index + 1) % self.size

        return -1

    # Insert a key-value pair or update the value if the key already exists.
    def insert(self, key, value):
        """Return the inserted slot index, or -1 if the table is full."""

        # Prevent duplicate keys by updating the existing value.
        existing = self.find_index(key)
        if existing != -1:
            self.values[existing] = value
            return existing

        home = self._hash(key)
        index = home
        first_tombstone = None

        # Find an available slot by checking consecutive positions.
        for _ in range(self.size):
            if self.keys[index] is None and not self.deleted[index]:

                # Prefer reusing the first deleted slot encountered.
                target = first_tombstone if first_tombstone is not None else index
                self.keys[target] = key
                self.values[target] = value
                self.deleted[target] = False
                return target

            # Remember the first tombstone so it can be reused.
            if self.deleted[index] and first_tombstone is None:
                first_tombstone = index

            index = (index + 1) % self.size

        # Reuse a tombstone if no completely empty slot is available.
        if first_tombstone is not None:
            self.keys[first_tombstone] = key
            self.values[first_tombstone] = value
            self.deleted[first_tombstone] = False
            return first_tombstone

        # Return -1 when every slot is occupied and no tombstone is available.
        return -1

    # Search for a key and return its product value together with its slot index.
    def search(self, key):
        """Return the product value and its slot index, or (None, -1) if not found."""
        index = self.find_index(key)

        if index == -1:
            return None, -1

        return self.values[index], index

    # Retrieve only the product value without returning its slot index.
    def get(self, key):
        """Return the value for a key, or None if the key does not exist."""
        value, _ = self.search(key)
        return value

    # Delete a key and its corresponding product value from the hash table.
    def delete(self, key):
        """Mark the deleted position as a tombstone to preserve the probing sequence."""
        index = self.find_index(key)

        if index == -1:
            return False

        self.keys[index] = None
        self.values[index] = None

        # Keep a tombstone marker so searches can continue past this position.
        self.deleted[index] = True
        return True

    # Display every slot, including empty and previously deleted positions.
    def display(self):
        for i in range(self.size):
            tag = " (tombstone)" if self.deleted[i] else ""
            val = f" | {self.values[i]}" if self.keys[i] is not None else ""
            print(f"Index [{i:2d}]: Key {self.keys[i]}{val}{tag}")
