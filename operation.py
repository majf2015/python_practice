# encoding:utf-8


#---用数列表示加运算---
def add(s1, s2):
    ss = ['0', '0']
    if int(float(s1)) == float(s1):
        if int(float(s2)) == float(s2):
            ss1 = [str(s1), '0']
            ss2 = [str(s2), '0']
        else:
            ss1 = [str(s1), '0']
            ss2 = s2.split('.')
    else:
        if int(float(s2)) == float(s2):
            ss1 = s1.split('.')
            ss2 = [str(s2), '0']
        else:
            ss1 = s1.split('.')
            ss2 = s2.split('.')
    sss = str(float('0.' + ss1[1]) + float('0.' + ss2[1]))
    ss[0] = str(int(ss1[0]) + int(ss2[0]) + int(sss.split('.')[0]))
    ss[1] = str(int(sss.split('.')[1]))
    print ss


#---另一种用数列表示整数加运算---
def add1(s1, s2):
    if len(s1) < len(s2):
        sss3 = s2
        s2 = s1
        s1 = sss3
    sss = ''
    sss1 = '0'
    for i in range(1, len(s2) + 1):
        sss2 = str(int(s1[-i]) + int(s2[-i]) + int(sss1) )
        sss1 = '0'
        if len(sss2) == 2:
            sss1 = sss2[0]
            sss2 = sss2[1]
        sss = sss2 +sss


    sss = str(int(s1[:len(s1) - len(s2)]) + int(sss1)) + sss


    print sss


#---用数列表示减运算---
def reduce(s1, s2):
    ss = ['0', '0']
    l = float(s1) - float(s2)
    b = 0

    if l < 0:
        ss1 = s2.split('.')
        ss2 = s1.split('.')
        b = 1

    else:
        ss1 = s1.split('.')
        ss2 = s2.split('.')

    ss[1] = float('0.' + ss1[1]) - float('0.' +ss2[1])
    if ss[1] < 0:
        ss[1] = (str(float('0.' +ss1[1]) - float('0.' +ss2[1]) + 1)).split('.')[1]
        ss[0] = str(int(ss1[0]) - int(ss2[0]) - 1)
    else:
        ss[1] = str(ss[1]).split('.')[1]
        ss[0] = str(int(ss1[0]) - int(ss2[0]))

    if b:
        ss[0] = '-' + ss[0]

    print ss



s1 = '33.33'
s2 = '232.276'
s3 = '33'
s4 = '232'
s5 = '1111123'
s6 = '92'

add(s1, s2)
add(s1, s4)
add(s2, s3)
add(s3, s4)
add1(s3, s4)
add(s5, s6)
add1(s5, s6)
reduce(s1, s2)