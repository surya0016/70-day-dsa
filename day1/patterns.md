# Python Patterns Used in Day 1 DSA Problems

## Pattern 1: Loop with Index
```python
for i in range(len(arr)):
    print(arr[i])
```
**Explanation:** Used when you need the index position to access or modify elements. Common in problems where you need to know the position of elements.

**Used in:** All three main problems (candies, running sum, richest customer)

---

## Pattern 2: Loop without Index
```python
for num in arr:
    sum += num
```
**Explanation:** Cleaner syntax when you only need the value, not the index. More Pythonic and readable.

**Used in:** practice.py sum_of_all_elements function

---

## Pattern 3: Initialize Empty List
```python
output = []
result = []
```
**Explanation:** Start with an empty list when building results dynamically. Use append() to add elements as you process data.

**Used in:** All problems to store results

---

## Pattern 4: List Append (Building Results)
```python
result.append(value)
```
**Explanation:** Add elements to the end of a list one at a time. Efficient for building results iteratively.

**Used in:** All problems for collecting output values

---

## Pattern 5: Find Max Value in Array
```python
max_val = 0
for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
```
**Explanation:** Track the maximum value seen so far by comparing each element. Initialize with 0 or first element depending on constraints.

**Used in:** kids-with-candies (finding greatest candy count), practice.py max_element function

---

## Pattern 6: Accumulator/Running Sum
```python
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]
    result.append(sum)
```
**Explanation:** Keep a running total that accumulates values as you iterate. Essential for prefix sum problems.

**Used in:** running-sum-of-1d-array problem

---

## Pattern 7: Nested Loops for 2D Arrays
```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
```
**Explanation:** Outer loop iterates rows, inner loop iterates columns. Used to process every element in a 2D array.

**Used in:** richest-customer-wealth problem

---

## Pattern 8: 2D Array Access
```python
value = matrix[row][col]
```
**Explanation:** Access 2D array elements using double indexing. First index is row, second is column.

**Used in:** richest-customer-wealth problem

---

## Pattern 9: Conditional List Building
```python
for i in range(len(arr)):
    if condition:
        result.append(True)
    else:
        result.append(False)
```
**Explanation:** Build a list of boolean values or any conditional results based on element-by-element checks.

**Used in:** kids-with-candies problem

---

## Additional Useful Patterns (Not Yet Used)

### Pattern 10: Loop with Enumerate
```python
for i, num in enumerate(arr):
    print(i, num)
```
**Explanation:** Get both index and value simultaneously. More Pythonic than range(len(arr)).

---

### Pattern 11: Swap Two Elements
```python
arr[i], arr[j] = arr[j], arr[i]
```
**Explanation:** Python's tuple unpacking allows swapping without a temp variable. Very useful in sorting algorithms.

---

### Pattern 12: Initialize Array with Default Values
```python
arr = [0] * n          # [0, 0, 0, ... n times]
matrix = [[0]*cols for _ in range(rows)]  # 2D array
```
**Explanation:** Pre-allocate arrays with default values. Note: Use list comprehension for 2D arrays to avoid reference issues.

---

## Tips & Best Practices

1. **Choose the right loop:** Use `for item in arr` when you don't need the index, use `for i in range(len(arr))` when you do.

2. **Enumerate is your friend:** When you need both index and value, `enumerate()` is cleaner than `range(len())`.

3. **List comprehensions:** Can make code more concise for simple transformations (learn this next!).

4. **Watch out for 2D array initialization:** Never use `[[0]*cols]*rows` - it creates references to the same list!

5. **Time complexity awareness:** Nested loops = O(n²), single loop = O(n). Be mindful of performance.
