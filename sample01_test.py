# -* encoding: utf-8 *-

import unittest

from sample01 import get_hello

class TestHello(unittest.TestCase):
    """ test class of Hello
    """

    def test_hello(self):
        s = get_hello()

        self.assertEqual(s, "hello, world!")


if __name__ == "__main__":
    unittest.main()
