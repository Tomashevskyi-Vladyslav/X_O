from tkinter import *
from random import *
import time

table = [0, 0, 0,   0, 0, 0,    0, 0, 0]
buttons = []
player = randint(0, 1)

# ======================================
def start(event):
    global table, buttons, player
    player = randint(0, 1)
    table = [0, 0, 0,    0, 0, 0,   0, 0, 0]
    for b in buttons: b.config(text=' ', state=NORMAL)


def move(index):
    global table, player
    if player == 1:
        buttons[index].config(text='X', state=DISABLED)
        table[index] = 'X'
        player = 0
    else:
        buttons[index].config(text='O', state=DISABLED)
        table[index] = 'O'
        player = 1
    for i in ['X', 'O']:
        check_win(0, 1, 2, i)
        check_win(3, 4, 5, i)
        check_win(6, 7, 8, i)
        check_win(0, 3, 6, i)
        check_win(1, 4, 7, i)
        check_win(2, 5, 8, i)
        check_win(0, 4, 8, i)
        check_win(2, 4, 6, i)
def check_win(one, two, three, sign):
    global buttons,player

    if table[one] == table[two] == table[three] == sign:
        for b in buttons: b.config(state=DISABLED)
        buttons[one].config(text='WIN')
        buttons[two].config(text='WIN')
        buttons[three].config(text='WIN')

        with open ('New Text Document.txt', 'a') as file: 
            if player==0:
                file.write(f"\nplayer whis sgin X win {time.strftime('%X %x')} combination : {one, two, three}")

            else :
                file.write(f"\nplayer whis sgin O win {time.strftime('%X %x')} combination : {one, two, three}")

# ======================================
root = Tk()
root.title('XO')
root.geometry('350x350')

# ======================================
btn1 = Button(bg='darkgray', command=lambda:move(0))
btn1.place(relx=0, rely=0, relwidth=0.333, relheight=0.333)

btn2 = Button(bg='gray', command=lambda:move(1))
btn2.place(relx=0.333, rely=0, relwidth=0.333, relheight=0.333)

btn3 = Button(bg='darkgray', command=lambda:move(2))
btn3.place(relx=0.666, rely=0, relwidth=0.333, relheight=0.333)

# ======================================
btn4 = Button(bg='gray', command=lambda:move(3))
btn4.place(relx=0, rely=0.333, relwidth=0.333, relheight=0.333)

btn5 = Button(bg='darkgray', command=lambda:move(4))
btn5.place(relx=0.333, rely=0.333, relwidth=0.333, relheight=0.333)

btn6 = Button(bg='gray', command=lambda:move(5))
btn6.place(relx=0.666, rely=0.333, relwidth=0.333, relheight=0.333)

# ======================================
btn7 = Button(bg='darkgray', command=lambda:move(6))
btn7.place(relx=0, rely=0.666, relwidth=0.333, relheight=0.333)

btn8 = Button(bg='gray', command=lambda:move(7))
btn8.place(relx=0.333, rely=0.666, relwidth=0.333, relheight=0.333)

btn9 = Button(bg='darkgray', command=lambda:move(8))
btn9.place(relx=0.666, rely=0.666, relwidth=0.333, relheight=0.333)

# ======================================
buttons.extend([btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9])
for b in buttons:
    b.config(activebackground='orange', font=('Consolas', 35))

root.bind('<Return>', start)
root.mainloop()

