# -*- coding: utf-8 -*-

class Person:

    def __init__(self, n, s, h, w):
        self.name = n
        self.sex = s
        self.height = h
        self.weight = w

    def set_name(self, n):
        self.name = n

    def set_sex(self, s):
        self.sex = s

    def set_height(self, h):
        self.height = h

    def set_weight(self, w):
        self.weight = w

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def to_string(self):
        return ' '.join([self.name, self.sex, self.height, self.weight])

class CharacterInquirySystem:
    def __init__(self):
        self.dic = {}
        self.func_dir = {'q': self.query, 'i': self.insert, 'u': self.update, 'd': self.delete}
        self.__read__()


    def query(self):
        while True:
            key = raw_input('enter the name you want to query : ').lower()
            if self.dic == {}:
                print "the characters system is empty"
                break

            if key == '':
                print "the name is empty"
            elif key == 'e':
                break
            elif not self.dic.has_key(key):
                print "The system does not have the characters you want to query"
            else:
                print '''
                name: %s
                sex: %s
                height: %scm
                weight: %skg''' % (key, self.dic[key].get_sex(), self.dic[key].get_height(), self.dic[key].get_weight())
                break

    def insert(self):
        while True:
            key = raw_input('enter the characters you want to insert : ').lower()
            if key == '':
                print "the name is empty"
            elif key == 'e':
                break
            sex = raw_input('enter the sex : ').lower()
            height = raw_input('enter the height : ').lower()
            weight = raw_input('enter the weight : ').lower()
            per = Person(key, sex, height, weight)
            if self.dic.has_key(key):
                print "system is already exist, please use update order or change your inquiry name"
            else:
                self.dic[key] = per
                print "successfully insert !"
                break

    def update(self):
        while True:
            key = raw_input('enter the characters you want to update : ').lower()
            if key == '':
                print "the name is empty"
            elif key == 'e':
                break
            sex = raw_input('enter the sex : ').lower()
            height = raw_input('enter the height : ').lower()
            weight = raw_input('enter the weight : ').lower()
            if self.dic == {}:
                print "the characters system is empty"
                break
            elif not self.dic.has_key(key):
                print "The system does not have the characters you want to update"
            else:
                if sex:
                    self.dic[key].set_sex(sex)
                if height:
                    self.dic[key].set_height(height)
                if weight:
                    self.dic[key].set_weight(weight)
                print "successfully update !"
                break

    def delete(self):
        while True:
            key = raw_input('enter the characters you want to delete : ').lower()
            if self.dic == {}:
                print "the characters system is empty"
                break
            elif key == '':
                print "the name is empty"
            elif key == 'e':
                break
            elif not self.dic.has_key(key):
                print "The system does not have the characters you want to delete"
            else:
                del self.dic[key]
                print "successfully delete !"
                break

    def __read__(self):
        with open('123.txt', 'rb') as file:
            persens = file.read()
            if persens == '':
                return
            else:
                for persen_string in persens.split('\n'):
                    per = persen_string.split(' ')
                    persen = Person(per[0], per[1], per[2], per[3])
                    self.dic[persen.get_name()] = persen

    def __write__(self):
        string = []
        for k, v in self.dic.iteritems():
            string.append(v.to_string())
        with open('123.txt', 'wb') as file:
            file.write('\n'.join(string))

    def menu(self):

        menu = '''
            q: query
            i: insert
            u: update
            d: delete
            e: exit
            enter choice:'''
        choice = ''
        while True:
            while True:
                try:
                    choice = raw_input(menu).lower()
                except(IndexError, KeyboardInterrupt,EOFError):
                    choice = 'e'
                if choice == '':
                    print 'you choice is empty'
                    continue
                else:
                    print 'you choice : %s' % choice
                if choice not in 'qiude':
                    print 'please enter the right menu'
                    choice = 'e'
                else:
                    break
            if choice == 'e':
                self.__write__()
                break
            self.func_dir[choice]()


menu = CharacterInquirySystem()
menu.menu()


