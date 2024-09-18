import numpy as np
import requests


def print_board(board):
    """
    print_board takes in a sudoku board and prints it in sudoku format

    :param board: the sudoku board (9x9 2d array) to be printed
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()
    print()


def is_possible(i, j, n):
    """
    is_possible takes in an coordinate of the sudoku board and a number and checks to see if the number can be inserted without breaking the rules

    :param i: the y coordinate of the sudoku board
    :param j: the x coordinate of the sudoku board
    :param n: the number that we're trying to insert

    :return: true if we can insert n legally and false otherwise
    """
    # check if num is in row
    if n in board[i]:
        return False
    # check if num is in col
    if n in board[:, j]:
        return False
    # check if num is in box
    x = (j // 3) * 3
    y = (i // 3) * 3
    for y0 in range(y, y + 3):
        for x0 in range(x, x + 3):
            if board[y0][x0] == n:
                return False
    return True


def solve():
    """
    solve is a recursive function that solves the sudoku board by filling in all the zero slots of the board

    :return: true if we can put a number in the first empty slot found or the board is filled and return false otherwise
    """

    # base case board is filled
    if 0 not in board and validate():
        return True

    # recursive case: board still needs to be filled
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    # there is a valid num for the current slot
                    if is_possible(i, j, num):
                        board[i][j] = num
                        if solve():
                            return True
                        board[i][j] = 0
                # there is not a valid number for the current slot, must backtrack
                return False
    return False


def solve_iteratively(callback=None):
    """
    solve_iteratively is an iterative backtracking function that solves the Sudoku board.

    :param callback: Optional function to call for visualization updates.
    """
    stack = []

    # Find all empty cells on the board and push them onto the stack with initial values
    for i in range(8, -1, -1):
        for j in range(8, -1, -1):
            if board[i][j] == 0:
                stack.append((i, j, 1))

    while stack:
        i, j, num = stack.pop()

        # Try placing 'num' in position (i, j)
        while num <= 9:
            if is_possible(i, j, num):
                board[i][j] = num
                # Update the UI for visualization purposes
                if callback:
                    callback(i, j, num)

                # Check if the board is solved
                if 0 not in board and validate():
                    return True

                # Push the next empty cell onto the stack with the initial number
                for x in range(i, 9):
                    for y in range(j if x == i else 0, 9):
                        if board[x][y] == 0:
                            # Push the next number for current cell
                            stack.append((i, j, num + 1))
                            # Push the next empty cell
                            stack.append((x, y, 1))
                            break
                    else:
                        continue
                    break
                # Move on to the next cell
                break
            num += 1

        # Backtrack if no number is valid
        if num > 9:
            board[i][j] = 0
            if callback:
                callback(i, j, num)

    return False  # No solution


def validate():
    """
    validate is a function that takes checks to see if a given board follows all the rules of sudoku

    :return: true if the board follows all the rules and false otherwise
    """
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            # check rows
            if board[i][j] != 0 and board[i][j] in row_set:
                return False
            row_set.add(board[i][j])
            # check cols
            if board[j][i] != 0 and board[j][i] in col_set:
                return False
            col_set.add(board[j][i])

    # check boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box_set = set()
            for x in range(3):
                for y in range(3):
                    val = board[i + x][j + y]
                    if val != 0 and val in box_set:
                        return False
                    box_set.add(val)
    return True


def fetch(difficulty):
    """
    fetch is a function that fetches a playable sudoku board from the dosuku api and parses the json to set it as the global board
    """
    global board
    board_difficulty = ""
    # fetch from api until board is desired difficulty
    url = "https://sudoku-game-and-api.netlify.app/api/sudoku"
    req = requests.get(url)
    response = req.json()
    board = np.array(response.get(difficulty))


def main():
    """
    main handles user input, and calls the corresponding function to fetch Sudoku puzzles, solving them, and displaying the original and solved boards.

    """
    difficulty = None
    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        difficulty = (
            input('Please select a difficulty "easy", "medium" or "hard": ')
            .lower()
            .strip()
        )
    fetch(difficulty)
    print("Original Board:")
    print_board(board)
    solve()
    input("Press enter when ready to see the solution\n")
    print("Solved Board:")
    print_board(board)


if __name__ == "__main__":
    main()
