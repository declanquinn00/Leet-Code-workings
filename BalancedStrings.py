# Assuming the string is balanced
def balancedStringSplit(s):
    count = 0
    if not s:
        return count
    # loop
    count_r = 0
    count_l = 0
    for i in range(0,len(s)):
        tmp1 = s[i]
        if s[i] == "R":
            count_r +=1
        if s[i] == "L":
            count_l +=1
        if count_l == count_r:
            count_r = 0
            count_l = 0
            count += 1

    return count



s = "RLRRLLRLRL"
s2 = "RLRRRLLRLL"
print(balancedStringSplit(s2))