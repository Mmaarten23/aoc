def part1(values: list[list[int]]):
    s: int = 0
    for time_series in values:
        current_differences: list[int] = time_series.copy()
        last_elements: list[int] = []
        while len(set(current_differences)) != 1 or 0 not in current_differences:
            last_elements.append(current_differences[-1])
            current_differences = [current_differences[i + 1] - current_differences[i] for i in
                                   range(len(current_differences) - 1)]
        current_difference: int = 0
        for i in range(len(last_elements) - 1, -1, -1):
            current_difference += last_elements[i]
        s += current_difference
    return s


def part2(values: list[list[int]]):
    s: int = 0
    for time_series in values:
        current_differences: list[int] = time_series.copy()
        first_elements: list[int] = []
        while len(set(current_differences)) != 1 or 0 not in current_differences:
            first_elements.append(current_differences[0])
            current_differences = [current_differences[i + 1] - current_differences[i] for i in
                                   range(len(current_differences) - 1)]
        current_difference: int = 0
        for i in range(len(first_elements) - 1, -1, -1):
            current_difference -= first_elements[i]
            current_difference *= -1
        s += current_difference
    return s


def main():
    with open('input/day9.txt') as f:
        lines: list[str] = f.readlines()
    values: list[list[int]] = [[int(val) for val in line.split()] for line in lines]
    print(part1(values))
    print(part2(values))


if __name__ == '__main__':
    main()
