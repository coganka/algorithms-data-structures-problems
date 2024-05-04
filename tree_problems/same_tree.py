def is_same_tree(t1, t2):
    if t1.value != t2.value:
        return False
    if t1 == None and t2 == None:
        return True
    if t1 == None or t2 == None:
        return False
    left_is_same = is_same_tree(t1.left, t2.left)
    right_is_same = is_same_tree(t1.right, t2.right)
    return t1.value == t2.value and left_is_same and right_is_same