import math

def factor(number):

    factor = []
    for n in range(1, int(math.sqrt(number)) + 1):
        fact = number / n
        if fact * n == number:
            factor.append(str(n))
            if fact != n:
                factor.append(str(fact))
    print ','.join(factor)

def factorial(number):
    if number == 0:
        return 1
    else:
        return number *  factorial(number - 1)

number = int(raw_input('please enter one number'))
factor(number)
print factorial(number)
