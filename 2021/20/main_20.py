from collections import defaultdict

algorithm, inp = open('input.txt', 'r').read().strip().split('\n\n')
assert(len(algorithm) == 512)
image = defaultdict(int)

Y = [0, 99]
X = [0, 99]

def vis():
    print(len(image))
    for r in range(Y[0]-2, Y[1]+3):
        for c in range(X[0]-2, X[1]+3):
            if image[(r, c)] == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

for r, row in enumerate(inp.split()):
    for c, character in enumerate(row):
        if character == '#':
            image[(r, c)] = 1

for t in range(50):
    result = defaultdict(int)
    YA = [0, 0]
    XA = [0, 0]
    for y in range(Y[0]-1, Y[1]+2):
        for x in range(X[0]-1, X[1]+2):
            binstr = ''
            for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if image[(y+dy, x+dx)] == 1 or (t % 2 == 1 and (y+dy < Y[0] or y+dy > Y[1] or x+dx < X[0] or x+dx > X[1])):
                    binstr += '1'
                else:
                    binstr += '0'
            if algorithm[int(binstr, 2)] == '#':
                result[(y, x)] = 1
                if y < YA[0]:
                    YA[0] = y
                if y > YA[1]:
                    YA[1] = y
                if x < XA[0]:
                    XA[0] = x
                if x > XA[1]:
                    XA[1] = x
    image = result
    Y = YA
    X = XA
    if t in [1, 49]:
        vis()