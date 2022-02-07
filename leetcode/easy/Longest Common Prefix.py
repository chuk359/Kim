#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(strs):
        prefix = strs[0]
        s = 1
        f = 201
        while s < f:
            m = s + (f-s)//2
            if not all([s.find(prefix[:m]) == 0 for s in strs]):
                f = m
            else:
                s = m + 1
        print(prefix)
        return prefix[:s-1]
print(Solution.longestCommonPrefix(["flower","flow","flight"]))
print(Solution.longestCommonPrefix(["dog","racecar","car"]))