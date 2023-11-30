from tkinter import *
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

 
root = Tk()
root.iconbitmap("")
root.geometry("240x470")

# this greyed-out the maximize button
# root.resizable(0,0)

frame = Frame(root)
frame.pack()
 
leftframe = Frame(root)
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
 
label = Label(frame, text = "Unicorn Log Analyzer Tool")
label.pack()

e1 = Button(text='\U0001F4A9', font=("", 50)).pack(padx = 3, pady = 3)

e2 = Button(text='\U0001F4A6', font=("", 50)).pack(padx = 3, pady = 3)

e2 = Button(text='\U0001F4A8', font=("", 50)).pack(padx = 3, pady = 3)


# button0 = Button(leftframe, text = "Unicorn PeePee")
# button0.pack(padx = 3, pady = 3) 
# button1 = Button(leftframe, text = "IPG Log")
# button1.pack(padx = 3, pady = 3)
# button2 = Button(leftframe, text = "Charger Log")
# button2.pack(padx = 3, pady = 3)
# button3 = Button(leftframe, text = "CP Log")
# button3.pack(padx = 3, pady = 3)
# button4 = Button(leftframe, text = "PC Log")
# button4.pack(padx = 3, pady = 3)
# button5 = Button(leftframe, text = "Unicorn Poopoo")
# button5.pack(padx = 3, pady = 3) 

entry = Entry(frame, width= 30)
entry.insert(INSERT, "What should your unicorn make?")
entry.pack(padx = 3, pady = 3)

# ico = Image.open("")
# photo = ImageTk.PhotoImage(ico)
# root.wm_iconphoto(False, photo)

image1 = resource_path("ico/unicorn_1f984.png")
photo = PhotoImage(file = image1)
root.wm_iconphoto(False, photo)

root.title("Unicorn Tools")
root.mainloop()