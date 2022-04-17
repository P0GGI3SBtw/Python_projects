from tkinter import *
from functions.operators import show

root = Tk()
root.geometry('300x160')
root.title('Calculator')

integer1 = Entry(root, fg='blue')
integer1.grid(row=1, column=1)

integer2 = Entry(root, fg='blue')
integer2.grid(row=2, column=1)

var = IntVar()

# Radio buttons + and -
R1 = Radiobutton(root, text='+', variable=var, value=1)
R1.grid(row=1, column=3)
R2 = Radiobutton(root, text='-', variable=var, value=2)
R2.grid(row=2, column=3)
R2 = Radiobutton(root, text='*', variable=var, value=3)
R2.grid(row=3, column=3)
R2 = Radiobutton(root, text='/', variable=var, value=4)
R2.grid(row=4, column=3)

label_text = Label(root, text='Result of action: 0')
label_text.grid(row=5, column=1)

# Button 'OK'
button_ok = Button(root, text='OK', fg='green', command=lambda: show(var, integer1, integer2, label_text))
button_ok.grid(row=6, column=1)

root.mainloop()
