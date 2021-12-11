#!/usr/bin/env python3

import sys


def step(grid, i, j):
    grid[i][j] += 1

    if grid[i][j] == 10:
        if i > 0:
            step(grid, i - 1, j)
            if j > 0:
                step(grid, i - 1, j - 1)
            if j < 9:
                step(grid, i - 1, j + 1)
        if i < 9:
            step(grid, i + 1, j)
            if j > 0:
                step(grid, i + 1, j - 1)
            if j < 9:
                step(grid, i + 1, j + 1)
        if j > 0:
            step(grid, i, j - 1)
        if j < 9:
            step(grid, i, j + 1)


def generation(grid):
    flash = 0
    for i in range(10):
        for j in range(10):
            step(grid, i, j)
    for i in range(10):
        for j in range(10):
            if grid[i][j] > 9:
                grid[i][j] = 0
                flash += 1
    return flash


def main():
    grid = []
    part1 = 0
    part2 = 0
    step = 0
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            grid.append([int(x) for x in line.strip()])
    while(step != 100):
        part2 += 1
        step = generation(grid)
        part1 += step
        if part2 == 100:
            print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
