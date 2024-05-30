
# my_list = [1,2,3,4,5]

# print(my_list[0])


# my_list[0] = 2

# print(my_list[0])

# for i in my_list:
#     print(i)



##a concise way to create lists.
# my_advlist = [x**2 for x in range(100)]

# print(my_advlist)


# 
def generate_pascal_triangle(num_rows):
    # Initialize an empty list to hold all rows of Pascal's Triangle
    triangle = []

    # Loop through each row number from 0 to num_rows - 1
    for n in range(num_rows):
        # Create a new row filled with 1s. The length is n + 1
        row = [1] * (n + 1)
        
        # Update the middle elements of this row
        for i in range(1, n):
            # Each element is the sum of the two numbers directly above it from the previous row
            row[i] = triangle[n-1][i-1] + triangle[n-1][i]
        
        # Add the new row to the list of rows
        triangle.append(row)
    
    # Return the list of rows after all rows are generated
    return triangle

# Generate Pascal's Triangle with 5 rows and print the result
triangle = generate_pascal_triangle(5)
for row in triangle:
    print(row)
