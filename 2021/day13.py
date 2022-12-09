def main():
    board = [[1 for _ in range(1311)] for _ in range(892)]
    folds = []
    f = open("input/input13.txt", "r")
    maxx = 0
    maxy = 0
    for line in f:
        if line.__contains__(","):
            (y, x) = line.replace("\n", "").split(",")
            maxx = max(maxx, int(x))
            maxy = max(maxy, int(y))
            board[int(x)][int(y)] = 0
        elif line.__contains__("fold along "):
            folds.append(tuple(line.replace("\n", "").replace("fold along ", "").split("=")))
    f.close()
    for fold in folds:
        board = applyFold(board, fold)
    for line in board:
        for char in line:
            print(" #", end="") if char == 0 else print("  ", end="")
        print()


def applyFold(board, fold):
    return applyHorizontalFold(board, int(fold[1])) if fold[0] == "y" else applyVerticalFold(board, int(fold[1]))


def applyHorizontalFold(board, nr):
    original = board[:nr]
    folded = board[nr + 1:]
    new_board = []
    end_i = min(len(original), len(folded))
    for i in range(0, end_i):
        a = original[-(i + 1)]
        b = folded[i]
        new_board.insert(0, [a[j] * b[j] for j in range(0, len(a))])
    if len(folded) > len(original):
        for i in range(end_i, len(folded)):
            new_board.insert(0, folded[i])
    else:
        for i in range(end_i, len(original)):
            new_board.insert(0, original[-(i + 1)])
    return new_board


def applyVerticalFold(board, nr):
    return transpose(applyHorizontalFold(transpose(board), nr))


def transpose(board):
    result = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            result[j][i] = board[i][j]
    return result


if __name__ == '__main__':
    main()
