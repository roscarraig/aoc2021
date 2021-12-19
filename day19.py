#!/usr/bin/env python3

import sys

TRANSFORMS = []


def translate(beacons, x, y, z):
    return [[item[0] + x, item[1] + y, item[2] + z] for item in beacons]


class Scanner(object):
    def __init__(self, name):
        self._name = name
        self._beacons = []
        self.done = False
        self.rel = None

    def add_beacon(self, line):
        self._beacons.append([int(x) for x in line.split(',')])

    def transform(self, num):
        if num == 0:
            return self._beacons

        base = TRANSFORMS[num]
        signs = [int(base[x] / abs(base[x])) for x in range(3)]
        base = [abs(x) - 1 for x in base]

        return [[signs[i] * x[base[i]] for i in range(3)] for x in self._beacons]

    def match_scan(self, candidate):
        candlen = len(candidate) - 11

        for i in range(len(self._beacons) - 11):
            for j in range(candlen):
                x = self._beacons[i][0] - candidate[j][0]
                y = self._beacons[i][1] - candidate[j][1]
                z = self._beacons[i][2] - candidate[j][2]
                b = len([a for a in translate(candidate, x, y, z) if a in self._beacons])
                if b >= 12:
                    return([x, y, z])

    def merge(self, candidate, offset):
        for item in translate(candidate, offset[0], offset[1], offset[2]):
            if item not in self._beacons:
                self._beacons.append(item)


def main():
    active = None
    scanners = []
    count = 0

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            if '---' in line:
                active = Scanner(line.split(' ')[2])
            elif ',' in line:
                active.add_beacon(line.strip())
            else:
                scanners.append(active)
                count += 1
                active = None
    if active:
        scanners.append(active)
        count += 1

    for base in [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 3, 2], [3, 2, 1], [2, 1, 3]]:
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                for k in range(-1, 2, 2):
                    TRANSFORMS.append([base[0] * i, base[1] * j, base[2] * k])

    while(len([x for x in scanners if x.done is False]) > 1):
        for i in range(count):
            match = True
            while match:
                match = False
                for j in range(i + 1, count):
                    if scanners[j].done:
                        continue
                    for k in range(len(TRANSFORMS)):
                        tra = scanners[j].transform(k)
                        res = scanners[i].match_scan(tra)

                        if res:
                            scanners[i].merge(tra, res)
                            scanners[j].done = True
                            scanners[j].rel = res
                            match = True
                            break
    print("Part 1:", len(scanners[0]._beacons))
    scanners[0].rel = [0, 0, 0]
    part2 = 0
    for i in range(len(scanners) - 1):
        a = scanners[i].rel
        for j in range(i + 1, len(scanners)):
            b = scanners[j].rel
            part2 = max(abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]), part2)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
