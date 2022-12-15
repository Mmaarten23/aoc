import re
from re import Match


def main():
    lines: list[str] = open("input/input15.txt").readlines()
    data: list[tuple[tuple[int, int], tuple[int, int]]] = [parse(line) for line in lines]
    line_nr: int = 2_000_000
    line: set[int] = fill_line(data, line_nr)
    line = remove_beacons(line, data, line_nr)
    max_index: int = 4_000_000
    for i in range(max_index, -1, -1):
        if i % 10 == 0:
            print(i)
        row: list[bool] = [False] * max_index
        row = fill_field(row, data)
        if False in row:
            print(i, row.index(False))
    print(f'Part 1: {len(line)}')
    # print(f'Part 2: {coordinate[0] * 4_000_000 + coordinate[1]}')


def parse(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    match: Match = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
    if not match:
        raise ValueError(f'Invalid line: {line}')
    groups: tuple = match.groups()
    return (int(groups[0]), int(groups[1])), (int(groups[2]), int(groups[3]))


def fill_line(data: list[tuple[tuple[int, int], tuple[int, int]]], line_nr: int) -> set[int]:
    busy_indices: set[int] = set()
    for line in data:
        distance: int = calculate_manhattan(line[0], line[1])
        start: int = line[0][0] - distance + abs(line[0][1] - line_nr)
        end: int = line[0][0] + distance + 1 - abs(line[0][1] - line_nr)
        busy_indices.update(range(start, end))
    return busy_indices


def calculate_manhattan(scanner: tuple[int, int], beacon: tuple[int, int]) -> int:
    return abs(scanner[0] - beacon[0]) + abs(scanner[1] - beacon[1])


def remove_beacons(line: set[int], data: list[tuple[tuple[int, int], tuple[int, int]]], line_nr: int) -> set[int]:
    for d in data:
        if not d[1][1] == line_nr:
            continue
        if d[1][0] in line:
            line.remove(d[1][0])
    return line


def fill_field(field: list[bool], data: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[bool]:
    for line in data:
        distance: int = calculate_manhattan(line[0], line[1])
        min_index: int = max(0, line[0][0] - distance)
        max_index: int = min(len(field), line[0][0] + distance)
        field[min_index:max_index + 1] = [True] * ((max_index + 1) - min_index)
    return field


if __name__ == '__main__':
    main()
