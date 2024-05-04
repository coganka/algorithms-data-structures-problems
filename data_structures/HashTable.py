class HashTable:
    def __init__(self):
        self.hashTable = {}
        self.count = 0
    
    def insert(self, key, value):
        self.hashTable[key] = value
        self.count += 1
    
    def get(self, key):
        return self.hashTable.get(key, "Key doesn't exist.")
    
    def delete(self, key):
        self.hashTable.pop(key, "No key found.")
        self.count -= 1
