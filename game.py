from tkinter import *
import solver
import copy
import time
import threading


# Function to create the game board
def start_game(difficulty):
    start_time = time.time() + 1
    error_time = 0

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
        entry = event.widget
        row, col = entry.row, entry.col

        # cache board if it needs to be reverted
        starter_board = copy.deepcopy(solver.board)

        num = int(entry.get())
        solver.board[row][col] = num
        starter_board[row][col] = num
        # solver.print_board(solver.board)
        print("check 0")
        solvable = threading.Thread(target=solver.solve).start()
        # solvable = solver.solve()  # and solver.validate()
        print("check 1")
        time.sleep(0.1)  # Adjust as needed

        # if it can lead to a solution set as read-only and tell user it's right
        if solvable:
            entry.config(state="readonly")
            solver.board = starter_board
            solver.print_board(starter_board)
            return

        # if it can't add 15 secs on timer, undo insertion in solver.board, and tell user it's wrong
        else:
            solver.board = starter_board
            solver.board[row][col] = 0
            solver.print_board(solver.board)
            error_time += 15
            err_label.pack(pady=20)
            return

    def update_time():
        elapsed_time = time.time() - start_time + error_time
        timer_label.config(text=f"Elapsed time: {elapsed_time:.0f} seconds")
        game.after(100, update_time)

    game = Tk()
    game.title("Sudoku Game")
    game.geometry("450x350")

    # Create a Frame to hold the Sudoku board
    board_frame = Frame(game, borderwidth=2, relief="solid")
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
                        entry.bind("<Return>", on_enter)
                        entry.row, entry.col = row, col

    start_time = time.time()
    timer_label = Label(game, text=f"Elapsed Time: 0 seconds", font=("Arial", 12))
    timer_label.pack(side="bottom", anchor="se", padx=10, pady=10)
    update_time()
    err_label = Label(
        game,
        text="X",
        font=("Arial", 16),
    )

    game.mainloop()

    """
    TODO:
        finish on_enter
            add time to timer when incorrect guess
            add red x when incorrect guess
        Add notation for minutes
        fetch easy med or hard board based on user selection
        Add ending page when user solves board
    """
