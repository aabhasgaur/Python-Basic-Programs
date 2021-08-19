class C(object):
    def __init__(self):
        self.c = 21
#by adding double underscore before d it makes it a private member of a parent class
        self.__d = 42
class D(C):
    def __init__(self):
        self.e=84
        C.__init__(self)
obj1=C()
obj2=D()

print(obj1.c)
print(obj2.d)
