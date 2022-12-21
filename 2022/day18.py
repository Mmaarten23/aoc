def main():
    lines: list[str] = open("input/input18.txt").readlines()
    droplets: list[tuple[int, int, int]] = parse(lines)
    total_surface_area: int = 0
    for droplet in droplets:
        total_surface_area += amount_of_exposed_sides(droplet, droplets)

    air: list[tuple[int, int, int]] = generate_air(22, droplets)
    exterior_surface_area: int = 0
    for droplet in droplets:
        exterior_surface_area += amount_of_exterior_exposed_sides(air, droplet)
    print(f'Part 1: {total_surface_area}')
    print(f'Part 2: {exterior_surface_area}')


def parse(lines: list[str]) -> list[tuple[int, int, int]]:
    droplets: list[tuple[int, int, int]] = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        droplets.append((x, y, z))
    return droplets


def amount_of_exposed_sides(droplet: tuple[int, int, int], droplets: list[tuple[int, int, int]]) -> int:
    x, y, z = droplet
    exposed_sides: int = 6
    for other_droplet in droplets:
        other_x, other_y, other_z = other_droplet
        if is_next_to(other_x, other_y, other_z, x, y, z):
            exposed_sides -= 1
    return exposed_sides


def is_next_to_cube(cube1: tuple[int, int, int], cube2: tuple[int, int, int]) -> bool:
    x1, y1, z1 = cube1
    x2, y2, z2 = cube2
    return is_next_to(x1, y1, z1, x2, y2, z2)


def is_next_to(x1, y1, z1, x2, y2, z2) -> bool:
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1) == 1


def generate_air(max_distance: int, droplets: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    air: list[tuple[int, int, int]] = [(0, 0, 0)]
    changed: bool = True
    while changed:
        changed = False
        for x in range(-1, max_distance + 1):
            for y in range(-1, max_distance + 1):
                for z in range(-1, max_distance + 1):
                    if droplets.__contains__((x, y, z)):
                        continue
                    if air.__contains__((x, y, z)):
                        continue
                    if is_next_to_air(x, y, z, air):
                        air.append((x, y, z))
                        changed = True
    return air


def is_next_to_air(x: int, y: int, z: int, air: list[tuple[int, int, int]]) -> bool:
    for dx in range(-1, 2):
        if air.__contains__((x + dx, y, z)):
            return True
    for dy in range(-1, 2):
        if air.__contains__((x, y + dy, z)):
            return True
    for dz in range(-1, 2):
        if air.__contains__((x, y, z + dz)):
            return True
    return False



def amount_of_exterior_exposed_sides(
        air: list[tuple[int, int, int]],
        droplet: tuple[int, int, int]
) -> int:
    sides: int = 0
    for air_cube in air:
        if is_next_to_cube(air_cube, droplet):
            sides += 1
    return sides


if __name__ == '__main__':
    main()
