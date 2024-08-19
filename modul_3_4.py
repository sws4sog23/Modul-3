def single_root_words(wroot_word, *other_wordsrds):
    same_words = []
    s = 0
    for i in other_wordsrds:
        s += len(i)
    if len(wroot_word) <= s / len(other_wordsrds):
        for i in other_wordsrds:
            if wroot_word.lower() in i.lower():
                same_words.append(i)
    else:
        for i in other_wordsrds:
            if i.lower() in wroot_word.lower():
                same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
