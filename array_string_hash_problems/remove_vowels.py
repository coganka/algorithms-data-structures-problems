def remove_vowels(st):
    st_list = list(st)
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    i = 0
    for s in st_list:
        if s.lower() in vowels:
            st_list.pop(i)
        i += 1
    return "".join(st_list)