def max_depth(node, cur_depth = 0):
    if node is None:
        return cur_depth
    return max(max_depth(node.left, cur_depth + 1), max_depth(node.right, cur_depth + 1))