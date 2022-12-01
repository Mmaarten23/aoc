def main1():
    depth = 0
    dist = 0
    f = open("input.txt", "r")
    for line in f:
        comp = line.split(" ")
        if comp[0] == "forward":
            dist += int(comp[1])
        if comp[0] == "up":
            depth -= int(comp[1])
        if comp[0] == "down":
            depth += int(comp[1])
    print(str(depth) + " " + str(dist) + " " + str(depth * dist))
    f.close()


def main2():
    depth = 0
    dist = 0
    aim = 0
    f = open("input.txt", "r")
    for line in f:
        comp = line.split(" ")
        if comp[0] == "forward":
            dist += int(comp[1])
            depth += aim * int(comp[1])
        if comp[0] == "up":
            aim -= int(comp[1])
        if comp[0] == "down":
            aim += int(comp[1])
    print(str(depth) + " " + str(dist) + " " + str(depth * dist))
    f.close()


if __name__ == '__main__':
    main1()
    main2()
