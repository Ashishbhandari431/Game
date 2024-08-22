from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Message")
root.geometry("800x800")
def first():
    messagebox.showinfo("hiiiiii","Dont have a nice day")
def abc():
    messagebox.showerror("Error","Naauney raixa vai xoddeu coding")
def ab():
    messagebox.showwarning("Alert","xoddey kya bhai nagar code janinas")
bt1=Button(root,text="Thichum",width=15,height=2,fg="yellow",bg="red",command=first)
bt1.pack()
bt2=Button(root,text="Thichum feri",width=15,height=2,fg="red",bg="yellow",command=abc)
bt2.pack()
bt3=Button(root,text="Thichum ya pani",width=15,height=2,fg="white",bg="blue",command=ab)
bt3.pack()
bt4=Button(root,text="Feri thichum hai la",width=15,height=2,fg="white",bg="black",command=root.destroy)
bt4.pack()
root.mainloop()