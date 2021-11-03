
def matrix_sum(matrix):
    
    for count, value in enumerate(matrix):
        
        matrix[count] = sum(value)
    
    
    return matrix 
  
     


print (matrix_sum([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]) )       