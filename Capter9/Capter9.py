import re
import xlrd

class FileMane:
    def __init__(self):
        self.filter_comment = []
    def  read(self, t):
        with open("test9.txt") as file:
            if t == "read":
                file.seek(-300, 2)
                return file.read()
            elif t == "readline":

                return file.readline()
            elif t == "readlines":
                return file.readlines()
            else:
                for l in file:
                    print l.decode("GBK").encode("utf-8")
    def reads(self, t, s):
        with open("test9.txt") as file:
            if t == "read":
                return file.read(s)
            elif t == "readline":
                return file.readline(s)
            else:
                return file.readlines(s)
    def write(self, t, s):
        with open("test9.txt","a") as file:
            if t == "write":
                file.seek(0, 0)
                return file.write(s)
            else:
                return file.writelines(s)
    def seek(self):
        with open("test9.txt") as file:
            print file.seek(0, 0)
            print file.readline().decode("GBK").encode("utf-8")
            print file.seek(30, 1)
            print file.readline().decode("GBK").encode("utf-8")
            print file.seek(-300, 2)
            print file.readline().decode("GBK").encode("utf-8")

    def filter_comments(self):
        with open ("test9.txt") as file:
            com = re.compile("^[^ *#].*$") #"^[^ *#]", "^(?! *#).*$", "^(?! *#)"
            for line in file.readlines():
                mat = line.decode("GBK").encode("utf-8")
                if  re.match(com, mat):
                    self.filter_comment.append(mat)

    def top_N_row(self, N, F):
        with open(F) as file:
            for i in range(N):
                print file.readline().decode("GBK").encode("utf-8")

    def file_rows(self, F):
        with open(F) as file:
            return len(file.readlines())

    def show_page(self, F):
        with open(F) as file:
            lines = file.readlines()
            page, length = 0, len(lines)
            while (page + 1)  * 25 <= length:
                for i in range(25):
                    print lines[page * 25 + i].decode("GBK").encode("utf-8"),
                page += 1
                print_or_not = raw_input("enter any key")
                print print_or_not

            if (page + 1) * 25 > length:
                for i in range(length - page * 25):
                     print lines[page * 25 + i].decode("GBK").encode("utf-8"),

    def raw(self):
        print_or_not = raw_input("enter any key")
        print print_or_not

    def file_compare(self, F1, F2):
        with open(F1) as file1:
            with open (F2) as file2:
                lines1 = file1.readlines()
                lines2 = file2.readlines()
                if len(lines1) > len(lines2):
                    return "different position", len(lines2) + 1, 1
                elif len(lines1) < len(lines2):
                    return "different position", len(lines1) + 1, 1
                else:
                    for i in range(len(lines1)):
                        for j in range(len(lines1[i])):
                            if lines1[i][j] != lines2[i][j]:
                                return "different position", i + 1, j + 1
                return  "two files are identical"



