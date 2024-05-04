class Graph:
    def __init__(self, vertices):
        self.Vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u,v,w])

    def bellman_ford(self, source):
        distances = [float("inf")] * self.Vertices
        distances[source] = 0

        for _ in range(self.Vertices - 1):
            for u, v, w in self.graph:
                if distances[u] != float("inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
        
        for u, v, w in self.graph:
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                print("Negative cycle has found")
                return 
        
        self.print_solution(distances)
    
    def print_solution(self, distances):
        print("Vertex distance from Source: ")
        for i in range(self.Vertices):
            print(f'{i}  {distances[i]}')