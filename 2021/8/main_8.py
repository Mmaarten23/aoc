import itertools


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    correctValues = [2, 3, 4, 7]
    outputDigits = []
    for line in lines:
        output = line.split(" | ")[1]
        for digit in [a for a in output.replace("\n", "").split(" ") if correctValues.__contains__(len(a))]:
            outputDigits.append(digit)
    print(len(outputDigits))


def main2():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    alphabet = ["a", "b", "c", "d", "e", "f", "g"]
    numbermapping = dict()
    numbermapping["abcefg"] = 0
    numbermapping["cf"] = 1
    numbermapping["acdeg"] = 2
    numbermapping["acdfg"] = 3
    numbermapping["bcdf"] = 4
    numbermapping["abdfg"] = 5
    numbermapping["abdefg"] = 6
    numbermapping["acf"] = 7
    numbermapping["abcdefg"] = 8
    numbermapping["abcdfg"] = 9

    totalcount = 0
    for line in lines:
        mapping = list(itertools.permutations(alphabet))
        inp, outp = line.split(" | ")
        lineMapping = []
        for permutation in mapping:
            correct = True
            for inputDigit in inp.split(" "):
                array = [permutation[alphabet.index(a)] for a in inputDigit]
                array.sort()
                translated = "".join(array)
                if not numbermapping.__contains__(translated):
                    correct = False
                    break
            if correct:
                lineMapping = permutation
                break
        linenr = ""
        for outputDigit in outp.split(" "):
            array = [lineMapping[alphabet.index(a)] for a in outputDigit.replace("\n", "")]
            array.sort()
            translated = "".join(array)
            linenr += str(numbermapping[translated])
        totalcount += int(linenr)
    print("total = " + str(totalcount))


if __name__ == '__main__':
    main2()
