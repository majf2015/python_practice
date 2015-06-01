import os

file_n = 0
code_row = 0
null_row = 0
note_row = 0

for i in os.walk('D:\QQMusicCache'):
    print len(i[2]), i
    if len(i[2]) != 0:
        for j in i[2]:
            if os.path.splitext(j)[1] == '.py':
                file_n += 1
                for line in open(os.path.join(i[0], j), 'r').readlines():
                    if line == '\n':
                        null_row += 1
                    elif line[0] == '#':
                        note_row += 1
                    else:
                        code_row += 1

print 'file_n , code_row, null_row, note_row:%d, %d, %d, %d ' % (file_n , code_row, null_row, note_row)