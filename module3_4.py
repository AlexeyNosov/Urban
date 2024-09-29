def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i in root_word or root_word in i:
            same_words.append(i)
    return same_words
print(single_root_words("bol", "footbol", "bol", "bolbol", "bal", "bolobol", "lob", "ol", "b"))


