#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
#Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#Return k after placing the final result in the first k slots of nums.

class Solution:
    def removeElement(nums, val):
        newnums = []
        k=0
        for num in nums:
            if num == val:
                pass
            else:
                newnums.append(num)
                k+=1
        nums[:k]=newnums
        nums[k:]=["_" for items in nums[k:]]
        return k, nums

    
print(Solution.removeElement([3,2,2,3],3))