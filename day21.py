#!/usr/bin/env python3

import sys


def part1(pos):
    score = [0, 0]
    die = 0
    rolls = 0

    while True:
        for player in range(2):
            move = 0
            for i in range(3):
                die = (die + 1) % 100
                move += die
            rolls += 3
            pos[player] = (pos[player] + move - 1) % 10 + 1
            score[player] += pos[player]
            if score[player] >= 1000:
                return score[1 - player] * rolls


def part2(pos, score, active):
    rolls = [1, 3, 6, 7, 6, 3, 1]
    win = [[1, 0], [0, 1]]
    player = 1 - active
    result = [0, 0]

    if score[active] >= 21:
        return win[active]

    for i in range(7):
        npos = list(pos)
        nscore = list(score)
        npos[player] = (npos[player] + i + 2) % 10 + 1
        nscore[player] += npos[player]
        bump = part2(npos, nscore, player)
        for j in range(2):
            result[j] += rolls[i] * bump[j]

    return result


def main():
    pos = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            pos.append(int(line.strip().split(' ')[-1]))
    print("Part 1:", part1(list(pos)))
    print("Part 2:", max(part2(list(pos), [0, 0], 1)))


if __name__ == '__main__':
    main()
