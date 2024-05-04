def invert_bt(node):
    if node is None:
        return None
    left = invert_bt(node.left)
    right = invert_bt(node.right)
    node.left = right
    node.right = left
    return node