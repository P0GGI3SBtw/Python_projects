# Function for main


def show(var, integer1, integer2, label_text):
    result = 0
    match var.get():
        case 1:
            result = int(integer1.get()) + int(integer2.get())
        case 2:
            result = int(integer1.get()) - int(integer2.get())
        case 3:
            result = int(integer1.get()) * int(integer2.get())
        case 4:
            if int(integer2.get()) == 0:
                result = "You can't divide by zero"
            else:
                result = float(integer1.get()) / float(integer2.get())
        case 5:
            result = int(integer1.get()) ** int(integer2.get())

    label_text.config(text=f'Result of action is {round(result, 2)}')
