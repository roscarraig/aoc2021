#!/usr/bin/env python3

import sys


class Card(object):
    def __init__(self, filehandle):
        self.lines = []
        self.marked = []
        self.done = False
        for _ in range(5):
            line = filehandle.readline().strip("\n")
            self.lines.append([int(line[x * 3:x * 3 + 2]) for x in range(5)])

    def __str__(self):
        result = []
        for i in range(5):
            result.append(str(self.lines[i]))
        return '\n'.join(result)

    def __repr__(self):
        result = []
        for i in range(5):
            result.append(str(self.lines[i]))
        return '\n'.join(result)

    def mark(self, num):
        for i in range(5):
            for j in range(5):
                if self.lines[i][j] == num:
                    self.marked.append(num)
        if num in self.marked:
            return self.wins()
        return False

    def wins(self):
        for i in range(5):
            match = True
            for j in range(5):
                if self.lines[i][j] not in self.marked:
                    match = False
                    continue
            if match:
                return True
        for i in range(5):
            match = True
            for j in range(5):
                if self.lines[j][i] not in self.marked:
                    match = False
                    continue
            if match:
                return True
        return False

    @property
    def score(self):
        total = 0
        for i in range(5):
            for j in range(5):
                if self.lines[i][j] not in self.marked:
                    total += self.lines[i][j]
        self.done = True
        return total * self.marked[-1]


def main():
    with open(sys.argv[1], 'r') as fhan:
        calls = [int(x) for x in fhan.readline().strip('\n').split(',')]
        cards = []
        while fhan.readline():
            cards.append(Card(fhan))
    for num in calls:
        for card in cards:
            if not card.done:
                if card.mark(num):
                    print(card)
                    print(card.score)


if __name__ == '__main__':
    main()
