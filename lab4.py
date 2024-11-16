# Hash implementation using chaining
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert a key into the hash table
    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    # Show the hash table
    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

def main():
    # Create data
    inputs = [10, 24, 46, 37, 66, 74, 33]
    hash_table = HashTable(len(inputs))

    # Insert data
    for key in inputs:
        hash_table.insert(key)

    # Show the results of our efforts
    hash_table.display()

if __name__ == "__main__":
    main()