To fully understand how to rotate an \( n \times n \) 2D matrix by 90 degrees clockwise in Python, let's break down the problem into smaller steps and concepts. We will then implement a solution that performs the rotation in-place, i.e., without using extra space for another matrix.

### Key Concepts and Steps

1. **Matrix Representation in Python**
   - A 2D matrix can be represented using a list of lists in Python. For example, a 3x3 matrix would look like this:
     ```python
     matrix = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ]
     ```

2. **In-place Operations**
   - Performing operations directly on the original data structure without creating a copy. This is essential to minimize space complexity.

3. **Matrix Transposition**
   - Transposing a matrix means converting its rows into columns. For example, the transpose of the above matrix would be:
     ```python
     transposed_matrix = [
         [1, 4, 7],
         [2, 5, 8],
         [3, 6, 9]
     ]
     ```

4. **Reversing Rows in a Matrix**
   - After transposing the matrix, the next step to achieve a 90-degree clockwise rotation is to reverse the order of elements in each row of the transposed matrix.

5. **Nested Loops**
   - Using nested loops to iterate through the 2D matrix to perform the transposition and row reversal.

### Steps to Rotate the Matrix

1. **Transpose the Matrix**:
   - Swap the elements across the diagonal. For an element at position \((i, j)\), swap it with the element at position \((j, i)\).

2. **Reverse Each Row**:
   - Reverse the order of elements in each row of the transposed matrix.

### Implementation

Let's implement the solution step-by-step:

#### Pseudocode

1. Iterate through each element above the diagonal (i.e., where \(i < j\)) and swap elements to transpose the matrix.
2. Reverse each row to complete the rotation.

```plaintext
for i from 0 to n-1:
    for j from i+1 to n-1:
        swap(matrix[i][j], matrix[j][i])

for each row in matrix:
    reverse(row)
```

#### Python Code

```python
def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

rotate_2d_matrix(matrix)

print("Rotated matrix:")
for row in matrix:
    print(row)
```

#### Example and Output

Given the initial matrix:
```
1 2 3
4 5 6
7 8 9
```

**After Transposition**:
```
1 4 7
2 5 8
3 6 9
```

**After Reversing Each Row**:
```
7 4 1
8 5 2
9 6 3
```

### Final Output

The matrix after rotating 90 degrees clockwise:
```python
Rotated matrix:
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
```

### Explanation

1. **Transposing the Matrix**:
   - Elements are swapped such that the element at position \((i, j)\) is swapped with the element at \((j, i)\).

2. **Reversing Each Row**:
   - Each row of the transposed matrix is reversed to complete the 90-degree rotation.

By following these steps and understanding the concepts, you can successfully rotate an \( n \times n \) matrix by 90 degrees clockwise in Python.

---

