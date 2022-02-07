#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(n):
        ways = 0
        ways1 = 1
        ways2 = 2
        if n < 3:
            return n 
        else:
            for i in range(2,n):
                ways = ways1+ways2
                ways1 = ways2
                ways2 = ways
        return ways