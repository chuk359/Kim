#Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.
from tkinter import S


class Solution:
    def lengthOfLastWord(s):
        s1 = s.split()
        x = len(s1[-1])
        return x

print(Solution.lengthOfLastWord('Hello World'))