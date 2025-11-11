def groupAnagrams(strs):
    # edge cases
    if len(strs) == 1:
        return [strs]

    hmaps = []
    result = []
    # generate a hashmap for each index
    for i, b in enumerate(strs):
        # gen hashmap
        hmap = {}
        for char in b:
            hmap[char] = 1 + hmap.get(char, 0)
        hmaps.append(hmap)

    # add indexes we have already used
    hset = set()

    # group matched hmaps
    for index, hmap in enumerate(hmaps):
        if index not in hset:
            # create list and add the first hmap
            matches = []
            matches.append(strs[index])
            hset.add(index)
            # add any matches
            for j in range(index + 1, len(hmaps)):
                if hmap == hmaps[j]:
                    matches.append(strs[j])
                    hset.add(j)
            result.append(matches)
    return result

strs = ["act","pots","tops","cat","stop","hat"]
groupAnagrams(strs)