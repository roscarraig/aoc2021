#!/usr/bin/env python3

import sys


def window(image, x, y, pattern, flash):
    bits = ''
    space = '.#'[flash]

    if pattern[0] == '.':
        space = '.'

    result = 0
    width = len(image[0])
    depth = len(image)

    for j in range(-1, 2):
        for i in range(-1, 2):
            if 0 <= i + x < width and 0 <= j + y < depth:
                bits += image[y + j][x + i]
            else:
                bits += space

    for x in bits:
        result *= 2
        if x == '#':
            result += 1

    return pattern[result]


def count(image):
    result = 0
    for j in range(len(image)):
        result += len(image[j].replace('.', ''))
    return result


def process(image, pattern, flash):
    result = []
    w = 2
    for j in range(-w, len(image) + w):
        line = ''
        for i in range(-w, len(image[0]) + w):
            line += window(image, i, j, pattern, flash)
        result.append(line)

    if flash == 0:
        while result[0].find('.') < 0:
            result.pop(0)
        while result[-1].find('.') < 0:
            result.pop()
        rlen = len(result)
        while '.' not in [x[0] for x in result]:
            for i in range(rlen):
                result[i] = result[i][1:]
        while '.' not in [x[-1] for x in result]:
            for i in range(rlen):
                result[i] = result[i][:-1]

    return result


def main():
    image = []
    with open(sys.argv[1], 'r') as fhan:
        pattern = fhan.readline().strip()
        fhan.readline()
        for line in fhan.readlines():
            image.append(line.strip())
    for i in range(2):
        image = process(image, pattern, i % 2)
    print("Part 1:", count(image))

    for i in range(48):
        image = process(image, pattern, i % 2)
    print("Part 2:", count(image))


if __name__ == '__main__':
    main()
