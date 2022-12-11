import re


def main():
    old: str = open('input/input11.txt', 'r').read()
    new: str = old
    new = create_new(new)
    new_2: str = create_new(new)
    print(f'Part 1: {new}')
    print(f'Part 2: {new_2}')


def create_new(new):
    while True:
        index: int = len(new) - 1
        while True:
            new, overflow = wrap(new, index)
            index -= 1
            if not overflow:
                break
        if is_valid(new):
            break
    return new


def wrap(old: str, pos: int) -> tuple[str, bool]:
    alphabet: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_char: str = alphabet[(alphabet.index(old[pos]) + 1) % len(alphabet)]
    return ''.join([old[i] if not i == pos else new_char for i in range(len(old))]), new_char == 'a'


def is_valid(new: str) -> bool:
    return is_increasing(new) and is_not_confusing(new) and has_pairs(new)


def is_increasing(new: str) -> bool:
    for i in range(len(new) - 2):
        if 'abcdefghijklmnopqrstuvwxyz'.find(new[i:i + 3]) != -1:
            return True
    return False


def is_not_confusing(new: str) -> bool:
    for i in ['i', 'o', 'l']:
        if new.__contains__(i):
            return False
    return True


def has_pairs(new: str) -> bool:
    return re.search(r'(\w)\1.*(\w)\2', new) is not None


if __name__ == '__main__':
    main()
