#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(nums):
        s = 0
        maxS = 0
        for i in range(len(nums)):
            maxS += nums[i]
        for i in range(len(nums)):
            if s>= 0:
                s += nums[i]
            else:
                s = nums[i]
            if s > maxS:
                maxS = s
        return maxS
print(Solution.maxSubArray([5,4,-1,7,8]))