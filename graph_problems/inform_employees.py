def find_needed_time(n, managers, inform_time, head_id):
    adj_list = [[] for _ in managers]
    for employee in range(n):
        manager = managers[employee]
        if manager == -1:
            continue
        adj_list[manager].append(employee)
    return dfs(head_id, adj_list, inform_time)

def dfs(cur_id, adj_list, inform_time):
    if len(adj_list[cur_id]) == 0:
        return 0
    max_val = 0
    subords = adj_list[cur_id]
    for subord in subords:
        max_val = max(max_val, dfs(subord, adj_list, inform_time))
    return max_val + inform_time[cur_id]