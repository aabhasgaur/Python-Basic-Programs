class Employee:
    def __init__(self,name,id):
        self.id=101
        self.name="john"
    def display(self):
        print("ID:%d\nName:%s\n"%(self.id,self.name))

emp1=Employee("John",101)
emp1.display()
