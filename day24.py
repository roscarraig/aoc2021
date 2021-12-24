#!/usr/bin/env python3

import re
import sys


def run(prog, ival):

    vars = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    val = [int(x) for x in ival]
    for line in prog:
        parts = line.split(' ')

        if parts[0] == 'inp':
            vars[parts[1]] = val.pop(0)
            continue

        cmd = parts[0]
        a = parts[1]
        if parts[2] in vars:
            b = vars[parts[2]]
        else:
            b = int(parts[2])
        if cmd == 'add':
            vars[a] += b
        elif cmd == 'mul':
            vars[a] *= b
        elif cmd == 'div':
            vars[a] = int(vars[a] / b)
        elif cmd == 'mod':
            vars[a] %= b
        elif cmd == 'eql':
            if vars[a] == b:
                vars[a] = 1
            else:
                vars[a] = 0
    return vars['z'] == 0


def reduce(expr):
    more = True
    while more:
        more = False
        mat = re.search(r'(\(\([a-n0-9]+\+[a-n0-9]+\)\+[a-n0-9]+\))', expr)

        if mat:
            more = True
            found = mat.group(1)
            fixed = '(' + mat.group(1).replace('(', '').replace(')', '') + ')'
            expr = expr.replace(found, fixed)

        mat = re.search(r'\((\d+)\+(\d+)\)', expr)

        if mat:
            more = True
            found = '(' + mat.group(1) + '+' + mat.group(2) + ')'
            fixed = str(int(mat.group(1)) + int(mat.group(2)))
            expr = expr.replace(found, fixed)

        mat = re.search(r'(\(\([a-n]\+\d\d\)==[a-n]\?1:0\))', expr)

        if mat:
            more = True
            found = mat.group(1)
            expr = expr.replace(found, '0')

        mat = re.search(r'(\([\da-n]+\))', expr)

        if mat:
            more = True
            found = mat.group(1)
            fixed = found.replace('(', '').replace(')', '')
            expr = expr.replace(found, fixed)
        mat = re.search(r'(\+\([a-n\d]+\+[a-n\d]+\))', expr)
        if mat:
            more = True
            found = mat.group(1)
            fixed = found.replace('(', '').replace(')', '')
            expr = expr.replace(found, fixed)

        mat = re.search(r'(\+\d\d+\)==[a-n]\?1:0\))', expr)
        if mat:
            more = True
            i = mat.start(0)
            j = mat.end(0)
            d = 2
            while d > 0:
                i -= 1
                if expr[i] == '(':
                    d -= 1
                elif expr[i] == ')':
                    d += 1
            found = expr[i:j]
            expr = expr.replace(found, '0')
        mat = re.search(r'\(([a-n])\+(\d+)\)-(\d+)', expr)
        if mat:
            found = '(' + mat.group(1) + '+' + mat.group(2) + ')-' + mat.group(3)
            fixed = mat.group(1) + '+' + str(int(mat.group(2)) - int(mat.group(3)))
            expr = expr.replace(found, fixed)
            more = True

        if '+-' in expr:
            more = True
            expr = expr.replace('+-', '-')
        mat = re.search(r'(\(\(\([a-z\d]+\+[a-z\d]+\)\*\d+\)\+[a-z0-9]+\+[a-z\d]+\)%\d+)', expr)
        if mat:
            found = mat.group(1)
            mat2 = re.search(r"\((\(\([a-z\d]+\+[a-z\d]+\)\*)(\d+)\)\+[a-z0-9]+\+[a-z\d]+\)%(\d+)", expr)
            if mat2.group(2) == mat2.group(3):
                more = True
                fixed = found.replace(mat2.group(1) + mat2.group(2) + ')+', '')
                expr = expr.replace(found, fixed)

    return expr


def modreduce(left, right):
    mat = re.search(r'\((\([a-n\d]+\+[a-n\d]+\)\*)(\d+)+', left)
    if mat and mat.group(2) == right:
        left = left.replace(mat.group(1) + mat.group(2) + '+', '')
    if re.match(r'^\([a-n]\+\d\)$', left):
        return left
    if left.find('*' + right):
        depth = 0
        spotting = ')*' + right
        i = len(left) - 1
        while i > 0:
            if left[i] == ')':
                depth += 1
            elif left[i] == '(':
                depth -= 1
            elif depth == 1 and left[i] == '+' and left[i - len(spotting):i] == spotting:
                last = i + 1
                i -= len(spotting)
                depth += 1
                while(depth > 1):
                    i -= 1
                    if left[i] == '(':
                        depth -= 1
                    elif left[i] == ')':
                        depth += 1
                left = left.replace(left[i:last], '')
            i -= 1
    mat = re.match(r'^\([a-n]\+(\d+)\)$', left)
    if mat and int(mat.group(1)) + 9 < int(right):
        return left
    if len(left) == 1 and int(right) > 9:
        return left
    if re.match(r'\([a-n0-9]\)', left) and int(right) > 9:
        return left[1]
    return '{0}%{1}'.format(left, right)


def add_bounds(bounds, left, right):
    if left[2] == '+':
        bounds[left[1]] = [1, 9 - int(left[3])]
        bounds[right] = [1 + int(left[3]), 9]
    else:
        bounds[right] = [1, 9 - int(left[3])]
        bounds[left[1]] = [1 + int(left[3]), 9]


def run2(prog, ival, bounds):
    vars = {
        'w': '0',
        'x': '0',
        'y': '0',
        'z': '0'
    }
    val = [x for x in ival]
    for line in prog:
        parts = line.split(' ')

        if parts[0] == 'inp':
            vars[parts[1]] = val.pop(0)
            continue

        cmd = parts[0]
        a = parts[1]
        if parts[2] in vars:
            b = vars[parts[2]]
        else:
            b = parts[2]

        if cmd == 'add':
            if b == '0':
                continue
            if vars[a] == '0':
                vars[a] = b
            else:
                vars[a] = '({0}+{1})'.format(vars[a], b)
        elif cmd == 'mul':
            if vars[a] == '0' or b == '1':
                continue
            if b == '0':
                vars[a] = '0'
            else:
                vars[a] = '{0}*{1}'.format(vars[a], b)
        elif cmd == 'div':
            if vars[a] == '0' or b == '1':
                continue
            mat = re.search(r'^\((\(.*\))\*26\+[a-n]\+(\d+)\)$', vars[a])
            if mat and int(mat.group(2)) + 9 < int(b):
                vars[a] = mat.group(1)
                continue
            mat = re.search(r'^\((\(.*\))\*26\+[a-n]\)$', vars[a])
            if mat and 9 < int(b):
                vars[a] = mat.group(1)
                continue
            vars[a] = '({0}/{1})'.format(vars[a], b)
        elif cmd == 'mod':
            if vars[a] == '0':
                continue
            if vars[a] in 'abcdefghijklmn' and int(b) > 9:
                continue
            if vars[a] == '(a+1)' and b == '26':
                continue
            vars[a] = modreduce(vars[a], b)
        elif cmd == 'eql':
            if vars[a] == '0' and b == '0':
                vars[a] = '1'
            elif vars[a] == '1' and b == '0':
                vars[a] = '0'
            elif vars[a] == '0' and b == '1':
                vars[a] = '0'
            elif vars[a] == b:
                vars[a] = '1'
            elif b in 'abcdefghijklmn' and vars[a][0] in '0123456789' and len(vars[a]) > 1:
                vars[a] = '0'
            elif b in 'abcdefghijklmn' and re.match(r'\([a-n][\+\-]\d\)', vars[a]):
                add_bounds(bounds, vars[a], b)
                vars[a] = '1'
            else:
                vars[a] = '({0}=={1}?1:0)'.format(vars[a], b)
        for item in vars:
            vars[item] = reduce(vars[item])
    return vars


def main():
    prog = []
    bounds = {}
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            prog.append(line.strip("\n"))

    vname = 'abcdefghijklmn'
    run2(prog, vname, bounds)
    part1 = ''.join([str(bounds[x][1]) for x in vname])
    if run(prog, part1):
        print("Part1:", part1)
    part2 = ''.join([str(bounds[x][0]) for x in vname])
    if run(prog, part2):
        print("Part2:", part2)


if __name__ == '__main__':
    main()
