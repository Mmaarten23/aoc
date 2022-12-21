def main():
    original: list[int] = [int(line) for line in open("test_data.txt", 'r').readlines()]
    actual: list[int] = [x for x in range(len(original))]
    for i in range(len(original)):
        value: int = original[i]
        if value == 0:
            print(apply_permutations(original, actual))
            continue
        actual_index: int = actual[i]
        new_actual: int = actual_index + value + (0 if value > 0 else -1)
        end: int = (new_actual + len(actual) + 1) % len(actual)
        if end == 0 and value < 0:
            end = len(actual)
        range_to_move: range = range(actual_index + 1, end)
        new_actual = (new_actual + (0 if new_actual < len(actual) else 1)) % len(original)
        for j in range(len(actual)):
            if actual[j] in range_to_move:
                actual[j] -= 1
                actual[j] += len(original) if actual[j] < 0 else 0
                actual[j] %= len(original)
        actual[i] = new_actual
        print(apply_permutations(original, actual))
    permutations: list[int] = apply_permutations(original, actual)
    print(permutations)
    start_index = permutations.index(0)
    print(permutations[(start_index + 1000) % len(permutations)])
    print(permutations[(start_index + 2000) % len(permutations)])
    print(permutations[(start_index + 3000) % len(permutations)])
    result =  + permutations[(start_index + 2000) % len(permutations)] + permutations[(start_index + 3000) % len(permutations)]
    print(f'Part 1: {result}')


def apply_permutations(original: list[int], actual: list[int]) -> list[int]:
    result: list[int] = [0] * len(original)
    for i in range(len(original)):
        result[actual[i]] = original[i]
    return result


if __name__ == '__main__':
    main()
