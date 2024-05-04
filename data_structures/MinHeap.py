class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] <= self.heap[parent_index]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest_index = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
                largest_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
                largest_index = right_child_index

            if largest_index == index:
                break

            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            index = largest_index

    def peek_max(self):
        return self.heap[0] if self.heap else None