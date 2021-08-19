#JAVA and C++ have protected key word and to do that same thing in PYTHON you need to put
#A single underscore before any variable to make to protected.
#PROTECTED
class A:
    def __init__(self):
        self._a=56
class B(A):
    def __init__(self):
        A.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)

obj1 = B()
obj2 = A()
print(obj2.a)


#PRIVATE
#It uses double underscores before anything.
