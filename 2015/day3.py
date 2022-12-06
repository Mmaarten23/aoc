def main():
    text: str = open('input3.txt').read()
    part_1: int = 0
    part_2: int = 0
    coord: tuple[int, int] = (0, 0)
    coord_santa: tuple[int, int] = (0, 0)
    coord_robot: tuple[int, int] = (0, 0)
    coords: list[tuple[int, int]] = [coord]
    coords_santa: list[tuple[int, int]] = [coord_santa]
    coords_robot: list[tuple[int, int]] = [coord_robot]
    for c in text:
        coord = get_new_coord(c, coord)
        coords.append(coord)
    for i in range(len(text)):
        if i % 2 == 0:
            coord_santa = get_new_coord(text[i], coord_santa)
            coords_santa.append(coord_santa)
        else:
            coord_robot = get_new_coord(text[i], coord_robot)
            coords_robot.append(coord_robot)
    print(f'Part 1: {len(set(coords))}')
    print(f'Part 2: {len(set(coords_santa + coords_robot))}')


def get_new_coord(c: str, coord: tuple[int, int]) -> tuple[int, int]:
    if c == '^':
        coord = (coord[0], coord[1] + 1)
    elif c == 'v':
        coord = (coord[0], coord[1] - 1)
    elif c == '>':
        coord = (coord[0] + 1, coord[1])
    elif c == '<':
        coord = (coord[0] - 1, coord[1])
    return coord


if __name__ == '__main__':
    main()
