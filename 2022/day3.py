def main():
    lines: list[str] = open('input/input3.txt', 'r').readlines()

    wrong: list = list()
    for line in lines:
        split: int = int(len(line) / 2)
        wrong.append(set(line[:split]).intersection(line[split:]).pop())

    badges: list = list()
    for i in range(0, len(lines), 3):
        badges.append(set(lines[i].strip()).intersection(lines[i + 1]).intersection(lines[i + 2]).pop())

    scores: list[int] = [get_score(x) for x in wrong]
    scores2: list[int] = [get_score(x) for x in badges]
    print(f'Part 1: {sum(scores)}')
    print(f'Part 2: {sum(scores2)}')


def get_score(x: str) -> int:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return alphabet.index(x) + 1


if __name__ == '__main__':
    main()
