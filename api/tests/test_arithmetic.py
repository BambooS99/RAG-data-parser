import unittest

from api.solvers.arithmetic import add


class TestAdd(unittest.TestCase):
    def test_adds_integers(self):
        self.assertEqual(add([1, 2, 3, 4]), 10)

    def test_adds_integers_and_decimals(self):
        self.assertEqual(add([2.5, 1.25]), 3.75)

    def test_empty_list_returns_zero(self):
        self.assertEqual(add([]), 0)


if __name__ == "__main__":
    unittest.main()
