def in_order_dfs(root):
    res = []
    def _helper(node,res):
        if node is None:
            return
        if node.left:
            _helper(node.left, res)
        res.append(node.value)
        if node.right:
            _helper(node.right, res)
    _helper(root, res)
    return res