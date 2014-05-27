# coding: utf-8
from twisted.trial import unittest


class ExampleTestCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1+1, 2)
