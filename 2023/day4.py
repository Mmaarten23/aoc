def part1(data):
    s = 0
    for winning, owned in data:
        total = len(winning) + len(owned)
        together = set(winning).union(owned)
        matches = total - len(together)
        s += 0 if matches == 0 else 2 ** (matches - 1)
    print(s)


def part2(data):
    annotated = data.copy()
    for x in annotated:
        x.append(1)
    for i in range(len(data)):
        winning, owned, multiplier = annotated[i]
        total = len(winning) + len(owned)
        together = set(winning).union(owned)
        matches = total - len(together)
        for j in range(1, matches + 1):
            annotated[i + j][2] += multiplier
    print(sum([x[2] for x in annotated]))


def main():
    with open("input/day4.txt") as f:
        lines = f.read().splitlines()
    data = []
    for i in range(len(lines)):
        data.append(lines[i].split(":")[1])
    for i in range(len(data)):
        data[i] = data[i].split("|")
    for i in range(len(data)):
        winning, owned = data[i]
        data[i][0] = [int(x) for x in winning.split(" ") if x.isdigit()]
        data[i][1] = [int(x) for x in owned.split(" ") if x.isdigit()]
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
