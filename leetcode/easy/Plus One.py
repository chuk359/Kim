#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(digits):
        i = -1
        digits[i] += 1
        while digits[i] > 9:
            if digits[0] > 9:
                digits.insert(0, 1)
                digits[i] = 0  
            else:
                digits[i] = 0
                digits[i-1] +=1
                i -= 1
        return digits
    
print(Solution.plusOne([9,9,9]))
