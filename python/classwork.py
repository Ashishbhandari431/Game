class College:
    def __init__(self,cname,caddress):
        self.cname=cname
        self.caddress=caddress
class Student:
    def __init__(self,sname,saddress):
        self.sname=sname
        self.address=saddress
class Library(College,Student):
    def __init__(self,cname,caddress,sname,saddress,bookname):
        College.__init__(self,cname,caddress)
        Student.__init__(self,sname,saddress)
        self.bookname=bookname
lib=Library("MMC","Bhadrapur","Bivek","DLB","C")
print(lib.__dict__)