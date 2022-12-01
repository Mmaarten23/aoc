def main():
    links = set()
    f = open("input.txt", "r")
    for line in f:
        links.add(tuple(a for a in line.replace("\n", "").split("-")))
    f.close()
    paths = [["start"]]
    count = 0
    while not len(paths) == 0:
        print(len(paths))
        to_remove = []
        to_add = []
        for path in paths:
            if isEnd(path[0]):
                to_remove.append(path)
                count += 1
                continue
            to_remove.append(path)
            end_node = path[0]
            for link in links:
                if not contains(end_node, link):
                    continue
                other = getOther(end_node, link)
                if isValidExtension(path, other):
                    copy = path.copy()
                    copy.insert(0, other)
                    to_add.append(copy)
        for removing in to_remove:
            paths.remove(removing)
        for adding in to_add:
            paths.append(adding)
    print(count)


def isStart(node):
    return node == "start"


def isEnd(node):
    return node == "end"


def isSmallCave(node):
    return node.islower()


def contains(node, tup):
    return tup.__contains__(node)


def getOther(node, tup):
    if not contains(node, tup):
        return None
    return tup[1] if tup[0] == node else tup[0]


def isFinished(paths):
    for path in paths:
        if not isEnd(path[0]):
            return False
    return True


def isValidExtension(path, node):
    if isStart(node):
        return False
    if not isSmallCave(node):
        return True
    return path.count(node) <= (0 if hasDoubleVisit(path) else 1)


def hasDoubleVisit(path):
    for value in path:
        if isSmallCave(value) and path.count(value) > 1:
            return True
    return False


if __name__ == '__main__':
    main()
