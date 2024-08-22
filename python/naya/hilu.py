from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("khai dropdown harey")
root.geometry("1920x1080")

option=StringVar()
option.set("BIM")
list=["BIM","BCA","BCS","BIT","CSIT"]
dropdown=OptionMenu(root,option,*list)
dropdown.pack()

def show():
    a=option.get()
    jpt=Label(root,text=a,bg="white",fg="black")
    jpt.pack()
bt1=Button(root,text="Users choice",command=show)
bt1.pack()
root.mainloop()