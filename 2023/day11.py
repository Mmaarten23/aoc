def expand_rows(sky_map: list[list[str]]) -> list[list[str]]:
    new_galaxies: list[list[str]] = []
    for row in sky_map:
        new_galaxies.append(row)
        if '#' not in row:
            new_galaxies.append(['x' for _ in range(len(row))])
    return new_galaxies


def expand_rows_2(sky_map: list[list[str]]) -> list[list[str]]:
    new_galaxies: list[list[str]] = []
    for row in sky_map:
        if '#' not in row:
            new_galaxies.append(['x' for _ in range(len(row))])
        else:
            new_galaxies.append(row)
    return new_galaxies


def transpose(sky_map: list[list[str]]) -> list[list[str]]:
    new_galaxies: list[list[str]] = []
    for i in range(len(sky_map[0])):
        new_galaxies.append([row[i] for row in sky_map])
    return new_galaxies


def part1(sky_map: list[list[str]]) -> int:
    sky_map = expand_rows(sky_map)
    sky_map = transpose(sky_map)
    sky_map = expand_rows(sky_map)
    sky_map = transpose(sky_map)
    galaxies: list[tuple[int, int]] = []
    for i in range(len(sky_map)):
        for j in range(len(sky_map[0])):
            if sky_map[i][j] == '#':
                galaxies.append((i, j))
    s: int = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distance: int = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            s += distance
    return s


def calculate_distance(sky_map, param, param1):
    start_x: int = min(param[0], param1[0])
    end_x: int = max(param[0], param1[0])
    start_y: int = min(param[1], param1[1])
    end_y: int = max(param[1], param1[1])
    distance: int = 0
    for i in range(start_x, end_x + 1):
        current_char: str = sky_map[i][start_y]
        if current_char == 'x':
            distance += 1_000_000
        else:
            distance += 1
    for j in range(start_y, end_y + 1):
        current_char: str = sky_map[end_x][j]
        if current_char == 'x':
            distance += 1_000_000
        else:
            distance += 1
    return distance - 2



def part2(sky_map: list[list[str]]) -> int:
    sky_map = expand_rows_2(sky_map)
    sky_map = transpose(sky_map)
    sky_map = expand_rows_2(sky_map)
    sky_map = transpose(sky_map)
    galaxies: list[tuple[int, int]] = []
    for i in range(len(sky_map)):
        for j in range(len(sky_map[0])):
            if sky_map[i][j] == '#':
                galaxies.append((i, j))
    s: int = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distance: int = calculate_distance(sky_map, galaxies[i], galaxies[j])
            s += distance
    return s


def main():
    with open('input/day11.txt') as f:
        lines: list[str] = f.readlines()
    sky_map: list[list[str]] = [[x for x in line.strip()] for line in lines]
    print(part1(sky_map))
    print(part2(sky_map))


if __name__ == '__main__':
    main()
