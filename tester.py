import unittest
import solver
import numpy as np


class tester(unittest.TestCase):
    """
    This class tests the functionality of solver.py
    """

    def test_is_possible(self):
        board = np.array(
            [
                [0, 0, 6, 3, 9, 0, 8, 0, 1],
                [0, 8, 9, 0, 7, 0, 5, 3, 0],
                [3, 5, 0, 8, 0, 0, 9, 6, 0],
                [0, 0, 0, 6, 0, 8, 0, 2, 3],
                [8, 0, 1, 0, 3, 4, 0, 0, 0],
                [4, 0, 3, 0, 0, 0, 6, 0, 8],
                [6, 0, 0, 0, 0, 9, 3, 8, 0],
                [0, 3, 0, 7, 8, 2, 0, 9, 0],
                [0, 7, 0, 0, 0, 3, 0, 0, 0],
            ]
        )

        # check when insert is possible
        self.assertTrue(solver.is_possible(0, 0, 2))
        # check if insert not possible due to row
        self.assertFalse(solver.is_possible(0, 0, 1))
        # check if insert not possible due to col
        self.assertFalse(solver.is_possible(0, 0, 4))
        # check if insert not possible due to box
        self.assertFalse(solver.is_possible(0, 0, 5))
