#!/usr/bin/env python3

import sys


def main():
    with open(sys.argv[1], 'r') as fhan:
        input = [int(x) for x in fhan.read().split('\n') if x != '']
    part1 = 0
    part2 = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            part1 += 1
    print("Part 1: {}".format(part1))
    for i in range(0, len(input) - 3):
        if input[i] < input[i + 3]:
            part2 += 1
    print("Part 2: {}".format(part2))


if __name__ == '__main__':
    main()
