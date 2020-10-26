import tkinter
from PIL import Image, ImageTk
from tkinter import IntVar, StringVar, scrolledtext, END, messagebox, filedialog

root = tkinter.Tk()
root.title("Notepad")
root.iconbitmap("notepad.ico")
root.geometry('600x600')
root.resizable(0, 0)

# fonts
bgcolor = '#FB6237'
menubox_color = '#68ca8f'
tbox_color = '#FCDE73'

root.config(bg=bgcolor)

# functions


def change(event):
    '''chnage stuff from here'''
    if stylevar.get() == 'none':
        myfont = (fontvar.get(), sizevar.get())
    else:
        myfont = (fontvar.get(), sizevar.get(), stylevar.get())
    input_text.config(font=myfont)


def new_page():
    ''' new page stuff'''
    ''' use a message box to user you sure '''
    question = messagebox.askyesno(
        'New Note', 'Are you sure you want to close this note ?')
    if question == 1:
        text = input_text.get('1.0', END)
        length = len(text)
        if length > 1:
            question = messagebox.askokcancel(
                "Are you Sure", "We see there are some file contents!!!! \n if already saved you can exit else  **do you want to save?**")
            if question == 1:
                savenote()
            else:
                input_text.delete('1.0', END)


def close_note():
    question = messagebox.askyesno(
        'Quit Notepad', 'Are you sure you wanna quit')
    if question == 1:
        text = input_text.get('1.0', END)
        length = len(text)

        if length > 1:
            question = messagebox.askokcancel(
                "Are you Sure", "We see there are some file contents!!!! \n if already saved you can exit else  **do you want to save?**")
            if question == 1:
                savenote()
        else:
            root.destroy()


def savenote():
    '''first 3 lines are saved with styles'''
    # use file dialog to get directory and name where to save the file
    save_name = filedialog.asksaveasfilename(
        initialdir='./', title="Save Note", filetypes=(("Text Files", "*.txtt"), ("Python Files", "*.py"), ('All Files', "*.*")))
    if '.' not in save_name:
        save_name = save_name + '.txtt'
        with open(save_name, 'w') as f:
            f.write(fontvar.get() + "\n")
            f.write(str(sizevar.get()) + "\n")
            f.write(stylevar.get() + "\n")

            # write remaining text

            f.write(input_text.get("1.0", END))
    else:

        with open(save_name, 'w') as f:
            f.write(fontvar.get() + "\n")
            f.write(str(sizevar.get()) + "\n")
            f.write(stylevar.get() + "\n")

            # write remaining text

            f.write(input_text.get("1.0", END))


def opennote():
    '''open the doc again'''
    # use file dialoge to get loaction and directory
    open_name = filedialog.askopenfilename(
        initialdir="./", title="Open note", filetypes=(("Text Files", "*.txtt"), ("Python Files", "*.py"), ('All Files', "*.*")))
    with open(open_name, 'r') as f:
        input_text.delete("1.0", END)

        # first 3 lines are for styles and remember to strip the new line char we used
        fontvar.set(f.readline().strip())
        sizevar.set(int(f.readline().strip()))
        stylevar.set(f.readline().strip())

        # call the change font for that set methods and remember to pass anystuff
        change(1)

        # read the rest of the file and insert it
        # the pointer is on the 4th file
        text = f.read()
        input_text.insert('1.0', text)


# frames
menuframe = tkinter.Frame(root, bg=menubox_color)
textframe = tkinter.Frame(root, bg=bgcolor)
menuframe.pack(pady=10, padx=10)
textframe.pack()

# layouts

# to add image as button open the image and use the instance
new_image = ImageTk.PhotoImage(Image.open("new.png"))
new_button = tkinter.Button(menuframe, image=new_image, command=new_page)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
open_button = tkinter.Button(menuframe, image=open_image, command=opennote)
open_button.grid(row=0, column=2, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open("save.png"))
save_button = tkinter.Button(menuframe, image=save_image, command=savenote)
save_button.grid(row=0, column=1, padx=5, pady=5)

quit_image = ImageTk.PhotoImage(Image.open("quit.png"))
quit_button = tkinter.Button(menuframe, image=quit_image, command=close_note)
quit_button.grid(row=0, column=3, padx=5, pady=5)

# for creating the dropdown we use the option menu
font_list = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Calibria',
             'Georgia', 'MS Georgia', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
fontvar = StringVar()

dropbox = tkinter.OptionMenu(menuframe, fontvar, *font_list, command=change)
fontvar.set('Terminal')
dropbox.config(width=16)
dropbox.grid(row=0, column=4, padx=5, pady=5)

size = ['6', '8', '12', '16', '20', '22', '26', '32', '36', '40', '42']
sizevar = IntVar()
dropintbox = tkinter.OptionMenu(menuframe, sizevar, *size, command=change)
sizevar.set('12')
dropintbox.config(width=2)
dropintbox.grid(row=0, column=5, padx=5, pady=5)

stylelist = ['none', 'italic', 'bold']
stylevar = StringVar()
styledropbox = tkinter.OptionMenu(
    menuframe, stylevar, *stylelist, command=change)
stylevar.set('none')
styledropbox.config(width=6)
styledropbox.grid(row=0, column=6, padx=5, pady=5)


myfont = (fontvar.get(), sizevar.get())
# makings a textbox for takiing input from the user

input_text = scrolledtext.ScrolledText(
    textframe, width=1000, height=100, font=myfont, bg=tbox_color)
input_text.pack(padx=5, pady=5)

# run the windows loop
root.mainloop()
