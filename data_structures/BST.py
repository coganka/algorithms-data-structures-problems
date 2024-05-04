class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            cur_node = self.root
            while True:
                if value < cur_node.value:
                    if cur_node.left is None:
                        cur_node.left = new_node
                        return
                    cur_node = cur_node.left
                else:
                    if cur_node.right is None:
                        cur_node.right = new_node
                        return
                    cur_node = cur_node.right
    
    def lookup(self, value):
        if self.root is None:
            return False
        cur_node = self.root
        while cur_node:
            if value == cur_node.value:
                return True
            elif value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right
        return False
    
    def remove(self, value):
        self.root = self._remove_node(self.root, value)
    
    def _remove_node(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove_node(node.left, value)
        elif value > node.value:
            node.right = self._remove_node(node.right, value)
        else: 
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._remove_node(node.right, successor.value)
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node