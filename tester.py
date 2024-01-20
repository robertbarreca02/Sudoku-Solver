import unittest
import solver
import numpy as np


class tester(unittest.TestCase):
    """
    This class tests the functionality of solver.py
    """

    def test_is_possible(self):
        """
        test_is_possible tests the functionality of the is_possible function in solver.py
        """
        solver.board = np.array(
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
        # case 1: check when insert is possible
        self.assertTrue(solver.is_possible(0, 0, 2))
        # case 2: check if insert not possible due to row
        self.assertFalse(solver.is_possible(0, 0, 1))
        # case 3: check if insert not possible due to col
        self.assertFalse(solver.is_possible(0, 0, 4))
        # case 4: check if insert not possible due to box
        self.assertFalse(solver.is_possible(0, 0, 5))

    def test_solve(self):
        """
        test_solve tests the functionality of the solve function solver.py
        """
        # case 1: test an easy board
        solver.board = np.array(
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
        self.assertTrue(solver.solve())

        # case 2 solve a medium board
        solver.board = np.array(
            [
                [0, 0, 0, 0, 2, 7, 0, 4, 1],
                [1, 0, 0, 0, 0, 0, 8, 0, 0],
                [0, 4, 0, 1, 0, 0, 0, 0, 5],
                [6, 0, 1, 0, 3, 0, 0, 9, 0],
                [0, 0, 5, 4, 8, 0, 0, 0, 0],
                [0, 3, 4, 7, 6, 1, 0, 0, 2],
                [5, 0, 7, 0, 0, 4, 0, 0, 8],
                [4, 0, 0, 0, 5, 8, 0, 0, 7],
                [8, 1, 2, 0, 0, 3, 0, 0, 6],
            ]
        )
        self.assertTrue(solver.solve())

        # case 3 solve a hard board
        solver.board = np.array(
            [
                [0, 0, 0, 0, 7, 0, 6, 1, 2],
                [6, 0, 0, 0, 2, 0, 0, 0, 8],
                [0, 0, 1, 0, 0, 0, 0, 3, 0],
                [0, 0, 0, 0, 0, 0, 8, 7, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 6, 5],
                [4, 0, 0, 0, 8, 0, 0, 0, 0],
                [0, 0, 8, 0, 0, 0, 0, 0, 6],
                [9, 0, 0, 0, 4, 0, 0, 0, 0],
            ]
        )
        self.assertTrue(solver.solve())
