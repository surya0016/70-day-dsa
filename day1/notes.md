
📝 Python List Notes

1. **Python list methods:**
    - `append(x)`: Adds item `x` to the end of the list.
       - Example: `arr = [1, 2]; arr.append(3)  # arr = [1, 2, 3]`
    - `pop([i])`: Removes and returns item at index `i` (default last item).
       - Example: `arr = [1, 2, 3]; arr.pop()  # returns 3, arr = [1, 2]`
    - `insert(i, x)`: Inserts item `x` at index `i`.
       - Example: `arr = [1, 3]; arr.insert(1, 2)  # arr = [1, 2, 3]`
    - `remove(x)`: Removes the first occurrence of item `x`.
       - Example: `arr = [1, 2, 3, 2]; arr.remove(2)  # arr = [1, 3, 2]`
    - `len(arr)`: Returns the number of items in the list.
       - Example: `arr = [1, 2, 3]; len(arr)  # returns 3`

2. **List slicing:** `arr[start:end:step]`
    - Returns a new list from index `start` to `end-1`, stepping by `step`.
    - Example: `arr = [0, 1, 2, 3, 4, 5]`
       - `arr[1:4]` gives `[1, 2, 3]`
       - `arr[:3]` gives `[0, 1, 2]`
       - `arr[::2]` gives `[0, 2, 4]`

3. **List comprehension:** `[expression for item in iterable]`
    - Creates a new list by applying `expression` to each `item` in `iterable`.
    - Example: `arr = [1, 2, 3]`
       - `[x*2 for x in arr]` gives `[2, 4, 6]`