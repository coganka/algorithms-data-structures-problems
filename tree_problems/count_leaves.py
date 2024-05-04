def count_leaves(root, count = 0):
    if root is None:
        return count
    if root.left is None and root.right is None:
        count += 1
    return count + count_leaves(root.left, count) + count_leaves(root.right, count)