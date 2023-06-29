from tkinter import*
import random
root=Tk()
root.title('Dictionary')
root.geometry("600x400")

dictionary={"color":["red","blue","balck","green","yellow","purple","pink","orange","white"]}
def bg_change():
    random_no=random.randint(0,8)
    print(dictionary["color"][random_no])
    root.configure(background=dictionary["color"][random_no])
btn1=Button(root,text="Click me",command=bg_change)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()