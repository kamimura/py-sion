# Created by kamimura on 2018/07/21.
# Copyright © 2018 kamimura. All rights reserved.
import sys
import datetime
from antlr4 import *
from SIONLexer import SIONLexer
from SIONParser import SIONParser
from SIONVisitor import SIONVisitor


def load(file, encoding: str='utf-8', errors: str='strict') -> object:
    data = file.read()
    if isinstance(data, (bytes, bytearray)):
        data = data.decode(encoding, errors)
    stream = InputStream(data)
    lexer = SIONLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = SIONParser(tokens)
    tree = parser.si_self()
    visitor = SIONVisitor()
    return visitor.visit(tree)


def loads(s):
    if isinstance(s, (bytes, bytearray)):
        s = s.decode()
    stream = InputStream(s)
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
    if obj is None:
        print('nil', file=file, end='')
    elif isinstance(obj, bool):
        if obj:
            print('ture', file=file, end='')
        else:
            print('false', file=file, end='')
    elif isinstance(obj, (int, float)):
        print(obj, file=file, end='')
    elif isinstance(obj, str):
        print(f'"{str_esc(obj)}"', file=file, end='')
    elif isinstance(obj, (bytes, bytearray)):
        print(f'.Data("{str(obj)[2:-1]}")', file=file, end='')
    elif isinstance(obj, datetime.datetime):
        print(f'.Date({obj.timestamp()})', file=file, end='')
    elif isinstance(obj, (list, tuple)):
        print(f'[', file=file, end='')
        if len(obj) > 0:
            for o in obj[:-1]:
                dump(o, file)
                print(',', file=file, end='')
            dump(obj[-1], file)
        print(']', file=file, end='')
    elif isinstance(obj, dict):
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


def dumps(obj: object):
    if obj is None:
        return 'nil'
    if isinstance(obj, bool):
        if obj:
            return 'true'
        return 'false'
    if isinstance(obj, (int, float)):
        return str(obj)
    if isinstance(obj, str):
        return f'"{str_esc(obj)}"'
    if isinstance(obj, (bytes, bytearray)):
        return f'.Data("{str(obj)[2:-1]}")'
    if isinstance(obj, datetime.datetime):
        return f'.Date({obj.timestamp(obj)})'
    if isinstance(obj, (list, tuple)):
        res = '['
        if len(obj) > 0:
            for o in obj[:-1]:
                res += dumps(o) + ','
            res += dumps(obj[-1])
        res += ']'
        return res
    if isinstance(obj, dict):
        res = '['
        ks = list(obj.keys())
        if len(ks) == 0:
            res += ':'
        elif len(ks) == 1:
            res += dumps(ks[0]) + ':' + dumps(obj[ks[0]])
        else:
            for k in ks[:-1]:
                res += dumps(k) + ':' + str(obj[k]) + ','
            res += dumps(ks[-1]) + ':' + dumps(obj[ks[-1]])
        res += ']'
        return res
    raise TypeError(
        f"Object of type '{obj.__class__.__name__}' is not SION serializable")


if __name__ == '__main__':
    import pprint
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = '../test/t.sion'
    with open(filename) as f:
        obj = load(f)
    pprint.pprint(obj)
    with open('../test/output.sion', 'w') as f:
        dump(obj, f)

    s = '''
[
    "array" : [
        nil,
        true,
        1,    // Int in decimal
        1.0,  // Double in decimal
        "one",
        [1],
        ["one" : 1.0]
    ],
    "bool" : true,
    "data" : .Data("R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"),
    "date" : .Date(0x0p+0),
    "dictionary" : [
        "array" : [],
        "bool" : false,
        "double" : 0x0p+0,
        "int" : 0,
        "nil" : nil,
        "object" : [:],
        "string" : ""
    ],
    "double" : 0x1.518f5c28f5c29p+5, // Double in hexadecimal
    "int" : -0x2a, // Int in hexadecimal
    "nil" : nil,
   "string" : "漢字、カタカナ、ひらがなの入ったstring😇",
    "url" : "https://github.com/dankogai/",
    nil   : "Unlike JSON and Property Lists,",
    true  : "Yes, SION",
    1     : "does accept",
    1.0   : "non-String keys.",
    []    : "like",
    [:]   : "Map of ECMAScript."
]
'''
    obj = loads(s)
    pprint.pprint(obj)
    s = dumps(obj)
    print(s)
