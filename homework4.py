#2
# Creating a variable named 'number_list' assigned to a list containing numbers from 0 to 50
number_list = list(range(51))
#syntax error when I didn't put parantheses around 51
print(number_list)

#2.1 squaring lists
def square_elements(input_list):
    """
    Squares each element in the input list and returns a new list.
    
    Parameters:
        input_list (list): The list containing elements to be squared.
        
    Returns:
        list: A new list containing squared elements.
    """
    squared_list = [x ** 2 for x in input_list]
    #syntax error didn't put brackets
    #name error because didnt relate x to input list, fixed it by typing code above
    return squared_list
original_list = [1, 2, 3, 4, 5]
result_list = square_elements(original_list)
print(result_list)

#2.3 2 lists
def odd_integers_sorted(listA, listB):
    """
    Returns a new list containing only the odd integers from both lists in sorted order.
    
    Parameters:
        listA (list): The first list containing integers.
        listB (list): The second list containing integers.
        
    Returns:
        list: A new list containing only the odd integers from both lists in sorted order.
    """
    combined_list = listA + listB  # Combine both lists
    odd_integers = [num for num in combined_list if num % 2 != 0]  # Filter out odd integers
    return sorted(odd_integers)  # Sort the resulting list
listA = list(range(1, 11))
listB = list(range(20, 31))
result = odd_integers_sorted(listA, listB)
print(result)

#3 part 1
# Initialize an empty 2D list
matrix = []

# Populate the 2D list using nested for loops
for i in range(5):
    row = []  # Initialize an empty row
    for j in range(5):
        number = i * 5 + j + 1  # Calculate the number for this position
        row.append(number)  # Append the number to the row
    matrix.append(row)  # Append the row to the matrix

# Print the 2D list
for row in matrix:
    print(row)

#3 part 2
# Initialize an empty 2D list
matrix = []

# Populate the 2D list using nested for loops
for i in range(5):
    row = []  # Initialize an empty row
    for j in range(5):
        number = i * 5 + j + 1  # Calculate the number for this position
        # Check if the number is a multiple of 3
        if number % 3 == 0:
            #syntax error forgot to put the :
            row.append('?')  # Replace with '?' if it's a multiple of 3
            #syntax error: forgot to put quotations around ?
        else:
            row.append(number)  # Append the number to the row
    matrix.append(row)  # Append the row to the matrix

# Print the 2D list
for row in matrix:
    print(row)

#4
def remove_duplicates(input_list):
    """
    Removes duplicate values from a list and returns a copy of the list with duplicates removed.
    
    Parameters:
        input_list (list): The input list containing elements with possible duplicates.
        
    Returns:
        list: A copy of the input list with duplicate values removed.
    """
    unique_list = []  # Initialize an empty list to store unique elements
    for item in input_list:
        if item not in unique_list:  # Check if the item is not already in the unique list
            unique_list.append(item)  # If not, add it to the unique list
    return unique_list

# Example usage:
original_list = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9]
result_list = remove_duplicates(original_list)
print(result_list)
