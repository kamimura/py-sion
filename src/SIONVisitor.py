# Created by kamimura on 2018/07/21.
# Copyright © 2018 kamimura. All rights reserved.
# Generated from SION.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SIONParser import SIONParser
else:
    from SIONParser import SIONParser

import datetime


def num_rem_under(n):
    return n.replace('_', '')


def str_esc(s):
    for o, n in [('"', '\\"'), ('\n', '\\n'), ('\r', '\\r')]:
        s = s.replace(o, n)
    return s

# This class defines a complete generic visitor for a parse tree produced by SIONParser.


class SIONVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SIONParser#si_self.
    def visitSi_self(self, ctx: SIONParser.Si_selfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SIONParser#si_array.
    def visitSi_array(self, ctx: SIONParser.Si_arrayContext):
        if ctx.si_array_items():
            a = self.visit(ctx.si_array_items())
        else:
            a = []
        return a

    # Visit a parse tree produced by SIONParser#si_array_items.
    def visitSi_array_items(self, ctx: SIONParser.Si_array_itemsContext):
        result = [self.visit(t) for t in ctx.si_self()]
        return result

    # Visit a parse tree produced by SIONParser#si_dict.
    def visitSi_dict(self, ctx: SIONParser.Si_dictContext):
        if ctx.si_dict_pairs():
            d = self.visit(ctx.si_dict_pairs())
        else:
            d = {}
        return d

    # Visit a parse tree produced by SIONParser#si_dict_pairs.
    def visitSi_dict_pairs(self, ctx: SIONParser.Si_dict_pairsContext):
        kvs = [self.visit(t) for t in ctx.si_dict_pair()]
        return {k: v for k, v in kvs}

    # Visit a parse tree produced by SIONParser#si_dict_pair.
    def visitSi_dict_pair(self, ctx: SIONParser.Si_dict_pairContext):
        k, v = [self.visit(t) for t in ctx.si_self()]
        if isinstance(k, list):
            k = tuple(k)
        elif isinstance(k, dict):
            k = tuple((s, t) for s, t in k.items())
        return (k, v)

    # Visit a parse tree produced by SIONParser#si_literal.
    def visitSi_literal(self, ctx: SIONParser.Si_literalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SIONParser#si_ints.
    def visitSi_ints(self, ctx: SIONParser.Si_intsContext):
        if ctx.SI_minus():
            sign = -1
        else:
            sign = 1
        return sign * self.visitChildren(ctx)

    # Visit a parse tree produced by SIONParser#si_doubles.
    def visitSi_doubles(self, ctx: SIONParser.Si_doublesContext):
        if ctx.SI_minus():
            sign = -1
        else:
            sign = 1
        text = num_rem_under(ctx.SI_double().getText())
        if text[:2] == '0x':
            n = float.fromhex(text)
        else:
            n = float(text)
        return sign * n

    # Visit a parse tree produced by SIONParser#si_bool.
    def visitSi_bool(self, ctx: SIONParser.Si_boolContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SIONParser#si_true.
    def visitSi_true(self, ctx: SIONParser.Si_trueContext):
        return True

    # Visit a parse tree produced by SIONParser#si_false.
    def visitSi_false(self, ctx: SIONParser.Si_falseContext):
        return False

    # Visit a parse tree produced by SIONParser#si_nil.
    def visitSi_nil(self, ctx: SIONParser.Si_nilContext):
        return None

    # Visit a parse tree produced by SIONParser#si_int.
    def visitSi_int(self, ctx: SIONParser.Si_intContext):
        if ctx.SI_bin():
            n = int(num_rem_under(ctx.SI_bin().getText()), 2)
        elif ctx.SI_oct():
            n = int(num_rem_under(ctx.SI_oct().getText()), 8)
        elif ctx.SI_decimal():
            n = int(num_rem_under(ctx.SI_decimal().getText()), 10)
        elif ctx.SI_hex():
            n = int(num_rem_under(ctx.SI_hex().getText()), 16)
        return n

    # Visit a parse tree produced by SIONParser#si_data.
    def visitSi_data(self, ctx: SIONParser.Si_dataContext):
        return ctx.SI_data().getText()[7:-2].encode('ascii')

    # Visit a parse tree produced by SIONParser#si_date.
    def visitSi_date(self, ctx: SIONParser.Si_dateContext):
        if ctx.si_doubles():
            t = self.visit(ctx.si_doubles())
        else:
            t = self.visit(ctx.si_ints())
        d = datetime.datetime.fromtimestamp(t)
        return d

    # Visit a parse tree produced by SIONParser#si_string.
    def visitSi_string(self, ctx: SIONParser.Si_stringContext):
        return ctx.SI_string_literal().getText()[1:-1]


del SIONParser
