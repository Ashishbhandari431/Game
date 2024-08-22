# #file writing 
# name=input("enter name")
# f=open("bim.txt","a")
# f.write(name)
# f.close()

#WAP to display content of file
# f=open("bim.txt","r")
# print(f.read())
# f.close()

name=input("Enter your name: ")
add=input("Addres halum")
age=input("Age: ")
f=open("data.txt","w")
f.write(name+"\n")
f.write(add+"\n")
f.write(age+"\n")
f.close()