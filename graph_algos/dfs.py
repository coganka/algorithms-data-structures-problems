def dfs(vertex, graph, seen = {}, values = []):
    values.append(vertex)
    seen[vertex] = True
    connections = graph[vertex]
    for connection in connections:
        if not seen[connection]:
            dfs(connection, graph, seen, values)
    