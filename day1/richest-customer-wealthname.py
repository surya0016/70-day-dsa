from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []

        for i in range(len(accounts)):
            n = 0
            for j in range(len(accounts[i])):
                n = n + accounts[i][j]
            wealth.append(n)

        val = 0
        for i in range(len(wealth)):
            if wealth[i] > val:
                val = wealth[i]
        return val
