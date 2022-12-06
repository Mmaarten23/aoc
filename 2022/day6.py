def main():
    text: str = open('input6.txt', 'r').read()
    part_1 = 0
    part_2 = 0
    for i in range(len(text)):
        if len(set(text[i:i + 4])) == 4:
            part_1 = i + 4
            break
    for i in range(len(text)):
        if len(set(text[i:i + 14])) == 14:
            part_2 = i + 14
            break
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


if __name__ == '__main__':
    main()
