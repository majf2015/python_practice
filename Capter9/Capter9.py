

class FileMane:
    def __init__(self):
        pass
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
