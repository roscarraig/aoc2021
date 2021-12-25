#!/usr/bin/env python3

import sys


def charsub(line, ind, val):
    return line[:ind] + val + line[ind + 1:]


def print_map(sea):
    for line in sea:
        print(line)


def step(sea):
    moved = False
    newsea = []
    ls = len(sea)

    for i in range(ls):
        newsea.append(sea[i])
        ll = len(sea[i])

        for j in range(ll):
            if sea[i][j] == '>' and sea[i][(j + 1) % ll] == '.':
                moved = True
                newsea[i] = charsub(newsea[i], j, '.')
                newsea[i] = charsub(newsea[i], (j + 1) % ll, '>')

        sea[i] = newsea[i]

    for i in range(ls):
        for j in range(len(sea[i])):
            if sea[i][j] == 'v' and sea[(i + 1) % ls][j] == '.':
                moved = True
                newsea[i] = charsub(newsea[i], j, '.')
                newsea[(i + 1) % ls] = charsub(newsea[(i + 1) % ls], j, 'v')

    for i in range(ls):
        sea[i] = newsea[i]

    return moved


def main():
    sea = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            sea.append(line.strip("\n"))
    i = 1
    while step(sea):
        i += 1
    print("Part 1:", i)


if __name__ == '__main__':
    main()
