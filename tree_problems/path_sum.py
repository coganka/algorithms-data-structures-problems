def has_sum(root, target_sum):
    if root is None:
        return False
    return helper(root, 0, target_sum)

def helper(node, cur_sum, target_sum):
    if node is None:
        return False
    cur_sum += node.value
    if cur_sum == target_sum and node.left is None and node.right is None:
        return True
    return (helper(node.left, cur_sum, target_sum) or helper(node.right, cur_sum, target_sum))