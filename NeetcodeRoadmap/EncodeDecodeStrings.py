# add length plus delimiter
def encode(strs) -> str:
    if strs == [] or strs == None:
        return None
    output = ""

    for i in range(0,len(strs)):
        output += str(len(strs[i])) + "$"
        output += str(strs[i])

    return output





def decode(s: str):
    if s == [] or s == None:
        return None
    output = []

    i = 0
    while i < len(s):
        num = ""
        while s[i] != "$":
            num += s[i]
            i = i + 1
        num = int(num)
        word = s[i+1:i+1+num]
        output.append(word)
        i = i + num + 1

    return output

strs = ["we","say",":","yes","!@#$%^&*()"]

s = encode(strs)
ans = decode(s)
print(ans)