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
        solver.solve()
        self.assertTrue(solver.validate())

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
        solver.solve()
        self.assertTrue(solver.validate())

        # case 3 solve a hard board
        solver.board = np.array(
            [
                [0, 0, 0, 0, 7, 0, 6, 0, 0],
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [3, 0, 0, 0, 0, 0, 7, 0, 0],
                [0, 8, 0, 7, 0, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 6, 0, 0, 3, 0, 5],
                [0, 0, 6, 3, 0, 0, 8, 0, 0],
                [0, 3, 0, 5, 0, 0, 2, 0, 6],
            ]
        )
        solver.solve()
        self.assertTrue(solver.validate())

        # case 4: test an unsolvable board
        solver.board = np.array(
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 8],
            ]
        )
        self.assertFalse(solver.solve())

        # case 5: test a board that's solved incorrectly
        solver.board = [
            [2, 3, 9, 6, 1, 7, 4, 8, 5],
            [1, 4, 6, 5, 8, 9, 2, 3, 7],
            [5, 7, 8, 3, 2, 4, 6, 1, 9],
            [8, 9, 2, 7, 5, 6, 3, 4, 1],
            [4, 6, 1, 2, 9, 3, 1, 7, 8],
            [7, 5, 3, 1, 4, 8, 9, 6, 2],
            [6, 8, 5, 9, 3, 1, 7, 2, 4],
            [3, 2, 4, 8, 7, 5, 1, 9, 6],
            [9, 1, 7, 4, 6, 2, 8, 5, 3],
        ]
        self.assertFalse(solver.solve())

    def test_validate(self):
        """
        test the functionality of the validate function in solver.py
        """
        # case 1: valid completed sudoku board
        solver.board = [
            [2, 3, 9, 6, 1, 7, 4, 8, 5],
            [1, 4, 6, 5, 8, 9, 2, 3, 7],
            [5, 7, 8, 3, 2, 4, 6, 1, 9],
            [8, 9, 2, 7, 5, 6, 3, 4, 1],
            [4, 6, 1, 2, 9, 3, 5, 7, 8],
            [7, 5, 3, 1, 4, 8, 9, 6, 2],
            [6, 8, 5, 9, 3, 1, 7, 2, 4],
            [3, 2, 4, 8, 7, 5, 1, 9, 6],
            [9, 1, 7, 4, 6, 2, 8, 5, 3],
        ]
        self.assertTrue(solver.validate())

        # case 2: invalid completed sudoku board
        solver.board = [
            [2, 3, 9, 6, 1, 7, 4, 8, 5],
            [1, 4, 6, 5, 8, 9, 2, 3, 7],
            [5, 7, 8, 3, 2, 4, 6, 1, 9],
            [8, 9, 2, 7, 5, 6, 3, 4, 1],
            [4, 6, 1, 2, 9, 3, 1, 7, 8],
            [7, 5, 3, 1, 4, 8, 9, 6, 2],
            [6, 8, 5, 9, 3, 1, 7, 2, 4],
            [3, 2, 4, 8, 7, 5, 1, 9, 6],
            [9, 1, 7, 4, 6, 2, 8, 5, 3],
        ]
        self.assertFalse(solver.validate())

        # case 3: test incomplete valid sudoku board
        solver.board = [
            [2, 3, 0, 6, 0, 5, 8, 7, 0],
            [6, 9, 7, 0, 0, 0, 5, 0, 1],
            [8, 1, 0, 0, 4, 0, 2, 3, 0],
            [9, 6, 3, 8, 2, 4, 0, 0, 0],
            [5, 7, 1, 3, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 0, 0, 0, 0, 3],
            [3, 5, 8, 0, 6, 2, 0, 0, 0],
            [1, 0, 6, 0, 0, 0, 0, 0, 5],
            [0, 0, 9, 0, 5, 8, 0, 6, 0],
        ]
        self.assertTrue(solver.validate())

        # case 4: incomplete invalid sudoku board bc of row
        solver.board = np.array(
            [
                [1, 0, 6, 3, 9, 0, 8, 0, 1],
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
        self.assertFalse(solver.validate())

        # case 5: incomplete invalid sudoku board bc of col
        solver.board = np.array(
            [
                [4, 0, 6, 3, 9, 0, 8, 0, 1],
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
        self.assertFalse(solver.validate())

        # case 6: incomplete invalid sudoku board bc of box
        solver.board = np.array(
            [
                [5, 0, 6, 3, 9, 0, 8, 0, 1],
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
        self.assertFalse(solver.validate())
