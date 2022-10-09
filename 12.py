prices = [7,1,5,3,6,4]

left_lowest = []
lowest = prices[0]
for i in range(len(prices)):
    if prices[i] < lowest:
        lowest = prices[i]
    left_lowest.append(lowest)

highest = prices[-1]
for j in range(len(prices)-1, -1, -1):
    if prices[j] > highest:
        highest = prices[j]
    left_lowest[j] = highest-left_lowest[j]

result = left_lowest

print(max(result))

#######################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_lowest = []
        lowest = prices[0]
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            left_lowest.append(lowest)

        highest = prices[-1]
        for j in range(len(prices)-1, -1, -1):
            if prices[j] > highest:
                highest = prices[j]
            left_lowest[j] = highest-left_lowest[j]

        result = left_lowest
        
        return max(result)

'''
Runtime: 2322 ms, faster than 30.41% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 24.6 MB, less than 96.55% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''

############

prices = [7,1,5,3,6,4]

result = 0
minimum = prices[0]

for price in prices:
    minimum = min(price, minimum)
    result = max(price-minimum, result)

print(result)