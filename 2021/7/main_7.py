def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    crabs = [int(a) for a in lines[0].split(",") if a != "\n"]
    counts = [0] * 2000
    for crab in crabs:
        if crab >= 2000:
            print("ERROR")
        for count_pos in range(0, len(counts)):
            counts[count_pos] += (abs(crab - count_pos) * (abs(crab - count_pos) + 1)) / 2
    print(min(counts))


if __name__ == '__main__':
    main()
