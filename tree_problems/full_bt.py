def is_full_bt(root):
    if root is None:
        return True  
    if root.left is None and root.right is None:
        return True 
    if root.left is None or root.right is None:
        return False  
    return is_full_bt(root.left) and is_full_bt(root.right)