#!/usr/bin/env python3

import sys


def main():
    h = 0
    d = 0
    d2 = 0
    a = 0
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            [move, delta] = line.split(' ')
            if move == 'forward':
                h += int(delta)
                d2 += a * int(delta)
            elif move == 'down':
                d += int(delta)
                a += int(delta)
            elif move == 'up':
                d -= int(delta)
                a -= int(delta)
            else:
                print('Unexpected input:', line)
    print('Part 1:', h * d)
    print('Part 2:', h * d2)


if __name__ == '__main__':
    main()
