class Table:
    EMPTY = "E"
    RED = "R"
    BLACK = "B"
    RANGE = (10, 10)
    MATRIX = [
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E"]
    ]

    def __init__(self):
        self.matrix = self.MATRIX

    def col_is_full(self, col):
        """Проверява дали дадена колона е пълна.
        """
        for i in range(0, len(self.matrix) - 1):
            if self.matrix[i][col] == "E":
                return True
        return False

    def get_matrix(self):
        """
        Връща матрицата.
        """
        return self.matrix

    def print_table(self):
        """
        Принтира на терминала матрицата.
        """
        for i in range(0, len(self.matrix)):
            print(self.matrix[i])

    def has_winner(self):
        """
        Проверява дали имаме победител.
        """
        if self.horizontal_win()[0] == True:
            return True
        if self.vertical_win()[0] == True:
            return True
        if self.first_diagonal_win()[0] == True:
            return True
        if self.second_diagonal_win()[0] == True:
            return True
        return False

    def get_winner(self):
        """
        Връща победителя в играта.
        """
        if self.horizontal_win()[0] == True:
            return self.horizontal_win()[1]
        if self.vertical_win()[0] == True:
            return self.vertical_win()[1]
        if self.first_diagonal_win()[0] == True:
            return self.first_diagonal_win()[1]
        if self.second_diagonal_win()[0] == True:
            return self.second_diagonal_win()[1]
        return self.EMPTY

    def get_free_position(self, col):
        """
        Връша позиция на която може да се играе.
        """
        for i in range(0, len(self.matrix)):
            if self.matrix[i][col] != self.EMPTY:
                return i - 1
        return len(self.matrix) - 1

    def make_turn(self, col, color):
        """
        Прави ход.
        Не проверява дали имам победител.
        """
        self.matrix[self.get_free_position(col)][col] = color

    def commit_turn(self, col, color):
        """
        Прави проверки дали хода е възможен.
        Ако е възможен го прави, ако не връща False.
        """
        if not self.col_is_full(col):
            return False
        else:
            if self.has_winner():
                return True
            else:
                self.make_turn(col, color)

    def horizontal_win(self):
        """
        Проверява дали има победител в хоризонтална позция.
        Ако има връща кортеж с знак, че има победител и кой е победитея.
        Ако не връща кортеж, с False и празна позиция
        """
        counter = 1
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i]) - 1):
                if self.matrix[i][j] != self.EMPTY:
                    if self.matrix[i][j] == self.matrix[i][j + 1]:
                        counter = counter + 1
                    else:
                        counter = 1
                    if counter == 4:
                        return (True, self.matrix[i][j])
        return (False, self.EMPTY)

    def vertical_win(self):
        """
        Проверява дали има победител в вертикална позция.
        Ако има връща кортеж с знак, че има победител и кой е победитея.
        Ако не връща кортеж, с False и празна позиция
        """
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i]) - 3):
                if self.matrix[j][i] != self.EMPTY:
                    first = self.matrix[j][i] == self.matrix[j + 1][i]
                    second = self.matrix[j][i] == self.matrix[j + 2][i]
                    third = self.matrix[j][i] == self.matrix[j + 3][i]
                    if first and second and third:
                        return (True, self.matrix[j][i])
        return (False, self.EMPTY)

    def first_diagonal_win(self):
        """
        Проверява дали има победител по диагонала.
        Ако има връща кортеж с знак, че има победител и кой е победитея.
        Ако не връща кортеж, с False и празна позиция
        """
        for i in range(0, len(self.matrix) - 3):
            for j in range(0, len(self.matrix[i]) - 3):
                if self.matrix[j][i] != self.EMPTY:
                    first = self.matrix[j][i] == self.matrix[j + 1][i + 1]
                    second = self.matrix[j][i] == self.matrix[j + 2][i + 2]
                    third = self.matrix[j][i] == self.matrix[j + 3][i + 3]
                    if first and second and third:
                        return (True, self.matrix[j][i])
        return (False, self.EMPTY)

    def second_diagonal_win(self):
        """
        Проверява дали има победител по втория диагонал.
        Ако има връща кортеж с знак, че има победител и кой е победитея.
        Ако не връща кортеж, с False и празна позиция
        """
        for i in range(0, len(self.matrix) - 3):
            for j in range(3, len(self.matrix[i])):
                if self.matrix[i][j] != self.EMPTY:
                    first = self.matrix[i][j] == self.matrix[i + 1][j - 1]
                    second = self.matrix[i][j] == self.matrix[i + 2][j - 2]
                    third = self.matrix[i][j] == self.matrix[i + 3][j - 3]
                    if first and second and third:

                        return (True, self.matrix[i][j])
        return (False, self.EMPTY)
