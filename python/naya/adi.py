from tkinter import*
from tkinter import messagebox
root =Tk()
root.title("Msg box")
root.geometry("800x800")
root.configure(bg='black')
menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(menubar, tearoff=0)
def f1():
    label = label(root,text="you have clicked new")
    label.pack()
def f2():
    label = label(root,text="you have clicked open")
    label.pack()
def f3():
    label = label(root,text="you have clicked edit")
    label.pack()
    
menubar.add_cascade(label="file",menu=filemenu)
menubar.add_command(label="new",command=f1)
menubar.add_command(label="new",command=f2)
menubar.add_command(label="new",command=f3)
menubar.add_command(label="new",command=root.destroy)

def first():
    messagebox.showerror("Error","error:404 not found")
def first():
    messagebox.showerror("Error","error:404 not found")
def first():
    messagebox.showerror("Error","error:404 not found")  
root.mainloop()