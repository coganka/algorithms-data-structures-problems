from collections import deque

def level_order_traversal(root):
    res = []
    if root is None:
        return res
    queue = deque([root])
    while len(queue):
        count = 0
        length = len(queue)
        cur_lvl_vals = []
        while count < length:
            cur = queue.popleft()
            cur_lvl_vals.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            count += 1
        res.append(cur_lvl_vals)
    return res