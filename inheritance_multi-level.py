class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barking!")

class DogChild(Dog):
    def eat(self):
        print("Dog is eating.")

d=DogChild()
d.speak()
d.bark()
d.eat()
