from tkinter import *
import solver
import copy
import time
import ending_page


# Function to create the game board
def run_game(difficulty):
    start_time = time.time() + 1
    error_time = 0
    error_ct = 0
    timer_callback = None

    def end_game(elapsed_time, err_ct):
        # stop the timer
        nonlocal timer_callback
        game.after_cancel(timer_callback)
        # start the end page
        ending_page.main(elapsed_time, err_ct)

    def validate_input(char, val):
        """
        validate_input checks whether the user can place a character in its selected entry

        :param char: the character to be validated
        :param val: the current value inside the entry

        :return: true if the char is a number 1-9 and the value inside the entry is one character
        """
        return char.isdigit() and 1 <= int(char) <= 9 and len(val) <= 1

    def on_enter(event):
        """
        on_enter handles the Enter key press event. If the entered number can lead to a solution, mark the entry as read-only. Otherwise, indicate an incorrect attempt and adjust the timer

        :param event: The event object associated with the Enter key press
        """
        nonlocal error_time
        nonlocal error_ct
        entry = event.widget
        row, col = entry.row, entry.col

        # cache board if it needs to be reverted
        starter_board = copy.deepcopy(solver.board)

        num = int(entry.get())
        solver.board[row][col] = num
        starter_board[row][col] = num
        # print(solver.board)
        # bug: valid leads to solution but board still incomplete
        solvable = solver.validate() and solver.solve()
        # if it can lead to a solution set as read-only and tell user it's right
        if solvable:
            entry.config(state="readonly")
            solver.board = starter_board
            # board is complete go to next page
            if all(0 not in row for row in solver.board):
                end_game(int(time.time() - start_time + error_time), error_ct)
            return

        # if it can't add 15 secs on timer, undo insertion in solver.board, and tell user it's wrong
        else:
            solver.board = starter_board
            solver.board[row][col] = 0
            # solver.print_board(solver.board)
            error_time += 15
            error_ct += 1
            err_label.config(text=f"Mistake Count: {error_ct}")
            return

    def update_time():
        nonlocal timer_callback
        elapsed_time = int(time.time() - start_time + error_time)
        mins = elapsed_time // 60
        secs = elapsed_time % 60
        timer_label.config(text=f"Elapsed time: {mins:02d}:{secs:02d}")
        timer_callback = game.after(100, update_time)

    global game
    game = Tk()
    game.title("Sudoku Game")
    game.geometry("630x540")

    # Create a Frame to hold the Sudoku board
    board_frame = Frame(game, borderwidth=2, relief="solid")
    board_frame.pack(side="top", padx=10, pady=15)

    # solver.fetch(difficulty)
    solver.board = [
        [0, 5, 3, 6, 2, 1, 7, 4, 9],
        [9, 7, 4, 3, 5, 8, 6, 1, 2],
        [2, 6, 1, 7, 4, 9, 3, 5, 8],
        [4, 2, 5, 9, 8, 3, 1, 7, 6],
        [6, 3, 8, 4, 1, 7, 2, 9, 5],
        [1, 9, 7, 2, 6, 5, 8, 3, 4],
        [3, 8, 6, 5, 7, 4, 0, 2, 1],
        [7, 4, 2, 1, 9, 6, 5, 8, 3],
        [5, 1, 9, 8, 3, 2, 4, 6, 7],
    ]

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
                        width=2,
                        font=("Arial", 30),
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
                        entry.bind("<Return>", on_enter)
                        entry.row, entry.col = row, col

    # Create a Frame to hold the timer and the error label
    bottom_frame = Frame(game)
    bottom_frame.pack(side="bottom", fill="x")

    timer_label = Label(
        bottom_frame, text=f"Elapsed Time: 0 seconds", font=("Arial", 18)
    )
    timer_label.pack(side="right", padx=15, pady=15)
    err_label = Label(bottom_frame, text="Mistake Count: 0", font=("Arial", 18))
    err_label.pack(side="left", padx=15, pady=15)

    # Start the timer
    start_time = time.time()
    update_time()

    game.mainloop()
