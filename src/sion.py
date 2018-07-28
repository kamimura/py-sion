# Created by kamimura on 2018/07/21.
# Copyright © 2018 kamimura. All rights reserved.
import sys
import datetime
from antlr4 import *
from SIONLexer import SIONLexer
from SIONParser import SIONParser
from SIONVisitor import SIONVisitor


def load(file) -> object:
    stream = InputStream(file.read())
    lexer = SIONLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = SIONParser(tokens)
    tree = parser.si_self()
    visitor = SIONVisitor()
    return visitor.visit(tree)


def str_esc(s):
    for o, n in [('"', '\\"'), ('\n', '\\n'), ('\r', '\\r'), ('\\', '\\\\')]:
        s = s.replace(o, n)
    return s


def dump(obj, file):
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
                dump(o, file)
                print(',', file=file, end='')
            dump(obj[-1], file)
        print(']', file=file, end='')
    elif t == dict:
        print('[', file=file, end='')
        ks = list(obj.keys())
        if len(ks) == 0:
            print(':', file=file, end='')
        elif len(ks) == 1:
            dump(ks[0], file)
            print(':', file=file, end='')
            dump(obj[ks[0]], file)
        else:
            for k in ks[:-1]:
                dump(k, file)
                print(':', file=file, end='')
                dump(obj[k], file)
                print(',', file=file, end='')
            dump(ks[-1], file)
            print(':', file=file, end='')
            dump(obj[ks[-1]], file)
        print(']', file=file, end='')
    else:
        raise TypeError(
            f"Object of type '{obj.__class__.__name__}' is not SION serializable")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = '../test/t.sion'
    with open(filename) as f:
        obj = load(f)
    print(obj)
    with open('../test/output.sion', 'w') as f:
        dump(obj, f)
