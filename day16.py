#!/usr/bin/env python3

import sys


def hextobits(char):
    result = ''
    val = '0123456789ABCDEF'.index(char)
    for i in range(4):
        result += '01'[val % 2]
        val >>= 1
    return result[-1::-1]


def bitstodec(data):
    result = 0
    for i in range(len(data)):
        result *= 2
        result += '01'.index(data[i])
    return result


class BitStream(object):
    def __init__(self, hexstring='', bitstring=''):
        self.hexstring = hexstring
        self.bits = bitstring

    def getbits(self, count):
        while(len(self.bits) < count):
            self.bits += hextobits(self.hexstring[0])
            self.hexstring = self.hexstring[1:]
        result = self.bits[0:count]
        self.bits = self.bits[count:]
        return result

    def read_packet(self):
        result = {}
        result['version'] = bitstodec(self.getbits(3))
        ptype = bitstodec(self.getbits(3))
        result['type'] = ptype

        if ptype == 4:
            value = 0
            while(self.getbits(1) == '1'):
                value *= 16
                value += bitstodec(self.getbits(4))
            value *= 16
            value += bitstodec(self.getbits(4))
            result['value'] = value
        else:
            result['sub'] = []
            if self.getbits(1) == '0':
                plens = self.getbits(15)
                plen = 0
                for i in range(15):
                    plen *= 2
                    if plens[i] == '1':
                        plen += 1
                substream = BitStream(bitstring=self.getbits(plen))
                while(not substream.eod):
                    result['sub'].append(substream.read_packet())
            else:
                pcounts = bitstodec(self.getbits(11))
                for i in range(pcounts):
                    result['sub'].append(self.read_packet())

        return result

    @property
    def eod(self):
        return len(self.hexstring + self.bits) == 0


def operate(packet):
    t = packet['type']
    if t == 4:
        return packet['value']

    if t == 0:
        result = 0
        for item in packet['sub']:
            result += operate(item)
        return result

    if t == 1:
        result = 1
        for item in packet['sub']:
            result *= operate(item)
        return result

    if t == 2:
        result = []
        for item in packet['sub']:
            result.append(operate(item))
        return min(result)

    if t == 3:
        result = []
        for item in packet['sub']:
            result.append(operate(item))
        return max(result)

    a = operate(packet['sub'][0])
    b = operate(packet['sub'][1])

    if t == 5:
        if a > b:
            return 1
        return 0

    if t == 6:
        if a < b:
            return 1
        return 0

    if a == b:
        return 1
    return 0


def version_total(packet):
    total = packet['version']
    if 'sub' in packet:
        for item in packet['sub']:
            total += version_total(item)
    return total


def main():
    with open(sys.argv[1], 'r') as fhan:
        line = fhan.readline().strip()
    bitstream = BitStream(line)
    packet = bitstream.read_packet()
    print("Part 1:", version_total(packet))
    print("Part 2:", operate(packet))


if __name__ == '__main__':
    main()
