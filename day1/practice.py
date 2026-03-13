from typing import List

# Write a function that takes a list and prints each element with its index
sample_list = ['a', 'b', 'c', 'd', 'e']
for i in range(len(sample_list)):
  print(sample_list[i], i)

# Write a function that returns the sum of all elements
def sum_of_all_elements(arr:List[int]):
  sum = 0
  for i in arr:
    sum = sum + i
  return sum

print(sum_of_all_elements([1, 2, 3, 4 ,5]))

# Write a function that returns the max element (without using max())
def max_element(arr:List[int])->int:
  max = 0
  for i in range(len(arr)):
    if arr[i] > max:
      max = arr[i]
  return max
    
print(max_element([1, 2, 3, 4 ,5]))