#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(accounts) -> int:
        max_wealth = 0
        for account in accounts:
            curr_account_wealth = sum(account)
            if curr_account_wealth > max_wealth:
                max_wealth=curr_account_wealth                
        return max_wealth
    
print(Solution.maximumWealth([[1,2,3],[3,2,1]]))