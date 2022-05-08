import random
from tkinter import *


def game_rules(user_move):
    lst_move = ['Rock', 'Paper', 'Scissors']

    computer_move = random.choice(lst_move)
    computer_label = Label(text='Computer move:')
    computer_label.pack()
    computer_choice = Label(text='{}'.format(computer_move))
    computer_choice.pack()

    result_label = Label(text='Place for result')
    result_label.pack()

    if user_move == 'Rock' or user_move == 'Paper' or user_move == 'Scissors':
        if user_move == computer_move:
            result_label.config(text='Draw')

        elif user_move == 'Paper' and computer_move == 'Rock':
            result_label.config(text='User win this tour')

        elif user_move == 'Rock' and computer_move == 'Scissors':
            result_label.config(text='User win this tour')

        elif user_move == 'Scissors' and computer_move == 'Paper':
            result_label.config(text='User win this tour')

        else:
            result_label.config(text='Computer win this tour')

    else:
        result_label.config(text='Wrong user input!')
