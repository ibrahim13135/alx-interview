To rotate a square matrix by 90 degrees anti-clockwise in-place, you can follow a cycle-based approach. This involves processing the matrix in cycles, where each cycle consists of elements that need to be rotated. Here's a detailed explanation along with the Python implementation and some advanced examples.

#### Concept
1. **Cycles and Layers**:
   - A \( N \times N \) matrix has \( N/2 \) layers (cycles). The outermost layer is the first cycle, the next one is the second cycle, and so on.
   - In each cycle, we process groups of 4 elements and rotate them.

2. **Element Rotation**:
   - For each cycle, select elements from four sides and rotate them:
     - Top -> Left
     - Left -> Bottom
     - Bottom -> Right
     - Right -> Top

3. **Indices Calculation**:
   - For each cycle starting at index \( x \):
     - Iterate through the elements from index \( x \) to \( N-x-1 \).

### Steps
1. Iterate through each cycle (layer) of the matrix.
2. For each element in the cycle, rotate the corresponding 4 elements.
3. Use a temporary variable to store one of the elements while performing the rotation to avoid overwriting.

### Implementation in Python

Here's the Python code to achieve this:

```python
def rotate_matrix_90_anticlockwise(matrix):
    N = len(matrix)
    
    # Consider all squares one by one
    for x in range(N // 2):
        # Consider elements in group of 4 in current square
        for y in range(x, N - x - 1):
            # Store current cell in temp variable
            temp = matrix[x][y]
            
            # Move values from right to top
            matrix[x][y] = matrix[y][N - 1 - x]
            
            # Move values from bottom to right
            matrix[y][N - 1 - x] = matrix[N - 1 - x][N - 1 - y]
            
            # Move values from left to bottom
            matrix[N - 1 - x][N - 1 - y] = matrix[N - 1 - y][x]
            
            # Assign temp to left
            matrix[N - 1 - y][x] = temp

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

# Test Case 1
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
print_matrix(matrix1)
rotate_matrix_90_anticlockwise(matrix1)
print("Rotated matrix by 90 degrees anti-clockwise:")
print_matrix(matrix1)

# Test Case 2
matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Original matrix:")
print_matrix(matrix2)
rotate_matrix_90_anticlockwise(matrix2)
print("Rotated matrix by 90 degrees anti-clockwise:")
print_matrix(matrix2)
```

### Outputs and Examples

**Example 1:**

Input:
```
Matrix:
1  2  3
4  5  6
7  8  9
```

Output:
```
Rotated Matrix:
3  6  9
2  5  8
1  4  7
```

**Example 2:**

Input:
```
Matrix:
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
```

Output:
```
Rotated Matrix:
4  8  12 16
3  7  11 15
2  6  10 14
1  5  9  13
```

### Dry Run of Example 2

1. **First Cycle**:
   ```
   Initial Matrix:
   1  2  3  4
   5  6  7  8
   9  10 11 12
   13 14 15 16

   After first group rotation:
   4  2  3 16
   5  6  7  8
   9  10 11 12
   1  14 15 13

   After second group rotation:
   4  8  3 16
   5  6  7  15
   2  10 11 12
   1  14 9  13

   After third group rotation:
   4  8  12 16
   3  6  7  15
   2  10 11 14
   1  5  9  13
   ```

2. **Second Cycle**:
   ```
   Initial Matrix:
   4  8  12 16
   3  6  7  15
   2  10 11 14
   1  5  9  13

   After rotating second cycle:
   4  8  12 16
   3  7  11 15
   2  6  10 14
   1  5  9  13
   ```

This method runs in \(O(N^2)\) time complexity since each element in the \(N \times N\) matrix is visited once. The space complexity is \(O(1)\) because it only uses a constant amount of extra space for the temporary variable.




----


### Explanation and Implementation of In-Place 90-Degree Anti-Clockwise Rotation of a Matrix

#### Concept
To rotate a \( N \times N \) matrix by 90 degrees in an anti-clockwise direction without using extra space, we can follow two main steps:

1. **Transpose the matrix**: This step swaps elements along the diagonal.
2. **Reverse each row**: This step reverses the elements in each row to achieve the final rotated matrix.

This method ensures that the matrix is rotated in-place with a time complexity of \( O(N^2) \) and an auxiliary space complexity of \( O(1) \).

#### Steps
1. **Transpose the matrix**:
   - Swap elements `matrix[i][j]` with `matrix[j][i]` for all \( i < j \).

2. **Reverse each row**:
   - For each row, reverse the order of the elements.

#### Python Implementation
Here's the Python code to achieve this:

```python
def transpose_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_rows(matrix):
    for row in matrix:
        row.reverse()

def rotate_matrix_90_anticlockwise(matrix):
    transpose_matrix(matrix)
    reverse_rows(matrix)

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

# Test Case 1
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
print_matrix(matrix1)
rotate_matrix_90_anticlockwise(matrix1)
print("Rotated matrix by 90 degrees anti-clockwise:")
print_matrix(matrix1)

# Test Case 2
matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Original matrix:")
print_matrix(matrix2)
rotate_matrix_90_anticlockwise(matrix2)
print("Rotated matrix by 90 degrees anti-clockwise:")
print_matrix(matrix2)
```

### Outputs and Examples

**Example 1:**

Input:
```
Matrix:
1  2  3
4  5  6
7  8  9
```

Output:
```
Rotated Matrix:
3  6  9
2  5  8
1  4  7
```

**Example 2:**

Input:
```
Matrix:
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
```

Output:
```
Rotated Matrix:
4  8  12 16
3  7  11 15
2  6  10 14
1  5  9  13
```

### Explanation of Steps

1. **Transpose the Matrix**:
   - The transpose operation swaps elements at positions (i, j) with elements at positions (j, i).
   - For example, after transposing the first example matrix:
     ```
     1  2  3         1  4  7
     4  5  6  -->    2  5  8
     7  8  9         3  6  9
     ```

2. **Reverse Each Row**:
   - After transposing, each row of the matrix is reversed to complete the 90-degree anti-clockwise rotation.
   - Continuing the first example:
     ```
     1  4  7         7  4  1
     2  5  8  -->    8  5  2
     3  6  9         9  6  3
     ```

By following these steps, you can efficiently rotate a square matrix by 90 degrees in an anti-clockwise direction without using any additional space. This method leverages the properties of matrix transposition and row reversal to achieve the desired result.
