from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = 0 
        opt = []
        for i in range(len(nums)):
            n = n + nums[i]
            opt.append(n)
    
        return opt
