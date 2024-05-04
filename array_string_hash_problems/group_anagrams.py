def groupAnagrams(strs):
    hash = {}
    for word in strs:
        key = ''.join(sorted(word))        
        if key not in hash:
            hash[key] = []
        hash[key].append(word)
    return hash.values()