def mergeAlternately(word1, word2):
    if word1 == "":
        return word2
    if word2 == "":
        return word1
    alt_string = ""
    min_length = min(len(word1), len(word2))
    i = 0
    for i in range(0,min_length):
        alt_string += word1[i]
        alt_string += word2[i]

    alt_string += word1[min_length:]
    alt_string += word2[min_length:]

    return alt_string

mergeAlternately("abc", "pqr")