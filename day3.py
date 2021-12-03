#!/usr/bin/env python3

import sys


def filter(lines, width, bit):
    value = 0
    for i in range(width):
        count = len(lines)
        bitcount = len([line[i] for line in lines if line[i] == str(bit)])
        value *= 2
        if bit:
            if bitcount >= count / 2:
                cbit = bit
            else:
                cbit = 1 - bit
        else:
            if bitcount <= count / 2:
                cbit = bit
            else:
                cbit = 1 - bit
        value += cbit
        lines = [line for line in lines if line[i] == str(cbit)]
        if len(lines) == 1:
            for j in range(i + 1, width):
                value *= 2
                if lines[0][j] == '1':
                    value += 1
            return value
    return value


def main():
    entries = 0
    counts = [0] * 16
    gamma = 0
    epsilon = 0
    width = 0
    olines = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            if width == 0:
                width = len(line.strip())
            for i in range(width):
                if line[i] == '1':
                    counts[i] += 1
            entries += 1
            olines.append(line.strip())

    for i in range(width):
        if counts[i] > entries / 2:
            bit = 1
        else:
            bit = 0
        gamma *= 2
        epsilon *= 2
        gamma += bit
        epsilon += 1 - bit

    print("Part 1:", gamma * epsilon)
    print("Part 2:", filter(olines, width, 1) * filter(olines, width, 0))


if __name__ == '__main__':
    main()
