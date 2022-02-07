# Given two binary strings a and b, return their sum as a binary string.
class Solution:
    def addBinary(a, b):
        return bin(sum([int(a, 2), int(b, 2)]))[2:]

