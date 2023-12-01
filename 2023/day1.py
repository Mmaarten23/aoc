numbers: dict[str, int] = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def main():
    with open('input/day1.txt', 'r') as file:
        lines: list[str] = file.readlines()
    # part1(lines)
    part2(lines)


def part1(lines):
    sums: int = 0
    for line in lines:
        first_number: str = find_first_number_1(line)
        last_number: str = find_first_number_1(line[::-1])
        sums += int(first_number + last_number)
    print(sums)


def part2(lines):
    sums: int = 0
    for line in lines:
        first_number: str = find_first_number_2(line)
        last_number: str = find_first_number_2(line, True)
        sums += int(first_number + last_number)
    print(sums)


def find_first_number_1(line):
    for i in line:
        if i.isdigit():
            return i


def find_first_number_2(line, backwards=False):
    r = range(len(line)) if not backwards else range(len(line) - 1, -1, -1)
    for i in r:
        if line[i].isdigit():
            return line[i]
        for j in numbers:
            if line[i:i + len(j)] == j:
                return str(numbers[j])


if __name__ == '__main__':
    main()
