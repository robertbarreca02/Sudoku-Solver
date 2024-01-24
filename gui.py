from tkinter import *
import solver


def validate_input(char, val):
    return char.isdigit() and 1 <= int(char) <= 9 and len(val) <= 1


def on_enter(row, col, entry):
    num = entry.get()
    solver.print_board(solver.board)
    solver.board[row][col] = int(num) if num.isdigit() else ""
    solver.print_board(solver.board)

    # if it can lead to a solution set as read only
    if solver.solve() and solver.validate:
        entry.config(state="readonly")
    # if it can't add 15 secs on timer and undo insertion into solver.board


root = Tk()
root.title("Sudoku Game")
root.geometry("450x350")

# Create a Frame to hold the Sudoku board
board_frame = Frame(root, borderwidth=2, relief="solid")
board_frame.pack(side="top", padx=10, pady=10)

solver.fetch()

# Create a 9x9 grid of Entry widgets inside 3x3 boxes
for i in range(3):
    for j in range(3):
        box_frame = Frame(board_frame, borderwidth=1, relief="solid")
        box_frame.grid(row=i, column=j, padx=1, pady=1)

        for m in range(3):
            for n in range(3):
                # do conversion for rows and cols
                row = i * 3 + m
                col = j * 3 + n
                # get val from starter board
                val = solver.board[row][col]
                entry = Entry(
                    box_frame,
                    width=4,
                    font=("Arial", 14),
                    justify="center",
                    validate="key",
                )
                entry.grid(row=m, column=n, padx=1, pady=1)
                if val != 0:
                    entry.insert(0, val)
                    entry.config(state="readonly")
                else:
                    entry.config(
                        validatecommand=(entry.register(validate_input), "%S", "%P")
                    )
                    entry.bind(
                        "<Return>",
                        lambda event, row=row, col=col, entry=entry: on_enter(
                            row, col, entry
                        ),
                    )

root.mainloop()
