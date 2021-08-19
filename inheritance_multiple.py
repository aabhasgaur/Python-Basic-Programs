class Cal1:
    def Sum(self,a,b):
        return a+b
class Cal2:
    def Multiply(self,a,b):
        return a*b
class Cal3:
    def Divide(self,a,b):
        return a/b
class Cal4:
    def Difference(self,a,b):
        return a-b
class Derived1(Cal1,Cal2,Cal4):
    def Divided(self,a,b):
        return a/b

d=Derived1()
print(d.Sum(10,5))
print(d.Difference(10,5))
print(d.Multiply(20,6))
print(d.Divided(10,20))
