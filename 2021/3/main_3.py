def main1(length):
    arr = [0] * length
    count = 0
    f = open("input.txt", "r")
    for line in f:
        chars = [char for char in line]
        for el in range(0, len(chars) - 1):
            arr[el] += int(chars[el])
        count += 1
    f.close()

    gamma = str.join("", ["1" if a > count / 2 else "0" for a in arr])
    epsilon = str.join("", ["0" if a > count / 2 else "1" for a in arr])
    int_gamma = int(gamma, 2)
    int_epsilon = int(epsilon, 2)
    print(int_epsilon * int_gamma)
    print(arr)
    print(count / 2)


def main2():
    lines = []
    f = open("input.txt", "r")
    for line in f:
        lines.append([char for char in line if char != "\n"])
    f.close()
    i = 0
    while len(lines) > 1:
        amount_of_1 = 0
        for line in lines:
            amount_of_1 += int(line[i])
        if amount_of_1 / len(lines) > 0.5:
            char = 1
        elif amount_of_1 / len(lines) < 0.5:
            char = 0
        else:
            char = 1
        lines = [a for a in lines if int(a[i]) == char]
        i += 1

    oxygen = str.join("", lines[0])
    int_oxygen = int(oxygen, 2)

    lines = []
    f = open("input.txt", "r")
    for line in f:
        lines.append([char for char in line if char != "\n"])
    f.close()
    i = 0
    while len(lines) > 1:
        amount_of_1 = 0
        for line in lines:
            amount_of_1 += int(line[i])
        if amount_of_1 / len(lines) > 0.5:
            char = 0
        elif amount_of_1 / len(lines) < 0.5:
            char = 1
        else:
            char = 0
        lines = [a for a in lines if int(a[i]) == char]
        i += 1

    co2 = str.join("", lines[0])
    int_co2 = int(co2, 2)
    print(int_co2 * int_oxygen)


if __name__ == '__main__':
    # main1(5)
    main2()
