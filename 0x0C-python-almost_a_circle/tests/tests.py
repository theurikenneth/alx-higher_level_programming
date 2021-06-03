#!/usr/bin/python3
"""Unitest module from Base, Square and Rectangle classes"""
import unitest
import json
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


idct = 0
nonintegers = [3.5, [], {}, {1, 2}, {1: 2, 3: 4}, "hi", b"hi", ()]

class TestBase(unittest.TestCase):
    """Test cases for Base geometry class"""

    def testdefault(self):
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)

    def testincrement(self):
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)
        b = Base()
        idct += 1
        self.assertEqual(b.id, idct)
        c = Base()
        idct += 1
        self.assertEqual(c.id, idct)
        d = Base()
        idct += 1
        self.assertEqual(d.id, idct)

    def testspecific(self):
        global idct
        a = Base(19)
        self.assertEqual(a.id, 19)

    def testspecincrement(self):
        """Tests that setting a specific id does not mess up incrementer"""
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)
        b = Base(19)
        self.assertEqual(b.id, 19)
        c = Base()
        idct += 1
        self.assertEqual(c.id, idct)
        d = Base()
        idct += 1
        self.assertEqual(d.id, idct)
