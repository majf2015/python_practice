import random

def guess(number, n):
    n += 1
    gue = int(raw_input('please guess ,and enter one number between 200 and 300 : '))
    if gue == number:
        print "Bingo!!!"
        print "you have guessing %d times " % n
    elif gue > number:
        print "your guess is too big"
        return guess(number, n)
    elif gue < number:
        print "your guess is too small"
        return guess(number, n)

number = random.randint(200, 300)
n = 0
guess(number, n)
