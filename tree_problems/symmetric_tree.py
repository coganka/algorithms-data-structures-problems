def is_symmetric(root):
    return helper(root, root)

def helper(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1.val == t2.val and helper(t1.left, t2.right) and helper(t1.right, t2.left)