""" 
給予一個數列prices, 內容代表股票在第i天的價格
只能在單獨一天買一張股票然後選擇另一天賣掉
回傳可能的最大收益, 如果沒有收益, 回傳0
"""
import time

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)
        return max_profit

def test_case_run():
    prices = [7,1,5,3,6,4]
    result = Solution.maxProfit(Solution, prices)
    print(result)
    prices = [7,6,4,3,1]
    result = Solution.maxProfit(Solution, prices)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

""" 
思路:
1. 由左向右, 根據最低買入值和當天賣出值, 輪流比較找出最高收益 O(n)
"""