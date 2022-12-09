def main1():
    prev = 1000000
    count = 0
    f = open("input/input1.txt", "r")
    for line in f:
        if int(line) > prev:
            count += 1
        prev = int(line)
    print(count)
    f.close()


def main2():
    prev = 1000000
    arr = []
    count = 0
    f = open("input/input1.txt", "r")
    for line in f:
        arr.insert(0, int(line))
        if len(arr) > 3:
            arr.pop()
        if len(arr) == 3:
            if sum(arr) > prev:
                count += 1
            prev = sum(arr)
    print(count)
    f.close()


if __name__ == '__main__':
    main1()
    main2()
