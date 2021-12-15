#!/usr/bin/env python3

import sys


def run_cave(cmap, risk):
    changes = 0
    cy = len(cmap)
    cx = len(cmap[0])

    for y in range(cy):
        for x in range(cx):
            a = cmap[y][x]
            sides = []
            if y > 0:
                sides.append(risk[y - 1][x])
            if x > 0:
                sides.append(risk[y][x - 1])
            if y < (cy - 1):
                sides.append(risk[y + 1][x])
            if x < (cx - 1):
                sides.append(risk[y][x + 1])
            a += min(sides)
            if a < risk[y][x]:
                risk[y][x] = a
                changes += 1
    return changes


def main():
    cmap = []
    cmap2 = []
    risk = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            cmap.append([int(x) for x in line.strip()])
            cmap2.append([int(x) for x in line.strip()])
            risk.append([0] * len(cmap[0]) * 5)

    cy = len(cmap)
    cx = len(cmap[0])

    for y in range(cy):
        for x in range(cx):
            if x == 0:
                if y > 0:
                    risk[y][x] = risk[y - 1][x] + cmap[y][x]
            else:
                risk[y][x] = risk[y][x - 1] + cmap[y][x]

    while (run_cave(cmap, risk)):
        pass
    print("Part 1:", risk[cy - 1][cx - 1])

    for j in range(cy):
        for k in range(1, 5):
            cmap2[j] += [((cmap2[j][i] + k - 1) % 9 + 1) for i in range(cx)]

    for k in range(1, 5):
        for j in range(cy):
            cmap2.append([((cmap2[j][i] + k - 1) % 9 + 1) for i in range(cx * 5)])

    for j in range(4 * cy):
        risk.append([0] * 5 * cx)

    cy *= 5
    cx *= 5

    for y in range(cy):
        for x in range(cx):
            if risk[y][x]:
                continue
            if x == 0:
                if y > 0:
                    risk[y][x] = risk[y - 1][x] + cmap2[y][x]
            else:
                risk[y][x] = risk[y][x - 1] + cmap2[y][x]

    while (run_cave(cmap2, risk)):
        pass
    print("Part 2:", risk[cy - 1][cx - 1])


if __name__ == '__main__':
    main()
