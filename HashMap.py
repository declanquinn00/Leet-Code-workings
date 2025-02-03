class MyHashMap:

    def __init__(self):
        self.size = 10 ** 6 + 1  # Define a large enough size to accommodate all possible values
        self.data = [-1] * self.size  # Initialize all values to -1 (indicating absence)
    def put(self, key: int, value: int) -> None:
        self.data[key] = value
    def get(self, key: int) -> int:
        return self.data[key]
    def remove(self, key: int) -> None:
        self.data[key] = -1  # Remove the key-value pair by resetting to -1
