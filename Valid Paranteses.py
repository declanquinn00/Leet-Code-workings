# Bad Solution use stack next time 
s1 = "(())"
s2 = "(()[]())"
s3 = "("
s4 = "([])"
s5 = "([)]"
s6 = "(("
s7 = "(([]){})"
s8 = "[([]])"


def isValid(s):
    i = len(s)-1
    j = 0
    l = [char for char in s]


    if len(l) <= 1:
        return False

    while i >= 0:
       found = False
       j = i
       if l[i] != "X":
           if l[i] != "Y":
               if l[i] == "(":
                   while j < len(l):
                        if l[j] == ")" and found == False:
                            if j+1<len(l):
                                tmpb = l[j+1]
                                if tmpb == "Y":
                                    return False
                                #if tmpa == "Y" and tmpb == "Y":
                                #    return False
                            found = True
                            l[j] = "Y"
                        j = j + 1
                   l[i] = "X"
                   if found == False:
                       return False
               elif l[i] == "{":
                   while j < len(l):
                       if l[j] == "}" and found == False:
                           if j + 1 < len(l):
                               tmpb = l[j + 1]
                               if tmpb == "Y":
                                   return False
                           found = True
                           l[j] = "Y"
                       j = j + 1
                   l[i] = "X"
                   if found == False:
                       return False
               elif l[i] == "[":
                   while j < len(l):
                       if l[j] == "]" and found == False:
                           if j + 1 < len(l):
                               tmpb = l[j + 1]
                               if tmpb == "Y":
                                   return False
                           found = True
                           l[j] = "Y"
                       j = j + 1
                   l[i] = "X"
                   if found == False:
                       return False
       if found == False and l[i] != "Y" and l[i] != "X" and l[i] != ")" and l[i] != "}" and l[i] != "]":
           return False
       i = i - 1

    for char in l:
        if char != "X" and char != "Y":
            return False

    return True


print(isValid(s1));
print(isValid(s2));
print(isValid(s3));
print(isValid(s4));
print(isValid(s5));
print(isValid(s6));
print(isValid(s7));
print(isValid(s8));
