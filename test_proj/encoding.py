class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):

    def __init__(self, name, gender, course):
        Person.__init__(self, name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course