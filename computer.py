from table import Table
import random


class Computer:
    def __init__(self, player):
        self.player = player

    def potential_enemy_win_horizontal(self, matrix):
        """Проверява за потенциалена победа на противника в хоризонтална позиция.
        Ако такъв ход не  съществува връща кортеж (-1, -1).
        Ако има такава вероятност връща позиция за ход"""
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i]) - 3):
                if matrix[i][j] != self.player and matrix[i][j] != Table.EMPTY:
                    b1 = matrix[i][j] == matrix[i][j + 1]
                    b2 = matrix[i][j] == matrix[i][j + 2]
                    if b1 and b2:
                        return (i, j + 3)
        return (-1, -1)

    def potential_enemy_win_vertical(self, matrix):
        """Проверява за потенциалена победа  на противника в вертиаклна вертикална.
        Ако такъв ход не  съществува връща кортеж (-1, -1).
        Ако има такава вероятност връща позиция за ход"""
        for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix) - 2):
                if matrix[j][i] != self.player and matrix[j][i] != Table.EMPTY:
                    b1 = matrix[j][i] == matrix[j + 1][i]
                    b2 = matrix[j][i] == matrix[j + 2][i]
                    if b1 and b2:
                        return (j + 3, i)
        return (-1, -1)

    def potential_player_win_horizontal(self, matrix):
        """Проверява за потенциалена победа на компютъра в хоризонтална позиция.
        Ако такъв ход не  съществува връща кортеж (-1, -1).
        Ако има такава вероятност връща позиция за ход"""
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i]) - 3):
                if matrix[i][j] == self.player:
                    b1 = matrix[i][j] == matrix[i][j + 1]
                    b2 = matrix[i][j] == matrix[i][j + 2]
                    if b1 and b2:
                        return (i, j + 3)
        return (-1, -1)

    def potential_player_win_vertical(self, matrix):
        """Проверява за потенциалена победа на компютъра в вертикална позиция.
        Ако такъв ход не  съществува връща кортеж (-1, -1).
        Ако има такава вероятност връща позиция за ход"""
        for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix) - 3):
                if matrix[j][i] == self.player:
                    b1 = matrix[j][i] == matrix[j + 1][i]
                    b2 = matrix[j][i] == matrix[j + 2][i]
                    if b1 and b2:
                        return (j + 3, i)
        return (-1, -1)

    def potential_player_win_first_diagonal(self, matrix):
        """Проверява за потенциалена победа на компютъра по диагонала.
        Ако такъв ход не  съществува връща кортеж (-1, -1).
        Ако има такава вероятност връща позиция за ход
        """
        for i in range(1, len(matrix) - 2):
            for j in range(1, len(matrix[i]) - 2):
                if matrix[i][j] == self.player and matrix[i][j] != Table.EMPTY:
                    b1 = matrix[i][j] == matrix[i + 1][j + 1]
                    b2 = matrix[i][j] == matrix[i + 2][j + 2]
                    if b1 and b2:
                        return (i-1, j-1)
        return (-1, -1)

    def get_turn_with_series_of_two_vertical(self, matrix):
        """
        Проверява дали има два поредни пула и слага до тях
        """
        for i in range(0, len(matrix) - 1):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] != self.player and matrix[i][j] != Table.EMPTY:
                    if matrix[i][j] == matrix[i + 1][j]:
                        return (i - 1, j)
        return (-1, -1)

    def get_turn_with_series_of_two_horizontal(self, matrix):
        """
        Проверява дали има два поредни пула и слага до тях
        """
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i]) - 1):
                if matrix[i][j] != self.player and matrix[i][j] != Table.EMPTY:
                    if matrix[i][j] == matrix[i][j + 1]:
                        return (i, j - 1)
        return (-1, -1)

    def get_turn(self, matrix):
        """
        Връща ход на компутъра
        """
        if self.potential_enemy_win_vertical(matrix)[0] != -1:
            print(1)
            return self.potential_enemy_win_vertical(matrix)[1]
        elif self.potential_enemy_win_horizontal(matrix)[0] != -1:
            print(2)
            print(self.potential_enemy_win_horizontal(matrix)[1])
            return self.potential_enemy_win_horizontal(matrix)[1]
        elif self.potential_player_win_horizontal(matrix)[0] != -1:
            print(3)
            return self.potential_player_win_horizontal(matrix)[1]
        elif self.potential_player_win_vertical(matrix)[0] != -1:
            print(4)
            return self.potential_player_win_vertical(matrix)[1]
        elif self.potential_player_win_first_diagonal(matrix)[0] != -1:
            print(5)
            return self.potential_player_win_first_diagonal(matrix)[1]
        elif self.get_turn_with_series_of_two_vertical(matrix)[0] != -1:
            print(8)
            return self.get_turn_with_series_of_two_vertical(matrix)[1]
        elif self.get_turn_with_series_of_two_horizontal(matrix)[0] != -1:
            print(9)
            return self.get_turn_with_series_of_two_horizontal(matrix)[1]
        else:
            print(7)
            return random.randint(0, len(matrix) - 1)
