
# config.py


class Config(object):

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c
        self.print_attr()

    def print_attr(self):
        print self.a, self.b, self.c


# test_config.py

import unittest
from mock import patch

from config import Config

class TestConfig(unittest.TestCase):

    def test_download(self):
        with patch.object(Config, '__init__', lambda a, b, c: None):
            c = Config()
            c.a = 1
            c.b = 2
            c.c = 3
            self.assertEqual(c.print_attr(), "1, 2, 3")