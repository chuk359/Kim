#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
class Solution:
    def twoSum(nums, target):
        def __init__(self):
            twoSum = []
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return (i,j)

print(Solution.twoSum((1,2,3,4,5),6))