class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adj_list = {}
    
    def add_node(self, node):
        self.adj_list[node] = []
        self.number_of_nodes += 1
    
    def add_edge(self, node1, node2):
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
    
    def remove_node(self, node):
        if node in self.adj_list:
            for _, neighbors in self.adj_list.items():
                if node in neighbors:
                    neighbors.remove(node)
            del self.adj_list[node]
            self.number_of_nodes -= 1
