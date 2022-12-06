def main():
    text: str = open('input1.txt').read()
    part_1: int = text.count('(') - text.count(')')
    part_2: int = 0
    floor: int = 0
    for i in range(len(text)):
        if text[i] == '(':
            floor += 1
        elif text[i] == ')':
            floor -= 1
        if floor == -1:
            part_2: int = i + 1
            break

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


if __name__ == '__main__':
    main()
