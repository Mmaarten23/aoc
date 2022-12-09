import re


def main():
    lines: list[str] = open('input/input5.txt').readlines()
    part_1: int = 0
    part_2: int = 0
    for line in lines:
        if more_than_three_vowels(line) and double_letter(line) and not contains_illegal_strings(line):
            part_1 += 1
        if pair_appears_twice(line) and letter_appears_between(line):
            part_2 += 1

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


def more_than_three_vowels(line: str) -> bool:
    vowels: int = 0
    for i in ['a', 'e', 'i', 'o', 'u']:
        vowels += line.count(i)
    return vowels >= 3


def double_letter(line: str) -> bool:
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            return True
    return False


def contains_illegal_strings(line: str) -> bool:
    for i in ['ab', 'cd', 'pq', 'xy']:
        if line.find(i) != -1:
            return True
    return False


def pair_appears_twice(line):
    return re.search(r'(\w\w).*\1', line) is not None


def letter_appears_between(line):
    return re.search(r'(\w).\1', line) is not None


if __name__ == '__main__':
    main()
