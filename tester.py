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

        # case 1: check when insert is possible
        self.assertTrue(solver.test_is_possible(0, 0, 2, board))
        # case 2: check if insert not possible due to row
        self.assertFalse(solver.test_is_possible(0, 0, 1, board))
        # case 3: check if insert not possible due to col
        self.assertFalse(solver.test_is_possible(0, 0, 4, board))
        # case 4: check if insert not possible due to box
        self.assertFalse(solver.test_is_possible(0, 0, 5, board))

    def test_solve(self):
        """
        test_solve tests the functionality of the solve function solver.py
        """
        # case 1: test an easy board
        preset_board = np.array(
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
        solved_board = np.array(
            [
                [2, 4, 6, 3, 9, 5, 8, 7, 1],
                [1, 8, 9, 4, 7, 6, 5, 3, 2],
                [3, 5, 7, 8, 2, 1, 9, 6, 4],
                [7, 9, 5, 6, 1, 8, 4, 2, 3],
                [8, 6, 1, 2, 3, 4, 7, 5, 9],
                [4, 2, 3, 9, 5, 7, 6, 1, 8],
                [6, 1, 2, 5, 4, 9, 3, 8, 7],
                [5, 3, 4, 7, 8, 2, 1, 9, 6],
                [9, 7, 8, 1, 6, 3, 2, 4, 5],
            ]
        )

        self.assertTrue(np.array_equal(solver.test_solve(preset_board), solved_board))
