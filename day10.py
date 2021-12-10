#!/usr/bin/env python3

import sys


def parse(line):
    stack = []
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    score1 = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    score2 = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    result = 0
    for i in range(len(line)):
        if line[i] in '([{<':
            stack.append(line[i])
        else:
            if line[i] != pairs[stack.pop()]:
                return -score1[line[i]]
    while(stack):
        result *= 5
        result += score2[stack.pop()]
    return result


def main():
    part1 = 0
    part2s = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            x = parse(line.strip())
            if x < 0:
                part1 += -x
            else:
                part2s.append(x)
    print("Part 1:", part1)
    part2s.sort()
    print("Part 2:", part2s[int(len(part2s) / 2)])


if __name__ == '__main__':
    main()
