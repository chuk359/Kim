#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(nums, target):
        if nums[-1] < target:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                elif nums[i] < target and nums[i+1] > target:
                    return i+1
                elif nums[i] > target:
                    return 0
                
print(Solution.searchInsert((1,2,3,4,5),0))