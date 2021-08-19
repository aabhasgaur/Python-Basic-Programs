# Python program to define
# abstract class
from abc import ABC

class Polygon(ABC):
    #abstract method
    def sides(self):
        pass
class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")

class Square(Polygon):
    def sides(self):
        print("Square has 4 sides")

class Pentagon(Polygon):
    def sides(self):
        print("Pentagon has 5 sides")

class Hexagon(Polygon):
    def sides(self):
        print("Hexagon has 6 sides")
t=Triangle()
t.sides()
s=Square()
s.sides()
p=Pentagon()
p.sides()
h=Hexagon()
h.sides()




"""
class Employee:
    __count = 0
    def __init__(self):
        Employee.__count=Employee.__count + 1
    def display(self):
        print("The Number of Employees: ",Employee.__count)
emp=Employee()
emp2=Employee()

print(emp.display())
"""
