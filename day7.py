#!/usr/bin/env python3

import sys


def cost(crabs, pos, clu):
    return sum([clu[abs(pos - x)] for x in crabs])


def main():
    with open(sys.argv[1], 'r') as fhan:
        line = fhan.readline().strip().split(',')
    crabs = [int(x) for x in line]
    low = min(crabs)
    high = max(crabs)
    clu = [0] * (1 + high - low)
    for i in range(1, 1 + high - low):
        clu[i] = i
    print("Part 1", min([cost(crabs, x, clu) for x in range(low, high + 1)]))
    for i in range(1, 1 + high - low):
        clu[i] += clu[i - 1]
    print("Part 2", min([cost(crabs, x, clu) for x in range(low, high + 1)]))


if __name__ == '__main__':
    main()
