def main():
    with open('input/day3.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))


def part1(lines: list[str]):
    som: int = 0
    for row in range(len(lines)):
        line: str = lines[row]
        current_number: str = ''
        for char in range(len(line)):
            if not line[char].isdigit():
                continue
            current_number += line[char]
            if char != len(line) - 1 and line[char + 1].isdigit():
                continue
            found: bool = check_for_symbol(char + 1 - len(current_number), char + 1, lines, row)
            if found:
                som += int(current_number)
            current_number = ''
    return som


def check_for_symbol(start_of_number: int, end_of_number: int, lines: list[str], row: int) -> bool:
    for i in range(-1, 2):  # Row above, one below
        if row + i >= len(lines) or row + i < 0:
            continue
        for j in range(max(start_of_number - 1, 0), min(end_of_number + 1, len(lines[row + i]))):
            if lines[row + i][j].isdigit():
                continue
            if lines[row + i][j] != '.':
                return True
    return False


def part2(lines: list[str]):
    dictionary: dict[tuple[int, int], list[int]] = {}
    for row in range(len(lines)):
        line: str = lines[row]
        current_number: str = ''
        for char in range(len(line)):
            if not line[char].isdigit():
                continue
            current_number += line[char]
            if char != len(line) - 1 and line[char + 1].isdigit():
                continue
            start: int = char + 1 - len(current_number)
            end: int = char + 1
            j: list[tuple[int, int]] = check_for_symbol_specific(start, end, lines, row, '*')
            for i in j:
                if i:
                    if i in dictionary:
                        dictionary[i][0] *= int(current_number)
                        dictionary[i][1] += 1
                    else:
                        dictionary[i] = [int(current_number), 1]
            current_number = ''
    return sum([x[0] for x in dictionary.values() if x[1] == 2])


def check_for_symbol_specific(start_of_number, end_of_number, lines, row, symbol):
    applicable = []
    for i in range(-1, 2):  # Row above, one below
        if row + i >= len(lines) or row + i < 0:
            continue
        for j in range(max(start_of_number - 1, 0), min(end_of_number + 1, len(lines[row + i]))):
            if lines[row + i][j].isdigit():
                continue
            if lines[row + i][j] == '*':
                applicable.append((row + i, j))
    return applicable


if __name__ == '__main__':
    main()
