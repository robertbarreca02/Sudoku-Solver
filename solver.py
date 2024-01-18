import numpy as np
board = np.array([
    [0, 0, 6, 3, 9, 0, 8, 0, 1],
    [0, 8, 9, 0, 7, 0, 5, 3, 0],
    [3, 5, 0, 8, 0, 0, 9, 6, 0],
    [0, 0, 0, 6, 0, 8, 0, 2, 3],
    [8, 0, 1, 0, 3, 4, 0, 0, 0],
    [4, 0, 3, 0, 0, 0, 6, 0, 8],
    [6, 0, 0, 0, 0, 9, 3, 8, 0],
    [0, 3, 0, 7, 8, 2, 0, 9, 0],
    [0, 7, 0, 0, 0, 3, 0, 0, 0]])


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def is_possible(i, j, n):
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
    print_board(board)
    print("\n")
    solve()
    print_board(board)


if __name__ == '__main__':
    main()
