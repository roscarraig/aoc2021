#!/usr/bin/env python3

import re
import sys


def draw(dmap, xy):
    if(xy[0] == xy[2]):
        for i in range(min(xy[1], xy[3]), max(xy[1], xy[3]) + 1):
            dmap[i][xy[0]] += 1
    elif(xy[1] == xy[3]):
        for i in range(min(xy[0], xy[2]), max(xy[0], xy[2]) + 1):
            dmap[xy[1]][i] += 1
    else:
        dist = abs(xy[0] - xy[2]) + 1
        if xy[0] > xy[2]:
            dx = -1
        else:
            dx = 1
        if xy[1] > xy[3]:
            dy = -1
        else:
            dy = 1

        for i in range(dist):
            dmap[xy[1] + i * dy][xy[0] + i * dx] += 1


def count(dmap, mx, my, limit):
    result = 0
    for i in range(mx + 1):
        for j in range(my + 1):
            if dmap[j][i] >= limit:
                result += 1
    return result


def main():
    copat = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    mx = 0
    my = 0
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            xy = [int(x) for x in copat.findall(line)[0]]
            mx = max(mx, xy[0], xy[2])
            my = max(my, xy[1], xy[3])
    map1 = [[0 for _ in range(mx + 1)] for _ in range(my + 1)]
    map2 = [[0 for _ in range(mx + 1)] for _ in range(my + 1)]

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            xy = [int(x) for x in copat.findall(line)[0]]

            if(xy[0] == xy[2] or xy[1] == xy[3]):
                draw(map1, xy)
            draw(map2, xy)
    print("Part 1:", count(map1, mx, my, 2))
    print("Part 2:", count(map2, mx, my, 2))


if __name__ == '__main__':
    main()
