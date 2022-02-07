#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

class Solution:
    def isValid(s):
        matches = ['()','[]','{}']
        l = []
        for i in s:
            if l and l[-1] + i in matches:
                l.pop()
            else:
                l.append(i)
        if not l:
            return True
        else:
            return False      
        
  
print(Solution.isValid("({[]})"))