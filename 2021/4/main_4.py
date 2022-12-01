def main1():
    f = open("input.txt", "r")
    lines = f.readlines()
    nrs = [int(a) for a in lines[0].split(",")]

    i = 2
    boards = []
    while i + 6 < len(lines):
        board = []
        for j in range(0, 5):
            board.append([int(lines[i + j][k:k + 2]) for k in range(0, len(lines[i + j]), 3)])
        boards.append(board)
        i += 6
    f.close()
    k = 0
    while anyWon(boards, nrs[k - 1]) == -1:
        for board in boards:
            for i in range(0, len(board)):
                for j in range(0, len(board)):
                    if board[i][j] == nrs[k]:
                        board[i][j] = -1
        k += 1


def calculateScore(board):
    score = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] != -1:
                score += board[i][j]
    return score


def anyWon(boards, k):
    for x in boards:
        if hasWon(x):
            score = calculateScore(x)
            print(score * k)
            return score
    return -1


def hasWon(board):
    for row in board:
        if sum(row) == -5:
            return True
    if any(x == -5 for x in map(sum, zip(*board))):
        return True

    return False


def main2():
    f = open("input.txt", "r")
    lines = f.readlines()
    nrs = [int(a) for a in lines[0].split(",")]

    i = 2
    boards = []
    while i + 6 < len(lines):
        board = []
        for j in range(0, 5):
            board.append([int(lines[i + j][k:k + 2]) for k in range(0, len(lines[i + j]), 3)])
        boards.append(board)
        i += 6
    f.close()
    k = 0
    while len(boards) > 1 or not hasWon(boards[0]):
        toRemove = []
        if nrs[k] == 16:
            print("test")
        for board in boards:
            for i in range(0, len(board)):
                for j in range(0, len(board)):
                    if board[i][j] == nrs[k]:
                        board[i][j] = -1
            if len(boards) > 1 and hasWon(board):
                toRemove.append(board)
        for board in toRemove:
            boards.remove(board)
        k += 1
    print(calculateScore(boards[0]) * nrs[k - 1])


if __name__ == '__main__':
    main1()
    main2()
