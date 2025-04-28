import numpy as np
class Matrix:
    """
    responsibilities:
        - calculate determinant
        - change columns
    """
    def __init__(self, matrix: list):
        self.matrix: np.array = np.array(matrix)

    def change_column(self, column: int, new_column: list) -> None:
        new_column = np.array(new_column)
        if new_column.shape[0] != self.matrix.shape[0]:
            raise ValueError("row matrix dont have the right size of the original matrix")
        self.matrix[:,column] = new_column

    def determinant(self) -> float:
        return Matrix._laplace_determinant(self.matrix)

    @staticmethod
    def _laplace_determinant(matrix: np.array):
        """
        Use the Laplace Theorem to calculate any type of quadratic matrix.
        These systems use the Laplace Theorem recursively, reducing the matrix to a 2x2 matrix, for an
        easier calculation using 2x2 determinant.
        Laplace Theorem:
         M = [[2, 2, 1],
              [3, 1, 1],
             [3, 1, 4]]

         det M = a11* C11 + a12*C12 + a13*C13 (the nums of a's and C's is the exact size of the matrix)

         a is the elements. (a11 = 2)

         C is the determinant cofactors of the element.(remove the column and the line of the C element)
         C11 =     (-1)^(1+1) x [[1,1]   =  3
                                 [1,4]]

        C12 = (-1)^(1+2) x [[3,1]   = -9
                            [3,4]]

        C13 = (-1)^(1+3) x [[3,1]   = 0
                            [3,1]]

        det M = 2*3 + 2*(-9) + 1*0 = -12


        :param matrix: A quadratic matrix with any size
        :return: a float. ex: -12.3
        """
        if matrix.shape[0] == 2:
            return Matrix._determinant_2x2_matrix(matrix)

        # The sum of multiplication of the element and the determinant coefficient matrix
        results = []
        for column in range(0, matrix.shape[0]):
            element = matrix[0,column]
            mult = pow(-1,2+column)
            cofactors = Matrix._cofactors_matrix(matrix.copy(),0,column)
            det_cofactors = Matrix._laplace_determinant(cofactors)
            results.append(element*mult*det_cofactors)
        return sum(results)


    @staticmethod
    def _determinant_2x2_matrix(square_matrix:np.array):
        if square_matrix.shape[0] != 2:
            raise ValueError
        return square_matrix[0,0] * square_matrix[1,1] - (square_matrix[0,1] * square_matrix[1,0])

    @staticmethod
    def _cofactors_matrix(matrix:np.array ,line:int, column: int) -> np.array:
        """
        :param
            matrix - the matrix to reduce
            line - line of the element
            column - column of the element
        :return: the reduced matrix
        """
        matrix = np.delete(matrix,line,axis=0) #remove the line
        matrix = np.delete(matrix,column,axis=1) #remove the column
        return matrix