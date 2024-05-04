def bfs(graph, vertex):
    seen = {}
    values = []
    queue = [vertex]
    while queue:
        cur = queue.pop(0)
        values.append(cur)
        seen[cur] = True
        connections = graph[cur]
        for connection in connections:
            if not seen[connection]:
                queue.append(connection)
    return values