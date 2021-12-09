#!/usr/bin/env python3

import sys


def mark_basin(floor, i, j):
    size = 0

    if floor[i][j] == '9':
        return 0

    floor[i] = floor[i][0:j] + '9' + floor[i][(j+1):]
    size += 1

    if i > 0:
        size += mark_basin(floor, i - 1, j)

    if j > 0:
        size += mark_basin(floor, i, j - 1)

    if j < len(floor[0]) - 1:
        size += mark_basin(floor, i, j + 1)

    if i < len(floor) - 1:
        size += mark_basin(floor, i + 1, j)

    return size


def main():
    floor = []

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            floor.append(line.strip())

    rl = len(floor[0])
    ml = len(floor)
    part1 = 0
    part2 = 1
    basins = []
    for i in range(ml):
        for j in range(rl):
            x = floor[i][j]
            if i > 0 and x >= floor[i - 1][j]:
                continue
            if j > 0 and x >= floor[i][j - 1]:
                continue
            if j < rl - 1 and x >= floor[i][j + 1]:
                continue
            if i < ml - 1 and x >= floor[i + 1][j]:
                continue
            part1 += int(x) + 1
    print("Part 1:", part1)

    for i in range(ml):
        for j in range(rl):
            s = mark_basin(floor, i, j)
            if s > 0:
                basins.append(s)
    basins.sort()
    for x in basins[-3:]:
        part2 *= x
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
