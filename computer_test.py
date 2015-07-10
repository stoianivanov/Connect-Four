import unittest
from computer import Computer


class ComputerTest(unittest.TestCase):

    def setUp(self):
        self.pc = Computer("B")

    def test_potential_enemy_win_horizontal(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "R", "R", "R", "E", "E", "E"]
        ]
        self.assertEqual(self.pc.potential_enemy_win_horizontal(
            matrix), (3, 4))

    def test_potential_enemy_win_horizontal_not_win(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "R", "R", "E", "E", "E", "E"]
        ]
        self.assertEqual(self.pc.potential_enemy_win_horizontal(
            matrix), (-1, -1))

    def test_potential_enemy_win_horizontal_not_win_v2(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "R", "B", "E"],
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"]
        ]
        self.assertEqual(self.pc.potential_enemy_win_horizontal(
            matrix), (-1, -1))

    def test_potential_enemy_win_vertical(self):
        matrix = [
            ["E", "E", "E", "R", "E", "E", "E"],
            ["E", "E", "E", "R", "E", "E", "E"],
            ["E", "E", "E", "R", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"]
        ]
        self.assertEqual(self.pc.potential_enemy_win_vertical(matrix), (3, 3))

    def test_potential_enemy_win_vertical_not_win(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "R", "E", "E", "E"],
            ["E", "E", "E", "R", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"]
        ]
        self.assertEqual(self.pc.potential_enemy_win_vertical(
            matrix), (-1, -1))

    def test_potential_player_win_horizontal(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "B", "B", "B", "E", "E"],
            ["R", "E", "E", "E", "E", "E", "E"],
            ["E", "R", "E", "R", "B", "B", "E"]
        ]
        self.assertEqual(self.pc.potential_player_win_horizontal(
            matrix), (1, 5))

    def test_potential_player_not_win_horizontal(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "B", "B", "E", "E", "E"],
            ["R", "E", "E", "E", "E", "E", "E"],
            ["E", "R", "E", "R", "B", "B", "E"]
        ]
        self.assertEqual(self.pc.potential_player_win_horizontal(
            matrix), (-1, -1))

    def test_potential_player_win_first_diagonal(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "B", "B", "R", "E", "E"],
            ["R", "E", "E", "B", "E", "E", "E"],
            ["E", "B", "E", "R", "B", "B", "E"]
        ]
        self.assertEqual(self.pc.potential_player_win_first_diagonal(
            matrix), (0, 1))

    def test_potential_player_not_win_first_diagonal(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"]
        ]
        self.assertEqual(self.pc.potential_player_win_first_diagonal(
            matrix), (-1, -1))

    def test_potential_player_win_second_diagonal(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "B", "R", "R", "E", "E"],
            ["R", "E", "E", "B", "E", "E", "E"],
            ["E", "B", "R", "R", "B", "B", "E"]
        ]
        self.assertEqual(self.pc.potential_player_win_first_diagonal(
            matrix), (0, 1))

    def test_potential_player_not_win_second_diagonal(self):
        matrix = [
            ["E", "E", "E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E", "E", "E"],
            ["R", "E", "E", "E", "E", "E", "E"],
            ["E", "B", "R", "R", "E", "B", "E"]
        ]
        self.assertEqual(self.pc.potential_player_win_first_diagonal(
            matrix), (-1, -1))


if __name__ == '__main__':
    unittest.main()
