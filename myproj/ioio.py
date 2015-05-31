import os
import pprint


class FileManager(object):
    def __init__(self):
        self.__dic = {1 : '..', 2 : 'exit', 3 : 'C:', 4 : 'D:', 5 : 'E:', 6 : 'F:'}
        self.__id = 0
        self.__directory = ''

    def get_id(self):
        return self.__id

    def set_id(self,d):
        self.__id = d

    def print_dic(self):
        if self.__directory != '':
            n = 3
            lis = os.listdir(self.__directory)
            for i in lis:
                self.__dic[n] =i
                n += 1

        massage = ''
        for k, v in self.__dic.iteritems():
            if k % 10 == 0:
                massage += '\n'
            massage += '  ' + str(k) + ':' + str(v)
        print massage

    def choose_id(self):
        while not self.__dic.has_key(self.__id):
            try:
                self.__id = int(raw_input('please enter your choice:'))
            except:
                print 'wrong input'
                continue

        if self.__id == 1 and self.__directory != '':
            self.__directory = os.path.dirname(self.__directory)
        elif self.__id ==2:
            return 3
        elif self.__directory != '':
            self.__directory += '/' + self.__dic[self.__id]
        else:
            self.__directory = self.__dic[self.__id] + '/'

        if os.path.isfile(self.__directory):
            self.__directory = os.path.dirname(self.__directory)
            return 0
        return 1

    def print_file(self):
        path_file = os.path.join(self.__directory,self.__dic[self.__id])
        with open(path_file, 'r') as f:
            print f.read()


file1 = FileManager()
while file1.get_id() == 0 :
    file1.print_dic()
    choose = file1.choose_id()
    if choose == 0:
        file1.print_file()
    elif choose == 3:
        break
    file1.set_id(0)
