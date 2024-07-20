### List Methods in Detail

1. **`list.append(x)`**
   - Adds an item to the end of the list.
   ```python
   fruits = ['orange', 'apple', 'pear']
   fruits.append('banana')
   print(fruits)
   # Output: ['orange', 'apple', 'pear', 'banana']
   ```

2. **`list.extend(iterable)`**
   - Extends the list by appending all the items from the iterable.
   ```python
   fruits = ['orange', 'apple']
   fruits.extend(['pear', 'banana'])
   print(fruits)
   # Output: ['orange', 'apple', 'pear', 'banana']
   ```

3. **`list.insert(i, x)`**
   - Inserts an item at a given position.
   ```python
   fruits = ['orange', 'apple', 'pear']
   fruits.insert(1, 'banana')
   print(fruits)
   # Output: ['orange', 'banana', 'apple', 'pear']
   ```

4. **`list.remove(x)`**
   - Removes the first item from the list whose value is equal to `x`.
   ```python
   fruits = ['orange', 'apple', 'pear', 'banana']
   fruits.remove('pear')
   print(fruits)
   # Output: ['orange', 'apple', 'banana']
   ```

5. **`list.pop([i])`**
   - Removes and returns the item at the given position in the list. If no index is specified, it removes and returns the last item.
   ```python
   fruits = ['orange', 'apple', 'pear']
   last_fruit = fruits.pop()
   print(last_fruit)
   # Output: 'pear'
   print(fruits)
   # Output: ['orange', 'apple']
   ```

6. **`list.clear()`**
   - Removes all items from the list.
   ```python
   fruits = ['orange', 'apple', 'pear']
   fruits.clear()
   print(fruits)
   # Output: []
   ```

7. **`list.index(x[, start[, end]])`**
   - Returns the zero-based index in the list of the first item whose value is equal to `x`.
   ```python
   fruits = ['orange', 'apple', 'pear', 'banana', 'apple']
   index_apple = fruits.index('apple')
   print(index_apple)
   # Output: 1
   index_apple_after = fruits.index('apple', 2)
   print(index_apple_after)
   # Output: 4
   ```

8. **`list.count(x)`**
   - Returns the number of times `x` appears in the list.
   ```python
   fruits = ['orange', 'apple', 'pear', 'banana', 'apple']
   apple_count = fruits.count('apple')
   print(apple_count)
   # Output: 2
   ```

9. **`list.sort(*, key=None, reverse=False)`**
   - Sorts the items of the list in place.
   ```python
   fruits = ['orange', 'apple', 'pear', 'banana']
   fruits.sort()
   print(fruits)
   # Output: ['apple', 'banana', 'orange', 'pear']
   ```

10. **`list.reverse()`**
    - Reverses the elements of the list in place.
    ```python
    fruits = ['orange', 'apple', 'pear']
    fruits.reverse()
    print(fruits)
    # Output: ['pear', 'apple', 'orange']
    ```

11. **`list.copy()`**
    - Returns a shallow copy of the list.
    ```python
    fruits = ['orange', 'apple', 'pear']
    fruits_copy = fruits.copy()
    print(fruits_copy)
    # Output: ['orange', 'apple', 'pear']
    ```

### Practical Example Using Multiple Methods

Let's see an example that uses most of these list methods to understand how they interact:

```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# Counting occurrences
print(fruits.count('apple'))  # Output: 2
print(fruits.count('tangerine'))  # Output: 0

# Finding index
print(fruits.index('banana'))  # Output: 3
print(fruits.index('banana', 4))  # Output: 6

# Reversing the list
fruits.reverse()
print(fruits)  # Output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# Appending an item
fruits.append('grape')
print(fruits)  # Output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

# Sorting the list
fruits.sort()
print(fruits)  # Output: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

# Popping an item
print(fruits.pop())  # Output: 'pear'
print(fruits)  # Output: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
```

### Important Notes

1. **Mutability and Return Values**:
   - Methods like `append`, `extend`, `insert`, `remove`, `clear`, `sort`, and `reverse` modify the list in place and return `None`. This is a design choice to make it clear that these operations modify the original list.

2. **Handling Different Data Types**:
   - Python lists can hold items of different data types, but certain operations like sorting might not work if the elements are not comparable. For example, `[None, 'hello', 10]` cannot be sorted because `None` and `str` can't be compared to `int`.



### Using Lists as Stacks

A stack follows the Last-In, First-Out (LIFO) principle. You can use the `append()` method to add items to the top of the stack and the `pop()` method to remove items from the top.

```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)  # Output: [3, 4, 5, 6, 7]

top = stack.pop()
print(top)    # Output: 7
print(stack)  # Output: [3, 4, 5, 6]

top = stack.pop()
print(top)    # Output: 6
top = stack.pop()
print(top)    # Output: 5
print(stack)  # Output: [3, 4]
```

### Using Lists as Queues

A queue follows the First-In, First-Out (FIFO) principle. Using a list as a queue by appending elements at the end and removing from the beginning can be inefficient, so `collections.deque` is recommended.

```python
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")   # Terry arrives
queue.append("Graham")  # Graham arrives

first = queue.popleft()  # The first to arrive now leaves
print(first)             # Output: 'Eric'
print(queue)             # Output: deque(['John', 'Michael', 'Terry', 'Graham'])

second = queue.popleft()  # The second to arrive now leaves
print(second)             # Output: 'John'
print(queue)              # Output: deque(['Michael', 'Terry', 'Graham'])
```

### List Comprehensions

List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a `for` clause, and then zero or more `for` or `if` clauses.

#### Basic Examples

1. **Creating a list of squares:**
   ```python
   squares = [x**2 for x in range(10)]
   print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   ```

2. **Filtering a list:**
   ```python
   vec = [-4, -2, 0, 2, 4]
   non_negative = [x for x in vec if x >= 0]
   print(non_negative)  # Output: [0, 2, 4]
   ```

3. **Applying a function to each element:**
   ```python
   vec = [-4, -2, 0, 2, 4]
   abs_values = [abs(x) for x in vec]
   print(abs_values)  # Output: [4, 2, 0, 2, 4]
   ```

4. **Calling a method on each element:**
   ```python
   freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
   stripped_fruit = [fruit.strip() for fruit in freshfruit]
   print(stripped_fruit)  # Output: ['banana', 'loganberry', 'passion fruit']
   ```

5. **Creating a list of tuples:**
   ```python
   tuples = [(x, x**2) for x in range(6)]
   print(tuples)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
   ```

6. **Flattening a list:**
   ```python
   vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   flat_list = [num for elem in vec for num in elem]
   print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

7. **Using complex expressions:**
   ```python
   from math import pi
   rounded_pi = [str(round(pi, i)) for i in range(1, 6)]
   print(rounded_pi)  # Output: ['3.1', '3.14', '3.142', '3.1416', '3.14159']
   ```

### Nested List Comprehensions

Nested list comprehensions can be used to perform more complex operations, such as transposing a matrix.

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)  # Output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

This is equivalent to:

```python
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)  # Output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

### Using `zip()` for Transposition

The `zip()` function can also be used for transposing a matrix, which is more efficient and concise.

```python
transposed = list(zip(*matrix))
print(transposed)  # Output: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```


### 5.2. The `del` Statement

The `del` statement in Python is used to remove an item from a list by its index, delete slices from a list, or delete entire variables.

1. **Removing an item by index:**
   ```python
   a = [-1, 1, 66.25, 333, 333, 1234.5]
   del a[0]
   print(a)  # Output: [1, 66.25, 333, 333, 1234.5]
   ```

2. **Removing a slice:**
   ```python
   a = [-1, 1, 66.25, 333, 333, 1234.5]
   del a[2:4]
   print(a)  # Output: [1, 66.25, 1234.5]
   ```

3. **Clearing the entire list:**
   ```python
   a = [-1, 1, 66.25, 333, 333, 1234.5]
   del a[:]
   print(a)  # Output: []
   ```

4. **Deleting an entire variable:**
   ```python
   a = [-1, 1, 66.25, 333, 333, 1234.5]
   del a
   # print(a)  # This would raise a NameError as `a` is deleted
   ```

### 5.3. Tuples and Sequences

Tuples are immutable sequences in Python. They can hold a collection of items and support indexing and slicing similar to lists.

1. **Basic Tuple Operations:**
   ```python
   t = 12345, 54321, 'hello!'
   print(t[0])  # Output: 12345
   print(t)     # Output: (12345, 54321, 'hello!')
   ```

2. **Nesting Tuples:**
   ```python
   u = t, (1, 2, 3, 4, 5)
   print(u)  # Output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
   ```

3. **Immutability:**
   ```python
   t[0] = 88888  # This raises a TypeError: 'tuple' object does not support item assignment
   ```

4. **Tuples with Mutable Objects:**
   ```python
   v = ([1, 2, 3], [3, 2, 1])
   print(v)  # Output: ([1, 2, 3], [3, 2, 1])
   ```

5. **Special Cases for 0 or 1 Item:**
   ```python
   empty = ()
   singleton = 'hello',  # Note the trailing comma
   print(len(empty))     # Output: 0
   print(len(singleton)) # Output: 1
   print(singleton)      # Output: ('hello',)
   ```

6. **Tuple Packing and Unpacking:**
   ```python
   t = 12345, 54321, 'hello!'
   x, y, z = t
   print(x)  # Output: 12345
   print(y)  # Output: 54321
   print(z)  # Output: 'hello!'
   ```

### 5.4. Sets

Sets in Python are unordered collections with no duplicate elements. They support operations like union, intersection, and difference.

1. **Creating Sets and Removing Duplicates:**
   ```python
   basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
   print(basket)  # Output: {'orange', 'banana', 'pear', 'apple'}
   ```

2. **Membership Testing:**
   ```python
   print('orange' in basket)  # Output: True
   print('crabgrass' in basket)  # Output: False
   ```

3. **Set Operations:**
   ```python
   a = set('abracadabra')
   b = set('alacazam')

   print(a)      # Output: {'a', 'r', 'b', 'c', 'd'}
   print(a - b)  # Output: {'r', 'd', 'b'}
   print(a | b)  # Output: {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
   print(a & b)  # Output: {'a', 'c'}
   print(a ^ b)  # Output: {'r', 'd', 'b', 'm', 'z', 'l'}
   ```

4. **Set Comprehensions:**
   ```python
   a = {x for x in 'abracadabra' if x not in 'abc'}
   print(a)  # Output: {'r', 'd'}
   ```

### 5.5. Dictionaries

Dictionaries in Python are a collection of key-value pairs where each key is unique. They are sometimes referred to as associative arrays or hash maps in other programming languages. 

**Key Characteristics of Dictionaries:**
- **Keys must be immutable:** This means you can use strings, numbers, or tuples as dictionary keys, but not lists or other dictionaries.
- **Values can be of any type:** Values associated with keys can be any Python object.
- **Order of elements:** From Python 3.7 onwards, dictionaries maintain the insertion order of keys.

#### Basic Dictionary Operations

1. **Creating a Dictionary:**
   ```python
   tel = {'jack': 4098, 'sape': 4139}
   print(tel)
   # Output: {'jack': 4098, 'sape': 4139}
   ```

2. **Adding an Item:**
   ```python
   tel['guido'] = 4127
   print(tel)
   # Output: {'jack': 4098, 'sape': 4139, 'guido': 4127}
   ```

3. **Accessing a Value:**
   ```python
   print(tel['jack'])
   # Output: 4098
   ```

4. **Deleting an Item:**
   ```python
   del tel['sape']
   print(tel)
   # Output: {'jack': 4098, 'guido': 4127}
   ```

5. **Listing All Keys:**
   ```python
   print(list(tel))
   # Output: ['jack', 'guido']
   ```

6. **Sorting Keys:**
   ```python
   print(sorted(tel))
   # Output: ['guido', 'jack']
   ```

7. **Checking Key Existence:**
   ```python
   print('guido' in tel)
   # Output: True
   print('jack' not in tel)
   # Output: False
   ```

#### Constructing Dictionaries

1. **Using `dict()` with Key-Value Pairs:**
   ```python
   d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
   print(d)
   # Output: {'sape': 4139, 'guido': 4127, 'jack': 4098}
   ```

2. **Using Dictionary Comprehensions:**
   ```python
   d = {x: x**2 for x in (2, 4, 6)}
   print(d)
   # Output: {2: 4, 4: 16, 6: 36}
   ```

3. **Using Keyword Arguments:**
   ```python
   d = dict(sape=4139, guido=4127, jack=4098)
   print(d)
   # Output: {'sape': 4139, 'guido': 4127, 'jack': 4098}
   ```

#### 5.6. Looping Techniques

1. **Looping Through Dictionaries:**
   ```python
   knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   for k, v in knights.items():
       print(k, v)
   # Output:
   # gallahad the pure
   # robin the brave
   ```

2. **Looping with `enumerate()`:**
   ```python
   for i, v in enumerate(['tic', 'tac', 'toe']):
       print(i, v)
   # Output:
   # 0 tic
   # 1 tac
   # 2 toe
   ```

3. **Looping with `zip()`:**
   ```python
   questions = ['name', 'quest', 'favorite color']
   answers = ['lancelot', 'the holy grail', 'blue']
   for q, a in zip(questions, answers):
       print(f'What is your {q}?  It is {a}.')
   # Output:
   # What is your name?  It is lancelot.
   # What is your quest?  It is the holy grail.
   # What is your favorite color?  It is blue.
   ```

4. **Looping in Reverse:**
   ```python
   for i in reversed(range(1, 10, 2)):
       print(i)
   # Output:
   # 9
   # 7
   # 5
   # 3
   # 1
   ```

5. **Looping in Sorted Order:**
   ```python
   basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   for fruit in sorted(basket):
       print(fruit)
   # Output:
   # apple
   # apple
   # banana
   # orange
   # orange
   # pear
   ```

6. **Looping with Unique Elements:**
   ```python
   basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   for fruit in sorted(set(basket)):
       print(fruit)
   # Output:
   # apple
   # banana
   # orange
   # pear
   ```

7. **Filtering While Looping:**
   ```python
   import math
   raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
   filtered_data = [value for value in raw_data if not math.isnan(value)]
   print(filtered_data)
   # Output: [56.2, 51.7, 55.3, 52.5, 47.8]
   ```




### 5.7. More on Conditions

Conditions in Python can use a variety of operators, including comparison operators, Boolean operators, and membership operators. Let's explore these with examples.

##### Comparison Operators
- `in` and `not in`: Check for membership.
- `is` and `is not`: Compare identity (whether two objects are the same).

```python
# Membership test
fruits = ['apple', 'orange', 'banana']
print('apple' in fruits)      # Output: True
print('grape' not in fruits)  # Output: True

# Identity test
a = b = [1, 2, 3]
c = [1, 2, 3]
print(a is b)  # Output: True
print(a is c)  # Output: False
```

##### Chained Comparisons
- You can chain comparisons to create a more complex condition.

```python
a = 2
b = 3
c = 3
print(a < b == c)  # Output: True
```

##### Boolean Operators
- `and`, `or`, and `not`: Combine multiple conditions.
- Short-circuit evaluation: Stops evaluating as soon as the outcome is determined.

```python
A = True
B = False
C = True

print(A and B or C)         # Output: True
print((A and (not B)) or C) # Output: True (equivalent to above)

# Short-circuit evaluation
print(A and B and C)  # Output: False (B is False, so C is not evaluated)
```

##### Assignment with Boolean Expressions
- You can assign the result of a comparison or Boolean expression to a variable.

```python
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)  # Output: 'Trondheim'
```

##### Walrus Operator (`:=`)
- Assign a value within an expression.

```python
if (n := len(fruits)) > 2:
    print(f"List has {n} elements.")
# Output: List has 3 elements.
```

#### 5.8. Comparing Sequences and Other Types

Sequences in Python can be compared lexicographically, meaning they are compared element by element.

##### Lexicographical Ordering
- Sequences are compared element by element until a difference is found.

```python
print((1, 2, 3) < (1, 2, 4))        # Output: True
print([1, 2, 3] < [1, 2, 4])        # Output: True
print('ABC' < 'C' < 'Pascal' < 'Python')  # Output: True
print((1, 2, 3, 4) < (1, 2, 4))     # Output: True
print((1, 2) < (1, 2, -1))          # Output: True
print((1, 2, 3) == (1.0, 2.0, 3.0)) # Output: True
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))  # Output: True
```

##### Mixed Type Comparisons
- Mixed numeric types can be compared based on their numeric value.

```python
print(0 == 0.0)  # Output: True
```

- Comparing incompatible types results in a `TypeError`.

```python
try:
    print(0 < 'apple')
except TypeError as e:
    print(e)  # Output: '<' not supported between instances of 'int' and 'str'
```

### Examples of Condition and Comparison Usage

1. **Chained Comparisons:**
   ```python
   a = 5
   b = 10
   c = 10
   print(a < b == c)  # Output: True
   ```

2. **Boolean Operators with Short-circuit Evaluation:**
   ```python
   A = True
   B = False
   C = True
   print(A and B or C)  # Output: True
   ```

3. **Assigning with Boolean Expressions:**
   ```python
   string1, string2, string3 = '', 'Hello', 'World'
   result = string1 or string2 or string3
   print(result)  # Output: 'Hello'
   ```

4. **Walrus Operator Usage:**
   ```python
   fruits = ['apple', 'banana', 'cherry']
   if (n := len(fruits)) > 2:
       print(f"List has {n} elements.")
   # Output: List has 3 elements.
   ```

5. **Lexicographical Comparison:**
   ```python
   print([1, 2, 3] < [1, 2, 4])  # Output: True
   print('abc' < 'abcd')         # Output: True
   ```
