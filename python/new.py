#exception handling
a=int(input("Num1: "))
b=int(input("Num2: "))
try:
    div=a/b
    print("The result is ",div)
# except (ZeroDivisionError,NameError) as r:
#     print(r)
except:
    print("error bhayo hauu error")
else:
    print("khatra ho dai tapai error vayena")
finally:
    print("mata chalxu chalxu")