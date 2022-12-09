def main():
    f = open("input/input14.txt", "r")
    polymer = [a for a in f.readline().replace("\n", "")]
    f.readline()
    rules = {}
    for line in f.readlines():
        (key, value) = line.replace("\n", "").split(" -> ")
        rules[key] = value
    f.close()

    for k in range(10):
        insertions = 0
        copy = polymer.copy()
        for i in range(len(copy) - 2, -1, -1):
            key = copy[i] + copy[i + 1]
            if rules.__contains__(key):
                polymer.insert(i + 1, rules[key])
                insertions += 1
    print(polymer.count(max(polymer, key=polymer.count)) - polymer.count(min(polymer, key=polymer.count)))


def main2():
    f = open("input/input14.txt")
    lines = f.read().splitlines()

    polymer = lines[0].replace("\n", "")
    raw_mappings = map(lambda char: char.split(" -> "), lines[2::])
    mappings = {}

    for item in raw_mappings:
        pair = item[0]
        toInsert = item[1]
        mappings[pair] = toInsert

    pair_count = {}
    for pair in mappings.keys():
        pair_count[pair] = 0

    for i in range(len(polymer)-1):
        pair_count[polymer[i] + polymer[i+1]] += 1

    letter_count = {}
    for char in polymer:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1

    step = 1

    while step <= 40:
        pair_count, letter_count = stepper(pair_count, letter_count, mappings)
        step += 1

    sorted_vals = sorted(letter_count.items(), key=lambda x: x[1])
    min_letter, max_letter = sorted_vals[0][0], sorted_vals[-1][0]
    print(letter_count[max_letter] - letter_count[min_letter])


def stepper(pair_count, letter_count, mappings):

    result_count = {}
    for pair in mappings.keys():
        result_count[pair] = 0

    for pair in mappings.keys():
        if pair_count[pair] > 0:
            letter = mappings[pair]

            result_count[pair[0] + letter] += pair_count[pair]
            result_count[letter + pair[1]] += pair_count[pair]
            if mappings[pair] in letter_count:
                letter_count[letter] += pair_count[pair]
            else:
                letter_count[letter] = 1

    return result_count, letter_count

if __name__ == '__main__':
    main2()
