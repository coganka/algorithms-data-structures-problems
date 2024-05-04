def right_side(root):
    res = []
    helper(root, 0, res)
    return res

def helper(node, cur_lvl, res):
    if node is None:
        return
    if cur_lvl >= len(res):
        res.append(node.value)
    if node.right:
        helper(node.right, cur_lvl+1, res)
    if node.left:
        helper(node.left, cur_lvl+1, res)
    return