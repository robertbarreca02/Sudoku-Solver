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


def test_is_possible(i, j, n, preset_board):
    """
    test_is_possible is a tester method that uses a custom board and instead of an api generated one and uses that board for the is_possible method

    :param i: the y coordinate of the sudoku board
    :param j: the x coordinate of the sudoku board
    :param n: the number that we're trying to insert
    :param preset_board: the board we are using to test

    :return: the value that is_possible returns
    """
    global board
    board = preset_board
    return is_possible(i, j, n)


def test_solve(preset_board):
    """
    test_solve is a tester method that uses a custom board instead of an api generated one and uses that board for the solve method

    :param preset_board: the board we are using to test

    :return: the solved version of preset board
    """
    global board
    board = preset_board
    solve()
    return board


def solve():
    """
    solve is a recursive function that solves the sudoku board by filling in all the zero slots of the board

    :return: true if we can put a number in the first empty slot found or the board is filled and return false otherwise
    """

    # base case board is filled
    if 0 not in board:
        return True

    # recursive case: board still needs to be filled
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_possible(i, j, num):
                        board[i][j] = num
                        if solve():
                            return True
                        board[i][j] = 0
                return False


def main():
    global board
    # fetch from api(only generates one solution 9x9 sudoku boards)
    url = "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}"
    req = requests.get(url)
    response = req.json()
    board = np.array(response.get("newboard").get("grids")[0].get("value"))
    print("Original Board:")
    print_board(board)
    solve()
    input("Press enter when ready to see the solution\n")
    print("Solved Board:")
    print_board(board)


if __name__ == "__main__":
    main()
