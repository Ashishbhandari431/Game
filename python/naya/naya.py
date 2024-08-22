#fseek ftell file handling using with 
#ftell-> display current portion of file 
#ftell->to travel into any position of file 
# f=open("bishal.txt","w")
# f.write("Hello goodmorning")
# f.close()
# f=open("bishal.txt","r")
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# print(f.read())
# f.seek(0)
# print(f.read())
# f.seek(10)
# print(f.read())
# f.close()

#FILE CLOSING TECHNIQUES
# try:
#     f=open("Hi.txt","w")
#     f.write("hahahah")
    
# finally:
#     f.close()

#WITH STATEMENT 
with open("student.txt","w") as f:
    f.write("Bivek don \n")
    f.write("100/100 \n")
    f.write("A++++")    