import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self._index = 0
    
    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, self._index, item))
        self._index += 1
    
    def dequeue(self):
        return heapq.heappop(self.queue)[-1]
    
    def peek(self):
        return self.queue[0][-1]
    
    def count(self):
        return len(self.queue)