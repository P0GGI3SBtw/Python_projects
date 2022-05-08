from functions.game import *

app = Tk()
app.geometry('300x300')
app.title('Rock, paper, scissors')

user_label = Label(text='Entry Rock, Paper or Scissors:')
user_label.pack()
user_move = Entry(app, fg='blue')
user_move.pack()

button_ok = Button(app, text='OK', fg='green', command=lambda: game_rules(user_move.get()))
button_ok.pack()

app.mainloop()
