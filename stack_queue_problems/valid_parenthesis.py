parens = {'{': '}', '[': ']', '(': ')'}

def valid_parens(s):
    if len(s) == 0:
        return True
    stack = []
    for i in range(len(s)):
        if s[i] in parens:
            stack.append(s[i])
        else:
            left_bra = stack.pop()
            cor_bra = parens[left_bra]
            if cor_bra != s[i]:
                return False
    return len(stack) == 0