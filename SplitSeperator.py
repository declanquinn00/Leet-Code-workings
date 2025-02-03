# There is a function for this
def splitWordsBySeparator(words, separator):
    if not words:
        return []
    # create new list
    new_list = []
    for word in words:
        split_words = word.split(separator)
        for split_word in split_words:
            if split_word is not "":
                new_list.append(split_word)

    return new_list

words = ["$easy$","$problem$"]
separator = "$"
splitWordsBySeparator(words, separator)

# split() splits into "" segments so remember that!!!