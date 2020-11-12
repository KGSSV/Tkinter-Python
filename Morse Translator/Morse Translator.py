import tkinter
import re
from tkinter import IntVar, END, DISABLED, NORMAL
from playsound import playsound
from PIL import Image, ImageTk
import pandas as pd
root = tkinter.Tk()

root.title('Morse Translator')
root.iconbitmap('morse.ico')
root.resizable(0, 0)
root.geometry('500x350')

# fonts and color
button_font = ('SimSun', 10)
root_color = '#95cab0'
frame_color = '#95c70f'

button_color = '4eacc1'

root.config(bg=root_color)


# define functions
def convert():
    if lang.get() == 1:
        getmorse()
    elif lang.get() == 2:
        geteng()


def getmorse():

    morse = ""
    text = input_text.get('1.0', END)
    text = text.lower()
    for letter in text:
        if letter not in eng_to_mor.keys():
            text = text.replace(letter, '')
    # break indivudual words
    # for example -  hello!are you   list output ['hello','how','' ....]  we dont wont that empty space so if space there remove it but only as an individual element
    wordlist = text.split(' ')
    for word in wordlist:
        letters = list(word)
        # for each letter get morse
        for letter in letters:
            char = eng_to_mor[letter]
            morse += char
            morse += " "
        # seperate words in morse
        morse += '|'
    df = pd.DataFrame([morse])
    df.to_clipboard(index=False, header=False)

    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)
    output_text.insert('1.0', morse)
    output_text.config(state=DISABLED)


def geteng():
    english = ''
    text = input_text.get(1.0, END)
    for letter in text:
        if letter not in mor_to_eng.keys():
            text = text.replace(letter, '')

    # break up each word based on '|'

    wordlist = text.split('|')
    print(wordlist)

    for word in wordlist:
        letters = word.split(' ')
        for letter in letters:
            char = mor_to_eng[letter]
            english += char
        english += " "

    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)
    output_text.insert('1.0', english)
    output_text.config(state=DISABLED)


def clear():
    input_text.delete(1.0, END)
    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)
    output_text.config(state=DISABLED)


def play():
    # play corressponding voice for dot and dash
    if lang.get() == 1:
        text = output_text.get(1.0, END)
    elif lang.get() == 2:
        text = input_text.get(1.0, END)

    # play tone( for . - " " |)
    for val in text:
        if val == ".":
            playsound('dot.mp3')
            root.after(100)  # to pause a loop 100 ms
        elif val == '-':
            playsound('dash.mp3')
            root.after(200)
        elif val == " ":
            root.after(300)
        elif val == "|":
            root.after(700)


def showguide():
    # image morse needs to be a global variable to put on new window
    global photo
    global guide

    guide = tkinter.Toplevel()
    guide.title('Morse Guide')
    guide.iconbitmap('morse.ico')
    guide.geometry('350x350+' + str(root.winfo_x()+550) +
                   "+" + str(root.winfo_y()))
    guide.config(bg=root_color)

    photo = ImageTk.PhotoImage(Image.open('morsechart.jpg'))
    label = tkinter.Label(guide, image=photo, bg=frame_color)
    label.pack(padx=10, pady=10, ipadx=5, ipady=5)

    closebutton = tkinter.Button(
        guide, text='Close', font=button_font, command=hide)
    closebutton.pack(padx=10, ipadx=20)

    # disable the guide
    guide_button.config(state=DISABLED)


def hide():
    guide_button.config(state=NORMAL)
    guide.destroy()


# create out morse code dict
eng_to_mor = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
              's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' ', '|': '|', '': ''}


mor_to_eng = dict([(value, key) for key, value in eng_to_mor.items()])

# define layout

# create frame
inputframe = tkinter.LabelFrame(root, bg=frame_color)
outputframe = tkinter.LabelFrame(root, bg=frame_color)
inputframe.pack(padx=16, pady=(16, 8))
outputframe.pack(padx=16, pady=(8, 16))

input_text = tkinter.Text(inputframe, height=8, width=30)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

lang = IntVar()
lang.set(1)
morse_button = tkinter.Radiobutton(
    inputframe, text='English --> Morse code', variable=lang, value=1, bg=frame_color, font=button_font)
eng_button = tkinter.Radiobutton(
    inputframe, text='Morse code --> English', variable=lang, value=2, bg=frame_color, font=button_font)
morse_button.grid(row=0, column=0, pady=(15, 0))
eng_button.grid(row=1, column=0)

guide_button = tkinter.Button(
    inputframe, text='Guide', font=button_font, command=showguide)
guide_button.grid(row=2, column=0, sticky='we', padx=10)

# output frame

output_text = tkinter.Text(outputframe, height=8, width=30)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)
output_text.config(state=DISABLED)

convent = tkinter.Button(outputframe, text='Convert',
                         font=button_font, command=convert)
play = tkinter.Button(outputframe, text='Play Morse',
                      font=button_font, command=play)
clear = tkinter.Button(outputframe, text='Clear',
                       font=button_font, command=clear)
quitb = tkinter.Button(outputframe, text='Quit',
                       font=button_font, command=root.destroy)


convent.grid(row=0, column=0, padx=10, sticky='we', ipadx=51)
play.grid(row=1, column=0, padx=10, sticky='we')
clear.grid(row=2, column=0, padx=10, sticky='we')
quitb.grid(row=3, column=0, padx=10, sticky='we')


# run the root window main loop
root.mainloop()
