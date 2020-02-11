from tkinter import *
from functools import partial


def printer(x, y):
    with open("sequence.txt", "a") as file:
        file.write("[{0},{1}],".format(str(x), str(y)))


values = [['C', 'D', 'E', 'F'], ['8', '9', 'A', 'B'], ['4', '5', '6', '7'], ['0', '1', '2', '3']]
buttons = []

master = Tk()
master.grid()

for row in range(len(values)):
    temp = []
    for col in range(len(values)):
        temp.append(
            Button(text=values[row][col], width=10, height=5, command=partial(printer, row, col)))
    buttons.append(temp)

for i in range(0, 4):
    for j in range(0, 4):
        buttons[i][j].grid(row=i, column=j)

master.mainloop()
