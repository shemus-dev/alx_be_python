import numpy as np

# Create a 2-dimensional array with 3 rows and 4 columns
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# Access an element at row 1, column 2

print(arr[1,1])

for row in arr:
    for element in row:
        print(element, end="")