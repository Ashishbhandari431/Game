from tkinter import*
root =Tk()
root.title("App hai app")
root.geometry("1920x1080")
root.configure(bg='black')
# label = Label(root, text="Enter your gender", bg='black', fg='white', font=('Arial', 16))
# label.pack(pady=20)

# var=IntVar()
# male_radio = Radiobutton(root, text="Male", variable=var, value="Male", bg='black', fg='white', font=('Arial', 14))
# female_radio = Radiobutton(root, text="Female", variable=var, value="Female", bg='black', fg='white', font=('Arial', 14))
# others_radio = Radiobutton(root, text="Others", variable=var, value="Others", bg='black', fg='white', font=('Arial', 14))
# male_radio.grid(row=1, column=0 )
# female_radio.grid(row=1, column=1)
# others_radio.grid(row=1, column=2)

frame=Frame(root,bg="red",height=500,width=500)
frame.pack()
Enter=Entry(root,width=30)
Enter.pack()

def dis():
    a=Enter.get()
    jpt=Label(root,text=a,bg="white",fg="black")
    jpt.pack()
btn=Button(root,text="Enter",bg="green",fg="black",command=dis)
btn.pack()
root.mainloop()