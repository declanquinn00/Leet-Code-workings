def isSubsequence(t, s):
    if s == "" and t == "":
        return True
    if not t:
        return False
    if not s:
        return True
    size_s = len(s)
    current_s = 0
    for i in range(len(t)):
        if t[i] == s[current_s]:
            current_s +=1
            if current_s == size_s:
                return True

    return False

print(isSubsequence("ahbgdc", "abc"))