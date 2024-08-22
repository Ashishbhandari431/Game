#hierarchial inheritance 

# class Person:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
# class Teacher(Person):
#     def __init__(self,name,address,salary):
#         super().__init__(name,address)
#         self.salary=salary
# class Student(Person):
#     def __init__(self,name,address,marks):
#         super().__init__(name,address)
#         self.marks=marks    
# teach=Teacher("Bishal Ghimire","Birtamode",50000)
# study=Student("Bivek Nepal","Dlb",100)
# print(teach.__dict__)
# print(study.__dict__)

class Hospital:
    def __init__(self,hname,haddress):
        self.hname=hname
        self.haddress=haddress
       
    def display(self):
        print("Welcome to  hospital")
class Patient(Hospital):
    def __init__(self,hname,haddress,pname):
        super().__init__(hname,haddress)
        self.pname=pname
class Employee(Hospital):
    def __init__(self,hname,haddress,ename,salary):
        super().__init__(hname,haddress)
        self.ename=ename
        self.salary=salary
pat=Patient("BNC","BTM","Bivek")
emp=Employee("BNC","BTM","Anamika",5000)

print(pat.__dict__)

print(emp.__dict__)