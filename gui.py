from tkinter import *

root = Tk()
root.title("Sudoku Game")
root.geometry("450x350")

# Create a Frame to hold the Sudoku board
board_frame = Frame(root, borderwidth=2, relief="solid")
board_frame.pack(side="top", padx=10, pady=10)

# Create a 9x9 grid of Entry widgets inside 3x3 boxes
for i in range(3):
    for j in range(3):
        box_frame = Frame(board_frame, borderwidth=1, relief="solid")
        box_frame.grid(row=i, column=j, padx=1, pady=1)

        for m in range(3):
            for n in range(3):
                entry = Entry(box_frame, width=4, font=("Arial", 14), justify="center")
                entry.grid(row=m, column=n, padx=1, pady=1)

root.mainloop()
