
def word_layout(words):
    re_word = ''
    for_word = ''
    for word in words:
        if word.isalpha():
            for_word += word
        else:
            if for_word == '':
                re_word += word
            else:
                re_word += layout(for_word)[1: ]
                for_word = ''
                re_word += word

    if for_word != '':
        re_word += layout(for_word)[1: ]
    return re_word


def layout(for_word):
    if for_word[0].isupper():
        for_word += for_word[0].lower() + 'ay'
        for_word = for_word[0] + for_word[1].upper() +for_word[2: ]
    else :
        for_word += for_word[0] + 'ay'

    return for_word


cases = ["we are all lone, \tright? \n   yes sb,,,,,,wweewww @we you, ^^^\n^^^&&&", "",
         "samw slkdfjls eerw", "very defin", "]]]]]]]]  we ,,, \t\n\r"]

for con in cases:
    print "origin txt:", con
    print "output:", word_layout(con)


