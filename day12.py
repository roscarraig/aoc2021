#!/usr/bin/env python3

import sys


def walk1(cmap, prefix, node):
    result = set()

    if node.islower() and node in prefix:
        return set()

    if node != 'start':
        prefix += ','

    prefix += node

    if node == 'end':
        return set([prefix])

    for x in cmap[node]:
        result |= walk1(cmap, prefix, x)

    return result


def walk2(cmap, prefix, node):
    result = set()
    if node.islower() and node in prefix:
        if node in ['start', 'end']:
            return set()

        prefix += ',' + node

        for x in cmap[node]:
            result |= walk1(cmap, prefix, x)
        return result

    if node != 'start':
        prefix += ','

    prefix += node

    if node == 'end':
        return set([prefix])

    for x in cmap[node]:
        result |= walk2(cmap, prefix, x)

    return result


def main():
    cmap = {}
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            parts = line.strip().split('-')
            for x in range(2):
                if parts[x] not in cmap:
                    cmap[parts[x]] = set()
                cmap[parts[x]].add(parts[1 - x])
    part1 = walk1(cmap, '', 'start')
    print("Part 1:", len(part1))
    part2 = walk2(cmap, '', 'start')
    print("Part 2:", len(part2))


if __name__ == '__main__':
    main()
