#!/usr/bin/env python3

import sys

TARGETS = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9
}

COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}


def blocked(cmap, x, y):
    a = min(x, y)
    b = max(x, y)
    for i in range(a, b):
        if cmap[1][i] != '.':
            return True
    return False


def available(cmap, a, b):
    colheight = len(cmap) - 3
    result = []
    temps = [1, 2, 4, 6, 8, 10, 11]
    c = cmap[a][b]
    if a == 1:
        if b < TARGETS[c] and blocked(cmap, b + 1, TARGETS[c]):
            return None
        if b > TARGETS[c] and blocked(cmap, TARGETS[c], b):
            return None
        for i in range(colheight):
            d = cmap[colheight + 1 - i][TARGETS[c]]
            if d == '.':
                return [[colheight + 1 - i, TARGETS[c]]]
            if d != c:
                return None

    for p in temps:
        if cmap[1][p] != '.':
            continue
        if p < b and not blocked(cmap, p, b):
            result.append([1, p])
        if p > b and not blocked(cmap, p, b + 1):
            result.append([1, p])
    return result


def ishome(cmap, y, x):
    for i in range(y, len(cmap) - 1):
        c = cmap[i][x]
        if TARGETS[c] != x:
            return False
    return True


def print_map(cmap):
    for line in cmap:
        print(line)


def moveable(cmap):
    result = []
    for j in range(1, len(cmap[1]) - 1):
        if cmap[1][j] in 'ABCD':
            if available(cmap, 1, j):
                result.append([1, j])
    for item in TARGETS:
        j = TARGETS[item]
        i = 2
        while cmap[i][j] == '.':
            i += 1
        c = cmap[i][j]
        if c not in 'ABCD':
            continue
        if ishome(cmap, i, j):
            continue
        if available(cmap, i, j):
            result.append([i, j])
    return result


def charsub(string, ind, c):
    return string[:ind] + c + string[ind + 1:]


def move(cmap, ax, ay, bx, by):
    c = cmap[ay][ax]
    cmap[ay] = charsub(cmap[ay], ax, '.')
    cmap[by] = charsub(cmap[by], bx, c)
    return (abs(ax - bx) + abs(ay - by)) * COSTS[c]


def final(cmap):
    for item in TARGETS:
        c = TARGETS[item]
        for i in range(2, len(cmap) - 1):
            if cmap[i][c] != item:
                return False
    return True


def tokey(cmap):
    result = ''
    for i in range(1, len(cmap) - 1):
        result += cmap[i]
    return result


def attempt(cmap, score, seen):
    result = []

    kmap = tokey(cmap)
    if kmap in seen and seen[kmap] <= score:
        return None
    if 'final' in seen and score >= seen['final']:
        return None
    seen[kmap] = score

    if final(cmap):
        if 'final' in seen:
            if score < seen['final']:
                seen['final'] = score
        else:
            seen['final'] = score
        return score

    for item in moveable(cmap):
        for tgt in available(cmap, item[0], item[1]):
            nmap = list(cmap)
            val = move(nmap, item[1], item[0], tgt[1], tgt[0])
            res = attempt(nmap, score + val, seen)
            if res:
                result.append(res)
    if result:
        val = min(result)
        return val
    return None


def main():
    sys.setrecursionlimit(1000000)
    seen = {}
    cmap = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            cmap.append(line.strip("\n"))
    print("Part 1:", attempt(cmap, 0, seen))
    cmap.insert(3, '  #D#B#A#C#')
    cmap.insert(3, '  #D#C#B#A#')
    seen = {}
    print("Part 2:", attempt(cmap, 0, seen))


if __name__ == '__main__':
    main()
