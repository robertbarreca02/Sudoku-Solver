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


def main():
    # print_board(starter_board)
    # extract_boxes(starter_board)
    # print(boxes)
    extract_cols(starter_board)
    print(cols)


if __name__ == '__main__':
    main()
