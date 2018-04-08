import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        # Through out this project, added codes are inside {}
        #{ Calculate the determinant of a 1x1 matrix
        if len(self.g) ==1 and len(self.g[0]) == 1:
            det =1/self.g[0][0]
        #Calculate the determinant of a 2x2 matrix
        if len(self.g) == 2:
            det = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        return det    
        #}    
                      
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        #{ 
        trace = 0
        for i in range(len(self.g)):
            trace = trace + self.g[i][i]
        return trace
        #}  
              
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        #{ Calculate the inverse of a 1x1 matrix
        inverse = []
        if len(self.g) ==1 and len(self.g[0]) == 1:
            row=[1/self.g[0][0]]
            inverse.append(row)
        #  Calculate the inverse of a 2x2 matrix   
        if len(self.g) == 2:
            if self.g[0][0]*self.g[1][1] == self.g[0][1]*self.g[1][0]:
                raise ValueError('The matrix is not invertible')
            else:
                det = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
                row_one = []
                row_one.append(self.g[1][1])
                row_one.append(-self.g[0][1])
                inverse.append(row_one)
                row_two = []
                row_two.append(-self.g[1][0])
                row_two.append(self.g[0][0])
                inverse.append(row_two)
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j]=inverse[i][j]*1/det
        return inverse
        #} 
        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        #{
        matrix_transpose = []
        for i in range (len(self.g[0])):
            row = []
            for j in range (len(self.g)):
                row.append(self.g[j][i])
            matrix_transpose.append(row)
        return matrix_transpose
         #}
    def is_square(self):
        return self.h == self.w
  
    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #{
        #test the two matrices is vectors or not
        matrixSum=[]
        if type(self.g[0]) == int and type(other[0]) == int:
            for i in range(len(self.g)):
                matrixSum.append(self.g[i]+other[i])
        #add two matrices
        else:
            for i in range(len(self.g)):
                row = []
                for j in range(len(self.g[0])):
                    row.append(self.g[i][j]+other[i][j])
                matrixSum.append(row)
        
        return matrixSum      
        #}

        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #{
        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                self.g[i][j] = -self.g[i][j]
        return self.g
        #}

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #{Add negative other
        sub = self.g + (-other) 
        
        return sub 
         #}

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #{ 
        #Test if the number of column in grid equal the number of row in other:
        if len(self.g[0]) != len(other):
            raise(ValueError, "Invalid multiplication length wise")
               
        #define the dot product as an inner function:
        def dot_product(vector_one, vector_two):
            dot_sum = 0
            #test if the vector length is equal
            if len(vector_one) != len(vector_two):
                raise(ValueError, "Two vectors must be equal in length to caluclate their dot product")
            for i in range(len(vector_one)):
                dot_sum= dot_sum + vector_one[i]*vector_two[i]
            return dot_sum

        product = []
        #take the transpose of other and store the result in a new matrix
        other_T = other.T()
        #use a nestet for loop to iterate through the rows of grid and the rows of transpose of the other
        for i in range(len(self.g)):
            row = []
            for j in range (len(other_T)):
                row.append(dot_product(self.g[i],other_T[j]))
            product.append(row)
        return product
        #}

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #{
            for i in range(len(self.g)):
                for j in range(len(self.g[0])):
                    self.g[i][j] = self.g[i][j] * other
        return self.g
            #}
            
            
            
            
            
 
            
 