def main():
    text: list[str] = open('input/input12.txt', 'r').readlines()
    parse: list[list[str]] = [[char for char in line.strip()] for line in text]
    values: list[list[int]] = [[-1 for _ in range(len(parse[0]))] for _ in range(len(parse))]
    start_row, start_col = find(parse, 'S')
    end_row, end_col = find(parse, 'E')
    values[start_row][start_col] = 0
    changed: bool = True
    while changed:
        changed = False
        for row in range(len(values)):
            for col in range(len(values[0])):
                if calculate(values, parse, row, col):
                    changed = True
    print(f'Part 2: {values[end_row][end_col]}')


def calculate(values, parse, row, col):
    # part 2
    if parse[row][col] == 'a':
        values[row][col] = 0
        return False
    # part 2
    up: int = get_value(row, col, -1, 0, parse, values) if row > 0 else -1
    down: int = get_value(row, col, 1, 0, parse, values) if row < len(values) - 1 else -1
    left: int = get_value(row, col, 0, -1, parse, values) if col > 0 else -1
    right: int = get_value(row, col, 0, 1, parse, values) if col < len(values[0]) - 1 else -1
    minimums: list[int] = [x for x in [up, down, left, right] if x != -1]
    if len(minimums) == 0:
        return False
    step: int = min(minimums) + 1
    if values[row][col] == -1 or step < values[row][col]:
        values[row][col] = step
        return True
    return False


def get_value(row, col, drow, dcol, parse, values):
    char: str = parse[row][col]
    if values[row + drow][col + dcol] == -1:
        return -1
    if not is_succeeding_letter(char, parse[row + drow][col + dcol]):
        return -1
    return values[row + drow][col + dcol]


def is_succeeding_letter(char: str, previous_char: str) -> bool:
    alphabet: str = 'SabcdefghijklmnopqrstuvwxyzE'

    return alphabet.index(previous_char) + 1 >= alphabet.index(char)


def find(matrix: list[list[str]], letter: str) -> tuple[int, int]:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == letter:
                return i, j


if __name__ == '__main__':
    main()
