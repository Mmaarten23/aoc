import re


def main():
    commands: list[str] = open('input6.txt', 'r').readlines()
    # lights: list[list[int]] = [[False for _ in range(0, 1_000)] for _ in range(0, 1_000)]
    lights: list[list[int]] = [[0 for _ in range(0, 1_000)] for _ in range(0, 1_000)]
    for command in commands:
        match = re.search(r'(.*) (\d+),(\d+) through (\d+),(\d+)', command)
        cmd: str = match.group(1)
        coord: tuple[int, int] = (int(match.group(2)), int(match.group(3)))
        coord2: tuple[int, int] = (int(match.group(4)) + 1, int(match.group(5)) + 1)
        for i in range(coord[0], coord2[0]):
            for j in range(coord[1], coord2[1]):
                if cmd == 'turn on':
                    # lights[i][j] = True
                    lights[i][j] += 1
                elif cmd == 'turn off':
                    # lights[i][j] = False
                    lights[i][j] = max(lights[i][j] - 1, 0)
                elif cmd == 'toggle':
                    # lights[i][j] = not lights[i][j]
                    lights[i][j] += 2
    result: int = sum([sum(x) for x in lights])
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
