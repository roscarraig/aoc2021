#!/usr/bin/env python3

import sys


def grow(chain, rules):
    result = {}

    for x in chain.keys():
        seg = x[0] + rules[x]
        a = result.get(seg, 0) + chain[x]
        result[seg] = a
        seg = rules[x] + x[1]
        a = result.get(seg, 0) + chain[x]
        result[seg] = a
    return result


def count(chain, last):
    counts = {last: 1}
    for item in chain:
        j = counts.get(item[0], 0) + chain[item]
        counts[item[0]] = j
    vals = [counts[x] for x in counts]
    return max(vals) - min(vals)


def main():
    rules = {}
    chain = {}

    with open(sys.argv[1], 'r') as fhan:
        start = fhan.readline().strip()
        last = start[-1]
        fhan.readline()
        for line in fhan.readlines():
            rule = line.strip().split(' -> ')
            rules[rule[0]] = rule[1]

    for i in range(len(start) - 1):
        a = start[i:(i + 2)]
        b = chain.get(a, 0) + 1
        chain[a] = b

    for i in range(10):
        chain = grow(chain, rules)

    print("Part 1:", count(chain, last))

    for i in range(30):
        chain = grow(chain, rules)

    print("Part 2:", count(chain, last))


if __name__ == '__main__':
    main()
