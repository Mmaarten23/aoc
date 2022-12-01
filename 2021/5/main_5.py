def main():
    board = [[0 for col in range(1000)] for row in range(1000)]
    f = open("input.txt", "r")
    for line in f:
        coordinates = line.replace("\n", "").split(" -> ")
        x_1, y_1 = [int(a) for a in coordinates[0].split(",")]
        x_2, y_2 = [int(a) for a in coordinates[1].split(",")]
        max_x = max(x_1, x_2)
        min_x = min(x_1, x_2)
        max_y = max(y_1, y_2)
        min_y = min(y_1, y_2)

        if min_x == max_x or min_y == max_y:
            for j in range(min_x, max_x + 1):
                for i in range(min_y, max_y + 1):
                    board[i][j] = board[i][j] + 1
        else:
            if x_1 < x_2:
                x_pos = [a for a in range(x_1, x_2 + 1)]
            else:
                x_pos = [a for a in range(x_1, x_2 - 1, -1)]
            if y_1 < y_2:
                y_pos = [a for a in range(y_1, y_2 + 1)]
            else:
                y_pos = [a for a in range(y_1, y_2 - 1, -1)]
            for i in range(max_x - min_x + 1):
                board[y_pos[i]][x_pos[i]] = board[y_pos[i]][x_pos[i]] + 1

    f.close()
    count = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] > 1:
                count += 1
    print(board)
    print(count)


if __name__ == '__main__':
    main()
