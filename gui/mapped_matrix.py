from tkinter import *

import randomizer

values = randomizer.random_matrix("0123456789ABCEDF")
buttons = []

master = Tk()
master.grid()

for row in range(len(values)):
    temp = []
    for col in range(len(values)):
        temp.append(
            Button(text=values[row][col], width=10, height=5))
    buttons.append(temp)

for i in range(0, 4):
    for j in range(0, 4):
        buttons[i][j].grid(row=i, column=j)

master.mainloop()
