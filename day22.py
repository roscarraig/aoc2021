#!/usr/bin/env python3

import sys


class Box(object):
    def __init__(self, sides):
        self.update(sides)

    def update(self, sides):
        self.sides = sides
        self.score = 1
        for i in range(3):
            self.score *= 1 + sides[i][1] - sides[i][0]

    def overlapped(self, other):
        for i in range(3):
            if other[i][0] > self.sides[i][1] or other[i][1] < self.sides[i][0]:
                return False
        return True

    def contained(self, other):
        for i in range(3):
            if other[i][0] > self.sides[i][0] or other[i][1] < self.sides[i][1]:
                return False
        return True

    def subtracted(self, other):
        result = []
        box = [list(x) for x in self.sides]
        for i in range(3):
            if box[i][0] < other[i][0]:
                a = [list(x) for x in box]
                a[i][1] = other[i][0] - 1
                result.append(a)
                box[i][0] = other[i][0]
            if box[i][1] > other[i][1]:
                a = [list(x) for x in box]
                a[i][0] = other[i][1] + 1
                result.append(a)
                box[i][1] = other[i][1]
        return result


def operate(boxes, line):
    state, bounds = line.split(' ')
    sides = []
    for side in bounds.split(','):
        sides.append([int(x) for x in side.split('=')[1].split('..')])
    for box in boxes:
        if box.score == 0:
            continue
        if box.contained(sides):
            box.score = 0
        elif box.overlapped(sides):
            more = box.subtracted(sides)
            if len(more) > 0:
                box.update(more[0])
                for abox in more[1:]:
                    boxes.append(Box(abox))
    if state == 'on':
        boxes.append(Box(sides))


def main():
    part1 = 0
    part2 = 0
    boxes = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            operate(boxes, line.strip())

    for box in boxes:
        if box.contained([[-50, 50], [-50, 50], [-50, 50]]):
            part1 += box.score
        part2 += box.score

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
