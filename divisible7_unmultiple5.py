def divisible7_not_multiple5():
    result = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            result.append(str(i))
    print result
    print ','.join(result)

divisible7_not_multiple5()
