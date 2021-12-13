#!/usr/bin/env python3

import sys


def foldx(x, paper):
    for i in range(len(paper)):
        xy = [int(a) for a in paper[i].split(',')]
        if xy[0] < x:
            continue
        paper[i] = "{0},{1}".format(2 * x - xy[0], xy[1])
    return list(set(paper))


def foldy(y, paper):
    for i in range(len(paper)):
        xy = [int(a) for a in paper[i].split(',')]
        if xy[1] < y:
            continue
        paper[i] = "{0},{1}".format(xy[0], 2 * y - xy[1])
    return list(set(paper))


def main():
    paper = []
    phase = 0

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            if phase == 0:
                if ',' in line:
                    paper.append(line.strip())
                else:
                    phase = 1
            elif phase == 1:
                instr = line.strip().split('=')
                if instr[0] == 'fold along x':
                    paper = foldx(int(instr[1]), paper)
                    phase = 2
                    print("Part 1:", len(set(paper)))
                else:
                    paper = foldy(int(instr[1]), paper)
                    phase = 2
                    print("Part 1:", len(set(paper)))
            else:
                instr = line.strip().split('=')
                if instr[0] == 'fold along x':
                    paper = foldx(int(instr[1]), paper)
                else:
                    paper = foldy(int(instr[1]), paper)
    mx = max([int(item.split(',')[0]) for item in paper])
    my = max([int(item.split(',')[1]) for item in paper])
    readout = [" " * (mx + 1)] * (my + 1)
    for item in paper:
        xy = [int(a) for a in item.split(',')]
        line = readout[xy[1]]
        readout[xy[1]] = line[0:xy[0]] + '#' + line[(xy[0] + 1):]
    print("Part 2:")
    for item in readout:
        print(item)


if __name__ == '__main__':
    main()
