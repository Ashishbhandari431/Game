# #raise function (custom exception )
# age=int(input("age haal: "))
# try:
#     if age<18:
#         raise ValueError
#     print("vote ho vote")
# except ValueError:
#     print("vote halna painas fucchey hahahhaha")

#WAP to input number and display invalid if user input number 8

inp=int(input("number hala: "))
try:
    if inp==8:
        raise ValueError
    print("Good bachis")
except ValueError:
    print("kei change nagari aafno folder ma gar bhai")