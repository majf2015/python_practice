# encoding:utf-8


#---用数列表示加运算---
def add(s1, s2):
    ss = ['0', '0']
    ss1 = s1.split('.')
    ss2 = s2.split('.')
    sss = str(float('0.' + ss1[1]) + float('0.' + ss2[1]))
    ss[0] = str(int(ss1[0]) + int(ss2[0]) + int(sss.split('.')[0]))
    ss[1] = str(int(sss.split('.')[1]))
    print ss


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


#---用数列表示乘法运算---





s1 = '33.33'
s2 = '232.776'
add(s1, s2)
reduce(s1, s2)