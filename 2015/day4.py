import hashlib


def main():
    text: str = open('input/input4.txt').read()
    part_1 = 0
    part_2 = 0
    for i in range(1, 10000000000000):
        if part_1 != 0 and part_2 != 0:
            break
        if hashlib.md5((text + str(i)).encode()).hexdigest()[:5] == '00000' and part_1 == 0:
            part_1 = i
        if hashlib.md5((text + str(i)).encode()).hexdigest()[:6] == '000000':
            part_2 = i

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


if __name__ == '__main__':
    main()
