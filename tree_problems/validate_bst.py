def validate_bst(root):
    if root is None:
        return None
    return helper(root, float("-inf"), float("inf"))

def helper(node, min_val, max_val):
    if node.value <= min_val or node.value >= max_val:
        return False
    if node.left:
        if not helper(node.left, min_val, node.value):
            return False
    if node.right:
        if not helper(node.right, node.value, max_val):
            return False
    return True