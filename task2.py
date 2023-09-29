""" Матрица на классах """



""" def matrix_transposition(matrix: list[list[int]]):
    for row in matrix:
        print(row)
    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("\n")
    for row in rez:
        print(row)
        """
        
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix 
                    
    def matrix_transpose( self ):
        if not matrix: return []
        return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]  

matrix = [[1, 2], [4, 5], [7, 8]]
x = Matrix (matrix)
print (x.matrix_transpose())  