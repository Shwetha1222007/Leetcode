class Solution(object):
    def maximizeSum(self, nums, k):
        score = 0
        maximum = max(nums)

        for i in range(k):
            score += maximum
            maximum += 1

        return score