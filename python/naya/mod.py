#GUI in python 
from tkinter import* 
root = Tk()
root.title("bibek ko app")
root.geometry("900x900")

# lbl1=Button(root,text="Bivek Nepal",font={"sans serif",30},foreground="red",background="yellow")
# lbl1.grid(row=1,column=10)
# lbl1=Label(root,text="Bivek Nepal",font={"sans serif",30},foreground="red",background="yellow")
# lbl1.pack(side=BOTTOM)
# lbl1=Label(root,text="Bivek Nepal",font={"sans serif",30},foreground="red",background="yellow")
# lbl1.pack(side=LEFT)
# lbl1=Label(root,text="Bivek Nepal",font={"sans serif",30},foreground="red",background="yellow")
# lbl1.pack(side=RIGHT)
def Bivek():
    lbl1=Label(root,text="Bivs",font={"sans serif",30},foreground="red",background="yellow")
    lbl1.pack()
lbl=Button(root,text="click here",font={"sans serif",30},foreground="red",background="yellow",command=Bivek)
lbl.pack()

root.mainloop()

