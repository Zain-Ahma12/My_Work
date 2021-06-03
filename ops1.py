#Object Oriented Programing

class Person:
    def __init__(self,name,age,height,standard):
        self.name=name
        self.age=age
        self.height=height
        self.standard=standard
    def About(self):
        print(f"Hellow \nMy name is {self.name} \nMy age is {self.age} \nI am in class {self.standard}")
    def __repr__(self):
        return f'Person({self.name},{self.age},{self.height},{self.standard})'
    def __str__(self):
        return f'({self.name},{self.age},{self.height},{self.standard})'

p1=Person('Zain',21,5.1,12)
print(p1.About())
