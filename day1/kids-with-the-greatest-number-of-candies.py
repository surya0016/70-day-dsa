from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        greatest_value = 0
        for i in range(len(candies)):
            if candies[i] > greatest_value:
                greatest_value = candies[i]
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest_value:
                output.append(True)        
            else:
                output.append(False)
