import heapq
from bellman_ford import Graph

graph = Graph()

def dijkstra(src):
    distances = [float("inf")] * graph.Vertices
    distances[src] = 0
    pq = [(0,src)]

    while pq:
        distance, u = heapq.heappop(pq)
        if distance > distances[u]:
            continue

        for edge in graph:
            if edge[0] == u:
                v, w = edge[1], edge[2]
                new_dist = distance + w
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    return distances