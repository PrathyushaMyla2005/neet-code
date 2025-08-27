'''1. Problem Statement:

You are given an array prices[] where prices[i] = price of a stock on the ith day.
You need to maximize profit by choosing a single day to buy and a single day to sell in the future.

If no profit is possible, return 0.

👉 Example:

Input: prices = [7,1,5,3,6,4]  
Output: 5  
Explanation: Buy at price 1 and sell at price 6 → profit = 6 - 1 = 5

2. Approaches
Approach 1: Brute Force

Try all pairs (buy, sell) such that buy < sell.

Calculate profit and keep track of maximum.
T.C.: O(n²) (two loops → not efficient for large input)
S.C.: O(1)'''
def stock_day(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):
        for j in range(i+1,n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit,profit)
    return max_profit
prices = [7,1,5,6,8]
print(stock_day(prices))
'''pproach 2: Optimal (Single Pass)

Idea: Keep track of minimum price so far while iterating.

At each day, calculate profit if sold today = price - min_price.

Update max profit accordingly.

👉 This is efficient because we only scan once.
4. Complexity Analysis

Time Complexity (T.C.):

Brute Force: O(n²)

Optimal: O(n) (single loop)

Space Complexity (S.C.):

Both approaches: O(1) (no extra data structures)'''
def maxProfit(prices):
    min_price = float('inf')   # very large to start
    max_profit = 0             # no profit initially
    
    for price in prices:
        if price < min_price:     # update minimum buying price
            min_price = price
        profit = price - min_price
        if profit > max_profit:   # update maximum profit
            max_profit = profit
            
    return max_profit
prices=[7,2,1,5,9]
print(stock_day(prices))
#using two pointer
'''omplexity

Time Complexity (T.C): O(n) → One pass through prices.

Space Complexity (S.C): O(1) → Only variables.

✅ Why Two Pointer Approach?

We avoid unnecessary comparisons (O(n²)).

By maintaining the lowest buying price and checking profit on-the-fly, we get the result in'''
def stock_day(prices):
    j =1
    i =0
    max_profit =0
    while j < len(prices):
        if prices[j] > prices[i] :
            profit = prices[j] - prices[i]
            max_profit = max(max_profit,profit)
        else:
            i = j
        j += 1
    return max_profit
prices = [7,1,5,3,6,4]
print(stock_day(prices))
