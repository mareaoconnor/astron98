#homework number 5 
import numpy as np

#hey twin
def find_rows_with_all_equal_values(matrix):
    #converting input into a numpy 
    arr = np.array(matrix)
    #code to find where all values of row are equal
    equal_rows = arr[(arr[:, 1:] == arr[:, :-1]).all(axis=1)]
    return equal_rows
matrix = [
    [1,1,1],
    [2,3,4],
    [3,3,3],
]
equal_rows = find_rows_with_all_equal_values(matrix)
print("rows where all values are equal:")
print(equal_rows)


#checkers
# create an 8 by 8 array filled with zeros
checkerboard = np.zeros((8,8), dtype = int)
# fill in alternate rows with ones
# even rows, even numbers
checkerboard[::2, ::2] = 1 
# odd rows, odd numbers
checkerboard[1::2, 1::2] = 1
print(checkerboard)


#I need some space
def separate_letters(arr):
    #convert array of strings into numpy
    char_array = np.array(list(' '.join(arr)))
    #reshape array to have letter per element
    char_array = char_array[np.newaxis, :]
    return char_array
array_of_strings = ["I","love","to","code"]
result = separate_letters(array_of_strings)
print(result)

#everything is in order
#define multidimension matrix
matrix = np.array([[1,4,5],
                   [1,3,6],
                   [8,3,6]])
#sort matrix along columns
sort_matrix = np.sort(matrix, axis=0)
print("original matrix:")
print(matrix)
print("sortef matrix along the columns:")
print(sort_matrix)
