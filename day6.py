#!/usr/bin/env python3

import sys


def generation(shoal):
    spawn = shoal.pop(0)
    shoal.append(0)
    shoal[6] += spawn
    shoal[8] += spawn


def main():
    with open(sys.argv[1], 'r') as fhan:
        line = fhan.readline().strip().split(',')
    start = [int(x) for x in line]
    shoal = [0] * 9
    for fish in start:
        shoal[fish] += 1

    for i in range(80):
        generation(shoal)
    print("Part 1", sum(shoal))
    for _ in range(256 - 80):
        generation(shoal)
    print("Part 2", sum(shoal))


if __name__ == '__main__':
    main()
