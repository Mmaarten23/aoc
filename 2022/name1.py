def main():
    text = open('input1.txt', 'r').read()
    maximum = []
    running_total = 0
    for line in text.split('\n'):
        if line == '':
            maximum.append(running_total)
            running_total = 0
        else:
            running_total += int(line)
    print(sum(sorted(maximum, reverse=True)[:3]))


if __name__ == '__main__':
    main()
