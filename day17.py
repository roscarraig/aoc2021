#!/usr/bin/env python3

import re
import sys


def inbox(x, y, tx, ty):
    if x < tx[0] or x > tx[1] or y > ty[1] or y < ty[0]:
        return False
    return True


def track(dx, dy, tx, ty):
    x = 0
    y = 0
    maxy = 0
    while x <= tx[1] and y >= ty[0]:
        x += dx
        y += dy

        if y > maxy:
            maxy = y
        if dx > 0:
            dx -= 1
        dy -= 1
        if inbox(x, y, tx, ty):
            return True, maxy
    return False, 0


def main():
    with open(sys.argv[1], 'r') as fhan:
        line = fhan.readline().strip()
    parts = re.match(r'target area: x=(\d+)\.\.(\d+), y=(-\d+)\.\.(-\d+)', line).groups()
    tx = [int(x) for x in parts[0:2]]
    ty = [int(x) for x in parts[2:]]
    minr = 0
    part1 = 0
    part2 = 0
    for i in range(tx[1] + 1):
        minr += i
        if minr < tx[0]:
            continue
        for j in range(ty[0], -ty[0] + 1):
            isin, alt = track(i, j, tx, ty)
            if isin:
                part2 += 1
            if alt > part1:
                part1 = alt
    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
