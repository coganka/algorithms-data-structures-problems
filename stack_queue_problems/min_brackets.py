def min_brackets(st):
    st_list = list(st)
    stack = []
    count = 0
    i = 0
    while i < len(st_list):
        if st_list[i] == '(':
            stack.append(i)
            i+=1
        elif st_list[i] == ')' and len(stack):
            stack.pop()
            i+=1
        elif st_list[i] == ')':
            st_list.pop(i)
            count += 1
        else:
            i+=1
    while len(stack):
        cur_id = stack.pop()
        st_list.pop(cur_id)
        count += 1
    return ("".join(st_list), count)