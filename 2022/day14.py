DEBUG: bool = False
vp: tuple[tuple[int, int], tuple[int, int]] = ((300, 700), (0, 161)) if not DEBUG else ((485, 520), (0, 15))


def main():
    lines: list[str] = open("input/input14.txt").readlines()

    field: list[list[str]] = [[' ' for _ in range(vp[0][0], vp[0][1])] for _ in range(vp[1][0], vp[1][1])]
    for line in lines:
        fill_field(field, line)
    field_2: list[list[str]] = [row.copy() for row in field]
    fill_bottom(field_2)
    print(f'Part 1: {simulate(field)}')
    print(f'Part 2: {simulate_2(field_2)}')


def fill_field(field: list[list[str]], line: str) -> None:
    parsed: list[tuple[int, int]] = parse_line(line)
    for i in range(1, len(parsed)):
        start: tuple[int, int] = parsed[i - 1]
        end: tuple[int, int] = parsed[i]
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                field[y][x] = '#'


def parse_line(line: str) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    tokens: list[str] = line.split(' -> ')
    for token in tokens:
        x: int = int(token.split(',')[0].strip()) - vp[0][0]
        y: int = int(token.split(',')[1].strip()) - vp[1][0]
        result.append((x, y))
    return result


def simulate(field: list[list[str]]) -> int:
    resting: int = 0
    start: tuple[int, int] = (500 - vp[0][0], 0)
    current_sand: tuple[int, int] = start
    while True:
        new_pos: tuple[int, int] = update_sand(field, current_sand)
        if new_pos[1] == vp[1][1] - 1:
            break
        elif new_pos == current_sand:
            resting += 1
            current_sand = start
        else:
            current_sand = new_pos
    return resting


def update_sand(field: list[list[str]], current_sand: tuple[int, int]) -> tuple[int, int]:
    if field[current_sand[1] + 1][current_sand[0]] == ' ':
        field[current_sand[1] + 1][current_sand[0]] = '°'
        field[current_sand[1]][current_sand[0]] = ' '
        return current_sand[0], current_sand[1] + 1
    elif field[current_sand[1] + 1][current_sand[0] - 1] == ' ':
        field[current_sand[1] + 1][current_sand[0] - 1] = '°'
        field[current_sand[1]][current_sand[0]] = ' '
        return current_sand[0] - 1, current_sand[1] + 1
    elif field[current_sand[1] + 1][current_sand[0] + 1] == ' ':
        field[current_sand[1] + 1][current_sand[0] + 1] = '°'
        field[current_sand[1]][current_sand[0]] = ' '
        return current_sand[0] + 1, current_sand[1] + 1
    else:
        field[current_sand[1]][current_sand[0]] = 'o'
        return current_sand


def fill_bottom(field_2: list[list[str]]) -> None:
    lowest_y: int = len(field_2) - 1
    for y in range(lowest_y, -1, -1):
        if field_2[y].__contains__('#'):
            lowest_y = y
            break
    field_2[lowest_y + 2] = ['~' for _ in range(len(field_2[lowest_y + 2]))]


def simulate_2(field: list[list[str]]) -> int:
    resting: int = 0
    start: tuple[int, int] = (500 - vp[0][0], 0)
    current_sand: tuple[int, int] = start
    while True:
        new_pos: tuple[int, int] = update_sand(field, current_sand)
        if new_pos == current_sand:
            resting += 1
            if new_pos == start:
                break
            current_sand = start
        else:
            current_sand = new_pos
    return resting


if __name__ == '__main__':
    main()
