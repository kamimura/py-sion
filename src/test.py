#!/usr/bin/env python3
# Copyright © 2018 kamimura. All rights reserved.
import unittest
from sion import loads


class LoadsDictTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list_keys(self):
        a = loads('[[]:nil, [nil]: nil, [nil, true]: false]')
        b = {(): None, (None,): None, (None, True): False}
        self.assertEqual(a, b)

    def test_dict_keys(self):
        a = loads('[[:]:nil, [true:nil]:nil, [true:nil, false:nil]:nil]')
        b = {(): None, ((True, None),): None,
             ((True, None), (False, None)): None}
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
