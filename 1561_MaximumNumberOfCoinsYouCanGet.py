'''
有3n堆不同數量的硬幣
1. 你每一次任意選三堆硬幣(不一定連續)
2. 從你選的三堆硬幣中, Alice會拿最多硬幣的那一堆
3. 你會拿取那堆硬幣中第二多的硬幣堆
4. Bob會拿取最後一堆
5. 重複循環直到全部硬幣分完

回傳你能取得的最大數值硬幣
'''

class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        result = 0
        sorted_piles = sorted(piles)
        for loop_cnt in range((len(piles) // 3)):
            max_index = len(sorted_piles)-1
            secondary_coins_index_this_loop = max_index-loop_cnt*2-1
            result += sorted_piles[secondary_coins_index_this_loop]
        return result
    
piles = [2,4,1,2,7,8]
result = Solution.maxCoins(Solution, piles)
print(result, "(expected value: 9)")
    
piles = [2,4,5]
result = Solution.maxCoins(Solution, piles)
print(result, "(expected value: 4)")
    
piles = [9,8,7,6,5,1,2,3,4]
result = Solution.maxCoins(Solution, piles)
print(result, "(expected value: 18)")

'''
思路:
1. 因為只能取得第二高數量, 最佳狀況是在全部硬幣堆中前兩高同時被隨機選中
2. 下一波, 選中第三第四高, 下一波...
3. 排序piles來取得所需的前兩高數字
'''