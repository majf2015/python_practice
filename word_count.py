word_len = 0
with open('123.txt', 'r') as f:
    words = f.read().split()
    for word in words:
        if word == 't':
            word_len += 1
    print word_len

