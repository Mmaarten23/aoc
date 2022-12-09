def main():
    lines: list[str] = open('input9.txt', 'r').readlines()
    commands: list[tuple[str, int]] = [(tokens[0], int(tokens[1])) for tokens in (line.split() for line in lines)]
    coord_t: list[tuple[int, int]] = [(0, 0) for _ in range(10)]
    result_1: set = set()
    result_2: set = set()
    for command, value in commands:
        for i in range(value):
            coord_t[0] = move_h(coord_t[0], command)
            for j in range(1, len(coord_t)):
                coord_t[j] = move_t(coord_t[j - 1], coord_t[j])
            result_1.add(coord_t[1])
            result_2.add(coord_t[-1])
    print(f'Part 1: {len(result_1)}')
    print(f'Part 2: {len(result_2)}')


def move_h(coord_h: tuple[int, int], command: str) -> tuple[int, int]:
    directions: dict[str, tuple[int, int]] = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0), }
    return coord_h[0] + directions[command][0], coord_h[1] + directions[command][1]


def move_t(coord_h: tuple[int, int], coord_t: tuple[int, int]) -> tuple[int, int]:
    x = coord_t[0]
    y = coord_t[1]
    dx, dy = coord_h[0] - x, coord_h[1] - y
    abs_x = abs(dx)
    abs_y = abs(dy)
    if abs_x == 2:
        x += 1 if dx > 0 else -1
        if abs_y == 1:
            y += dy
    if abs_y == 2:
        y += 1 if dy > 0 else -1
        if abs_x == 1:
            x += dx
    return x, y


if __name__ == '__main__':
    main()
