strs = ["abbc", "abbc", "abbcd"];


def longestCommonPrefix(strs):
    i = 0;
    l = 0;
    prefix = True;
    outputString = ""
    length = len(strs);
    if (length == 0):
        return outputString;
    while (prefix != False):
        for i in range(length):
            if (prefix == False):
                return outputString
            if(len(strs[i])>l):
                letterA = strs[i][l];
            else:
                return outputString;
            if (i >= 1):
                letterB = strs[i - 1][l];
                if (letterA != letterB):
                    prefix = False
                    return outputString;
        outputString += strs[0][l];
        l  = l + 1;

    return outputString;

tmp = longestCommonPrefix(strs);
print(tmp);