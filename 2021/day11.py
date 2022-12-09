def main():
    board = []
    f = open("input/input11.txt", "r")
    for line in f:
        board.append([int(a) for a in line.replace("\n", "")])
    f.close()
    count = 0
    for _ in range(0, 100):
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                board[row][col] += 1
        flashed = True
        while flashed:
            flashed = False
            for row in range(0, len(board)):
                for col in range(0, len(board[0])):
                    if board[row][col] > 9:
                        flash(row, col, board)
                        flashed = True
                        board[row][col] = -100
                        count += 1
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] < 0:
                    board[row][col] = 0
    print(count)


def main2():
    board = []
    f = open("input/input11.txt", "r")
    for line in f:
        board.append([int(a) for a in line.replace("\n", "")])
    f.close()
    i = 0
    while True:
        i += 1
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                board[row][col] += 1
        flashed = True
        while flashed:
            flashed = False
            for row in range(0, len(board)):
                for col in range(0, len(board[0])):
                    if board[row][col] > 9:
                        flash(row, col, board)
                        flashed = True
                        board[row][col] = -100
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] < 0:
                    board[row][col] = 0
        sync = True
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] != 0:
                    sync = False
        if sync:
            print(i)
            return


def flash(row, col, board):
    if row > 0:
        board[row - 1][col] += 1
    if row < len(board) - 1:
        board[row + 1][col] += 1
    if col > 0:
        board[row][col - 1] += 1
    if col < len(board[0]) - 1:
        board[row][col + 1] += 1
    if row > 0 and col > 0:
        board[row - 1][col - 1] += 1
    if row < len(board) - 1 and col > 0:
        board[row + 1][col - 1] += 1
    if row > 0 and col < len(board) - 1:
        board[row - 1][col + 1] += 1
    if row < len(board) - 1 and col < len(board[0]) - 1:
        board[row + 1][col + 1] += 1


if __name__ == '__main__':
    main()
    main2()
