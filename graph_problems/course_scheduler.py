def course_scheduler(n, preq):
    indegrees = [0] * n
    adj_list = [[] for _ in range(n)]
    for pair in preq:
        indegrees[pair[0]] += 1
        adj_list[pair[1]].append(pair[0])

    stack = []
    for i, degree in enumerate(indegrees):
        if degree == 0:
            stack.append(i)
    
    count = 0
    while stack:
        cur = stack.pop()
        connections = adj_list[cur]
        count += 1
        for connection in connections:
            indegrees[connection] -= 1
            if indegrees[connection] == 0:
                stack.append(connection)
    return n == count