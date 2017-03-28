import unittest

from lecture_code.testing.wrap_around_counter.wraparoundcounter import WrapAroundCounter


class SimpleTest(unittest.TestCase):

    def test_pass(self):
        wac = WrapAroundCounter(10)

        with self.assertRaises(ValueError):
            wac.increment(0)

        with self.assertRaises(ValueError):
            wac.increment(11)

        self.assertEqual(wac.increment(1), 2)
        self.assertEqual(wac.increment(9), 10)
        self.assertEqual(wac.increment(10), 1)

