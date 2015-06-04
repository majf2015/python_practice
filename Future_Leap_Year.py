def FutureLeapYear():
    leap_year = []
    n = 0
    year = 2016
    while n != 20:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_year.append(str(year))
            n += 1
        year += 1
    print ','.join(leap_year)

FutureLeapYear()