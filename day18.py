#!/usr/bin/env python3

import re
import sys


def find5(line):
    i = 0
    depth = 0
    while i < len(line):
        if line[i] == "[":
            depth += 1
        elif line[i] == "]":
            depth -= 1
        if depth == 5:
            mat = re.search(r'\[\d+,\d+\]', line[i:])
            return i + mat.start()
        i += 1
    return 0


def regulars(line):
    rest = r'(?=[^\d]\d+[^\d])'
    return [j + 1 for j in [i.start() for i in re.finditer(rest, line)]]


def nsplit(x):
    v = int(x)
    return '[{0},{1}]'.format(int(v / 2), int(v / 2) + v % 2)


def nreduce(line):
    while True:
        f5 = find5(line)
        while f5:
            newline = ''
            lpos = 0
            rpos = 0
            matches = regulars(line[:f5])

            if matches:
                lpos = max(matches)

            right = line.index(']', f5) + 1
            numbers = re.match(r'\[(\d+),(\d+)\]', line[f5:right])
            a = int(numbers.group(1))
            b = int(numbers.group(2))
            matches = regulars(line[right:])

            if matches:
                rpos = min(matches)

            if lpos:
                newline = line[:lpos]
                nval = re.match(r'(\d+)', line[lpos:f5])
                newline += str(a + int(nval.group(1)))
                newline += line[lpos + len(nval.group(1)):f5]
            else:
                newline = line[:f5]

            newline += '0'

            if rpos:
                newline += line[right:(right + rpos)]
                nval = re.match(r'(\d+)', line[right + rpos:])
                newline += str(b + int(nval.group(1)))
                newline += line[right + rpos + len(nval.group(1)):]
            else:
                newline += line[right:]
            line = newline
            f5 = find5(line)
        big = re.search(r'(\d\d+)', line)
        if not big:
            return line
        newline = line[:big.start()] + nsplit(big.group(1)) + line[big.start() + len(big.group(1)):]
        line = newline


def sum(a, b):
    return nreduce('[{0},{1}]'.format(a, b))


def magnitude(line):
    pat = re.compile(r'\[(\d+),(\d+)\]')
    mat = pat.search(line)
    while mat:
        left = mat.start(1) - 1
        a = mat.group(1)
        b = mat.group(2)
        le = len(a) + len(b) + 3
        val = str(3 * int(a) + 2 * int(b))
        line = line[:left] + val + line[left + le:]
        mat = pat.search(line)
    return line


def main():
    sline = ''
    lines = []
    part2 = 0
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            lines.append(nreduce(line.strip()))
            if sline == '':
                sline = nreduce(line.strip())
            else:
                sline = sum(sline, nreduce(line.strip()))
    print("Part 1:", magnitude(sline))
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                continue
            part2 = max(part2, int(magnitude(sum(lines[i], lines[j]))))
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
