def main():
    f = open("input/input10.txt", "r")
    lines = f.readlines()
    f.close()
    points = 0

    for line in lines:
        stack = []
        for char in line.replace("\n", ""):
            if isOpening(char):
                stack.insert(0, char)
                continue
            if stack[0] == getOther(char):
                stack.pop(0)
                continue
            points += getScore(char)
            break
    print(points)


def main2():
    f = open("input/input10.txt", "r")
    lines = f.readlines()
    f.close()
    correct_lines = []

    for line in lines:
        correct = True
        stack = []
        for char in line.replace("\n", ""):
            if isOpening(char):
                stack.insert(0, char)
                continue
            if stack[0] == getOther(char):
                stack.pop(0)
                continue
            correct = False
            break
        if correct:
            correct_lines.append(line)
    scores = []
    for correct_line in correct_lines:
        stack = []
        for char in correct_line:
            if isOpening(char):
                stack.insert(0, char)
                continue
            if stack[0] == getOther(char):
                stack.pop(0)
                continue
            break
        score = 0
        for completion in stack:
            score *= 5
            score += getCorrectScore(getOther(completion))
        scores.append(score)
    scores.sort()
    print (scores)
    print(scores[int((len(scores) - 1) / 2)])


def getOther(char):
    if char == "[":
        return "]"
    if char == "]":
        return "["
    if char == "(":
        return ")"
    if char == ")":
        return "("
    if char == "<":
        return ">"
    if char == ">":
        return "<"
    if char == "{":
        return "}"
    if char == "}":
        return "{"


def isOpening(char):
    return char == "<" or char == "{" or char == "[" or char == "("


def getScore(char):
    if char == "]":
        return 57
    if char == ")":
        return 3
    if char == ">":
        return 25137
    if char == "}":
        return 1197


def getCorrectScore(char):
    if char == "]":
        return 2
    if char == ")":
        return 1
    if char == ">":
        return 4
    if char == "}":
        return 3


if __name__ == '__main__':
    main2()
