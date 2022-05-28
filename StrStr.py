haystack = "aaabaaabbbabaa"
needle = "babb"

def strStr(haystack, needle):
    lhay = len(haystack)
    lneedle = len(needle)
    if lneedle == None:
        return 0
    j = 1
    i = 0

    while i < lhay:
        if (haystack[i] == needle[0]):
            while j < lneedle and i + j < lhay:
                if (needle[j] != haystack[i + j]):
                    break
                j += 1
            if j >= lneedle:
                return i
        i += 1
        j = 1
    return -1
print(strStr(haystack, needle))