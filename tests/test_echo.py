#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo


# Your test case class goes here

class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_no_options(self):
        args = ["HeLlo WorLD"]
        ns = self.parser.parse_args(args)
        self.assertFalse(ns.upper)
        self.assertFalse(ns.lower)
        self.assertFalse(ns.title)
        actual = echo.main(args)
        expected = args[0]
        self.assertEqual(actual, expected)

    def test_all_options(self):
        args = ['-tul', "HeLlo WorLD"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_lower_short(self):
        args = ['-l', "HeLlo world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_upper_short(self):
        args = ['-u', 'hello world']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ['-t', "HeLlO WoRlD"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        args = ['--upper', "hello world"]
        actual = echo.main(args)
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_long(self):
        args = ['--lower', 'Hello world']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_long(self):
        args = ['--title', 'HeLlO world']
        actual = echo.main(args)
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        expected = "Hello World"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
