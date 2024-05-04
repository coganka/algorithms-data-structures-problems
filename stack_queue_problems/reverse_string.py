def reverse_with_stack(st):
    stack = [s for s in st]
    returnStr = ""
    while len(stack) > 0:
        cur = stack.pop()
        returnStr += cur
    return returnStr