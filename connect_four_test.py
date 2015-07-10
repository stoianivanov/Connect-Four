import unittest
from connect_four import Table


class TableTest(unittest.TestCase):

    def setUp(self):
        self.table = Table()

    def test_col_is_full(self):
        matrix = [
            ["E", "E", "E", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
        ]
        self.table.matrix = matrix
        self.assertTrue(self.table.col_is_full(2))

    def test_col_is_not_full(self):
        matrix = [
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
        ]
        self.table.matrix = matrix
        self.assertFalse(self.table.col_is_full(2))

    def test_get_matrix(self):
        matrix = [
            ["E", "E"],
            ["E", "E"],
        ]
        self.table.matrix = matrix
        self.assertEqual(self.table.get_matrix(), matrix)

    def test_has_winner(self):
        matrix = [
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
        ]
        self.table.matrix = matrix
        self.assertTrue(self.table.has_winner())

    def test_has_winner_with_no_winner(self):
        matrix = [
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "E", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
        ]
        self.table.matrix = matrix
        self.assertFalse(self.table.has_winner())

    def test_get_winner(self):
        matrix = [
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
            ["E", "E", "R", "E", "E"],
        ]
        self.table.matrix = matrix
        self.assertEqual(self.table.get_winner(), "R")

    def test_get_free_position(self):
        matrix = [
            ["B", "E", "R", "E", "E"],
            ["R", "R", "R", "E", "E"],
            ["R", "R", "R", "E", "E"],
            ["B", "R", "R", "E", "E"],
            ["R", "R", "R", "E", "E"],
        ]
        self.table.matrix = matrix
        self.assertEqual(self.table.get_free_position(1), 0)

    def test_make_turn(self):
        matrix = [
            ["E", "E"],
            ["E", "E"]
        ]
        matrix2 = [
            ["E", "E"],
            ["R", "E"]
        ]
        self.table.matrix = matrix
        self.table.make_turn(0, "R")
        self.assertEqual(self.table.get_matrix(), matrix2)

    def test_commit_turn(self):
        matrix = [
            ["E", "E"],
            ["E", "E"]
        ]
        matrix2 = [
            ["E", "E"],
            ["R", "E"]
        ]
        self.table.matrix = matrix
        self.table.commit_turn(0, "R")
        self.assertEqual(self.table.get_matrix(), matrix2)

    def test_commit_turn_col_is_full(self):
        matrix = [
            ["R", "E"],
            ["R", "E"],
            ["R", "E"],
            ["R", "E"],
        ]

        self.table.matrix = matrix
        self.assertFalse(self.table.commit_turn(0, "R"))

    def test_horizontal_win(self):
        matrix = [
            ["R", "E", "E", "E"],
            ["R", "E", "E", "E"],
            ["E", "E", "E", "E"],
            ["R", "R", "R", "R"],
        ]
        self.table.matrix = matrix
        self.assertEqual(self.table.horizontal_win()[0], True)

    def test_vertical_win(self):
        matrix = [
            ["R", "E", "E", "E"],
            ["R", "E", "E", "E"],
            ["R", "E", "E", "E"],
            ["R", "E", "R", "R"],
        ]
        self.table.matrix = matrix
        self.assertEqual(self.table.vertical_win()[0], True)

    def test_first_diagonal_win(self):
        matrix = [
            ["R", "E", "E", "R"],
            ["R", "R", "R", "E"],
            ["E", "R", "R", "E"],
            ["R", "E", "R", "R"],
        ]
        self.table.matrix = matrix
        self.assertEqual(self.table.first_diagonal_win()[0], True)
if __name__ == '__main__':
    unittest.main()
