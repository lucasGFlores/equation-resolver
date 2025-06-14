import numpy as np


class Matrix:
    """
    responsabilidades:
        - calcular determinante
        - trocar colunas
    """

    def __init__(self, matrix: list):
        self.matrix: np.array = np.array(matrix)

    def change_column(self, column: int, new_column: list) -> "Matrix":
        new_column = np.array(new_column)
        if new_column.shape[0] != self.matrix.shape[0]:
            raise ValueError(
                "a nova coluna não tem o tamanho correto da matriz original"
            )
        new_matrix = self.matrix.copy()
        new_matrix[:, column] = new_column
        return Matrix(list(new_matrix))

    def determinant(self) -> float:
        return Matrix._laplace_determinant(self.matrix)

    @staticmethod
    def _laplace_determinant(matrix: np.array):
        """
        Usa o Teorema de Laplace para calcular qualquer tipo de matriz quadrada.
        Este método usa o Teorema de Laplace recursivamente, reduzindo a matriz para uma matriz 2x2,
        para um cálculo mais fácil usando determinante de 2x2.
        Teorema de Laplace:
         M = [[2, 2, 1],
              [3, 1, 1],
             [3, 1, 4]]

         det M = a11* C11 + a12*C12 + a13*C13 (a quantidade de a's e C's é igual ao tamanho da matriz)

         a são os elementos. (a11 = 2)

         C são os cofatores determinantes do elemento (remover a coluna e a linha do elemento C)
         C11 = (-1)^(1+1) x [[1,1] =  3
                            [1,4]]

         C12 = (-1)^(1+2) x [[3,1]   = -9
                             [3,4]]

         C13 = (-1)^(1+3) x [[3,1]   = 0
                             [3,1]]

         det M = 2*3 + 2*(-9) + 1*0 = -12


        :param matrix: Uma matriz quadrada de qualquer tamanho
        :return: um float. ex: -12.3
        """
        if matrix.shape[0] == 2:
            return Matrix._determinant_2x2_matrix(matrix)

        # Soma da multiplicação do elemento pelo determinante da matriz dos cofatores
        results = []
        for column in range(0, matrix.shape[0]):
            element = matrix[0, column]
            mult = pow(-1, 2 + column)
            cofactors = Matrix._cofactors_matrix(matrix.copy(), 0, column)
            det_cofactors = Matrix._laplace_determinant(cofactors)
            results.append(element * mult * det_cofactors)
        return sum(results)

    @staticmethod
    def _determinant_2x2_matrix(square_matrix: np.array):
        if square_matrix.shape[0] != 2:
            raise ValueError
        return square_matrix[0, 0] * square_matrix[1, 1] - (square_matrix[0, 1] * square_matrix[1, 0])

    @staticmethod
    def _cofactors_matrix(matrix: np.array, line: int, column: int) -> np.array:
        """
        :param
            matrix - matriz a ser reduzida
            line - linha do elemento
            column - coluna do elemento
        :return: a matriz reduzida
        """
        matrix = np.delete(matrix, line, axis=0)  # remove a linha
        matrix = np.delete(matrix, column, axis=1)  # remove a coluna
        return matrix
