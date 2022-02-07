#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
class Solution:
    def romanToInt(s) -> int:
        num = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
        result = 0
        for i in range (len(s)-1):
            if num[s[i]] >= num[s[i+1]]:           
                result += num[s[i]]
            else:
                result -= num[s[i]] 
        result += num[s[-1]]
        return result
print(Solution.romanToInt('MCMXCIV'))