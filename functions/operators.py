# Function for main


def show(var, integer1, integer2, label_text):
    result = 0
    if var.get() == 1:
        result = int(integer1.get()) + int(integer2.get())
    elif var.get() == 2:
        result = int(integer1.get()) - int(integer2.get())
    elif var.get() == 3:
        result = int(integer1.get()) * int(integer2.get())
    elif var.get() == 4:
        if int(integer2.get()) == 0:
            result = "You can't divide by zero"
        else:
            result = float(integer1.get()) / float(integer2.get())

    label_text.config(text=f'Result of action is {result}')
