# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0 or x % 10 == 0:
            if x == 0:
                return True
            else:
                return False
        else:
            reversedX = 0
            while x > reversedX:
                reversedX = reversedX * 10 + x % 10
                x = x // 10
            if x == reversedX or x == reversedX // 10:
                return True 
            else:
                return False
print(Solution.isPalindrome(121))