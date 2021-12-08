#!/usr/bin/env python3

import sys


def parsepart1(line):
    parts = line.strip().split(' | ')
    digits = parts[1].split(' ')
    return len([x for x in digits if len(x) in [2, 3, 4, 7]])


def sortsegments(segs):
    return ''.join(sorted([segs[i] for i in range(len(segs))]))


def matches(src, dst):
    for i in range(len(src)):
        if src[i] not in dst:
            return False
    return True


def parsepart2(line):
    lookup = {}
    found = [''] * 10
    parts = line.strip().split(' | ')
    feed = [sortsegments(x) for x in parts[0].split(' ')]
    digits = [sortsegments(x) for x in parts[1].split(' ')]
    result = 0

    for item in feed:
        if len(item) == 2:
            found[1] = item
        elif len(item) == 3:
            found[7] = item
        elif len(item) == 4:
            lookup[item] = '4'
            found[4] = item
        elif len(item) == 7:
            found[8] = item

    for item in feed:
        if item in found:
            continue
        if matches(found[1], item) and len(item) == 5:
            found[3] = item
        elif matches(found[4], item):
            found[9] = item

    for item in feed:
        if item in found:
            continue
        if matches(found[1], item):
            found[0] = item
        elif len(item) == 6 and not matches(found[1], item):
            found[6] = item

    for item in feed:
        if item in found:
            continue
        if matches(item, found[6]):
            found[5] = item
        elif not matches(item, found[6]):
            found[2] = item

    for item in digits:
        result *= 10
        result += found.index(item)

    return result


def main():
    part1 = 0
    part2 = 0
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            part1 += parsepart1(line)
            part2 += parsepart2(line)
    print("Part 1: {}".format(part1))
    print("Part 2: {}".format(part2))


if __name__ == '__main__':
    main()
