#multiple and hybrid inheritance 
class Person:
    def __init__(self,pname,paddress):
        self.pname=pname
        self.paddress=paddress
class Player:
    def __init__(self,type):
        self.type=type
class Student(Person,Player):
    def __init__(self,pname,paddress,type,marks):
        Person.__init__(self,pname,paddress)
        Player.__init__(self,type)
        self.marks=marks
stu=Student("Bivek Nepal","dlb","athlete",50)
print(stu.__dict__)

#hybrid

class Arko(Person):
    def __init__(self,pname,paddress,hobby):
        super().__init__(pname,paddress)
        self.hobby=hobby
ark=Arko("Aditya","Damak","Marketing")
print(ark.__dict__)