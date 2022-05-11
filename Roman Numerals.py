def table(char):
    switcher={
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    return switcher.get(char, "Invalid character")

s = "LVIII"

number = 0
print(len(s)-1)
index = 0
range = len(s)
while index < range:
    tmp1 = table(s[index])
    if len(s)-1 > index:
        tmp2 = table(s[index+1])
        if tmp1 < tmp2:
            number += (tmp2 - tmp1)
            index = index + 2
        else:
            number += tmp1
            index = index + 1
    else:
        number += tmp1
        index = index + 1

print(number)