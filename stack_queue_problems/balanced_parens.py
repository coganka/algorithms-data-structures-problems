def is_balanced(st):
    stack = []
    for s in st:
        if s == '(':
            stack.append(s)
        elif s == ')' and len(stack) > 0:
            stack.pop()
        else:
            return False
    return len(stack) == 0