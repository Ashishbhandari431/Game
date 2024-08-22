# class Hi:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,next):
#         sum=self.a+next.a
#         return sum
# obj=Hi(10)
# obj1=Hi(20)
# print(obj+obj1)

# class key:
#     def calc(self,a,b):
#         print(a+b)
# class mikey(key):
#     def calc(self,a,b):
#         super().calc(20,30)
#         print(a*b) 
# mik=mikey()
# mik.calc(10,20)

class Hello:
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def displaySum(self):
        print(self.__a+self.__b)
hi=Hello(10,20)
hi.displaySum()