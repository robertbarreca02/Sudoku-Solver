starter_board = [
    [0, 0, 6, 3, 9, 0, 8, 0, 1],
    [0, 8, 9, 0, 7, 0, 5, 3, 0],
    [3, 5, 0, 8, 0, 0, 9, 6, 0],
    [0, 0, 0, 6, 0, 8, 0, 2, 3],
    [8, 0, 1, 0, 3, 4, 0, 0, 0],
    [4, 0, 3, 0, 0, 0, 6, 0, 8],
    [6, 0, 0, 0, 0, 9, 3, 8, 0],
    [0, 3, 0, 7, 8, 2, 0, 9, 0],
    [0, 7, 0, 0, 0, 3, 0, 0, 0]]

boxes = []
cols = []


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def extract_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            boxes.append(box)
    return boxes


def extract_cols(board):
    for j in range(9):
        col = [board[i][j] for i in range(9)]
        cols.append(col)
    return cols


def backtrack(sol_board, i, j):
    for x in range(i, -1, -1):
        for y in range(j, -1, -1):
            if (starter_board[x, y]) == 0:
                insert(sol_board, sol_board[x][y] + 1, x, y)


def insert(sol_board, starter_val, i, j):
    # find row element is in
    row = sol_board[i]
    # find col element is in
    col = cols[j]
    # find box element is in
    box = boxes[((i // 3) * 3) + (j // 3)]
    for z in range(9):
        if (z not in row) and (z not in col) and (z not in box):
            sol_board[i][j] = z
            return
    # can't insert any number must backtrack
    backtrack(sol_board, i, j)
    return sol_board


def solve():
    sol_board = starter_board
    for i in range(9):
        for j in range(9):
            # if num is there move to next element
            if starter_board[i][j] != 0:
                continue
            sol_board = insert(sol_board, 1, i, j)


def main():
    extract_boxes(starter_board)
    extract_cols(starter_board)
    solve()


if __name__ == '__main__':
    main()
