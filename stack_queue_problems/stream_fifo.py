class FIFO:
    def __init__(self, data):
        self.data = data

    def add(self, value):
        self.data.append(value)
        return self
    
    def pop(self):
        if len(self.data) > 0:
            return self.pop(0)
        return "data is empty"
    
    def find_index(self, value):
        for i,num in enumerate(self.data):
            if num == value:
                return i
        raise ValueError("Value not found")
    
    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
            return self
        raise ValueError("Value not found")