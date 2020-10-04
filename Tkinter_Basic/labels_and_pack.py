import tkinter

# creating root window
root = tkinter.Tk()
root.title('Labels')
root.geometry('500x500')
root.config(bg='lightblue')  # we can use color codes , hex values etc

# lables adding widgets
# root specifies where the label has to displayed
lab1 = tkinter.Label(root, text='hello labels')
lab1.pack()

# we can use the many properties in this (text , font , gb , fg)

lab2 = tkinter.Label(root, text='hello folks', bg='green')
lab2.pack()

# if we want to allign this use properties in pack system

lab3 = tkinter.Label(root, text='hello labels')
# anchors the ie places west direction can use (N S W E)
lab3.pack(anchor='w')

# we can also add padding by padx and pady

lab4 = tkinter.Label(root, text='hello lab4')
lab4.pack(padx=10, pady=50)

# we can selectively padd ie pad at buttom but not top

lab5 = tkinter.Label(root, text='hello labels')
lab5.pack(pady=(20, 20), anchor='e', padx=(0, 10))
# does padding padding 20 at top 20  at buttom
# 0 in the left 10 at the right
# values are in pixels

# ****we can have internal padding by ipadx and ipady and give respc values *****


lab6 = tkinter.Label(root, text='hello lab6')
lab6.pack(fill='x')

#lab7 = tkinter.Label(root, text='hello lab7')
# lab7.pack(pady=(10,0), fill='y')  # does not work as hight is taken by height of letters in the text
# add expand = TRUE

lab7 = tkinter.Label(root, text='hello lab7')
lab7.pack(pady=(10, 0), fill='y', expand='TRUE')

# import both and use EXPAND in x and y direction

lab8 = tkinter.Label(root, text='hello lab7')
lab8.pack(pady=(10, 0), fill='both', expand='TRUE')

# can use the key word BOTH BY IMPORTING

# run the gaint loop
root.mainloop()
