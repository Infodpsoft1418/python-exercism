class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(x) for x in row.split()] for row in matrix_string.split("\n")]

        self.cols = [list(tup) for tup in zip(*self.rows)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.cols[index - 1]
