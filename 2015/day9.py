import re


def main():
    lines: list[tuple[str, str, int]] = [(groups[0], groups[1], int(groups[2]))
                                         for groups in (re.match(r'(.*) to (.*) = (\d*)', line).groups()
                                                        for line in open('input/input9.txt', 'r').readlines())]
    cities: list[str] = list(set(line[0] for line in lines).union(set(line[1] for line in lines)))
    paths: list[list[int]] = [[0 for _ in range(len(cities))] for _ in range(len(cities))]
    for line in lines:
        paths[cities.index(line[0])][cities.index(line[1])] = line[2]
        paths[cities.index(line[1])][cities.index(line[0])] = line[2]
    result = []
    for c in cities:
        result.extend(visit_all(cities, paths, c, [x for x in cities if x != c]))
    print(f'Part 1: {min(result)}')
    print(f'Part 2: {max(result)}')


def visit_all(c: list[str], p: list[list[int]], current: str, to_visit: list[str]) -> list[int]:
    if len(to_visit) == 1:
        return [p[c.index(current)][c.index(to_visit[0])]]
    result: list[int] = []
    for city in to_visit:
        cost: int = p[c.index(current)][c.index(city)]
        result.extend([cost + v for v in visit_all(c, p, city, [x for x in to_visit if x != city])])
    return result


if __name__ == '__main__':
    main()
