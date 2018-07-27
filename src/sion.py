#!/usr/bin/env python3
# Created by kamimura on 2018/07/21.
# Copyright © 2018 kamimura. All rights reserved.

import sys
from antlr4 import *
from SIONLexer import SIONLexer
from SIONParser import SIONParser
from SIONVisitor import SIONVisitor

import datetime


def load(filename: str, encoding='utf-8') -> object:
    fs = FileStream(filename, encoding='utf-8')
    lexer = SIONLexer(fs)
    tokens = CommonTokenStream(lexer)
    parser = SIONParser(tokens)
    # tree = parser.si_self()
    tree = parser.si_self()
    visitor = SIONVisitor()
    return visitor.visit(tree)


def str_esc(s):
    for o, n in [('"', '\\"'), ('\n', '\\n'), ('\r', '\\r'), ('\\', '\\\\')]:
        s = s.replace(o, n)
    return s


def dump_file(obj, file):
    t = type(obj)
    if obj is None:
        print('nil', file=file, end='')
    elif t == bool:
        if obj:
            print('ture', file=file, end='')
        else:
            print('false', file=file, end='')
    elif t in {int, float}:
        print(obj, file=file, end='')
    elif t == str:
        print(f'"{str_esc(obj)}"', file=file, end='')
    elif t == bytes:
        print(f'.Data("{str(obj)[2:-1]}")', file=file, end='')
    elif t == datetime.datetime:
        print(f'.Date({t.timestamp(obj)})', file=file, end='')
    elif t in {list, tuple}:
        print(f'[', file=file, end='')
        if len(obj) > 0:
            for o in obj[:-1]:
                dump_file(o, file)
                print(',', file=file, end='')
            dump_file(obj[-1], file)
        print(']', file=file, end='')
    elif t == dict:
        print('[', file=file, end='')
        ks = list(obj.keys())
        if len(ks) == 0:
            print(':', file=file, end='')
        elif len(ks) == 1:
            dump_file(ks[0], file)
            print(':', file=file, end='')
            dump_file(obj[ks[0]], file)
        else:
            for k in ks[:-1]:
                dump_file(k, file)
                print(':', file=file, end='')
                dump_file(obj[k], file)
                print(',', file=file, end='')
            dump_file(ks[-1], file)
            print(':', file=file, end='')
            dump_file(obj[ks[-1]], file)
        print(']', file=file, end='')


def dump(obj, filename):
    with open(filename, 'w') as file:
        dump_file(obj, file)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = '../test/t.sion'
    obj = load(filename)
    print(obj)
    dump(obj, '../test/output.sion')
