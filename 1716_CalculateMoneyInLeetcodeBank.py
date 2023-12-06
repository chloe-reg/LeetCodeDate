""" 
星期一到星期日每天存入1~7塊錢
下個星期基礎值增加一塊, 一到日存入2~8塊錢
從星期一開始直到第n天, 回傳所存的金額
"""
import time

class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        for i in range(n):
            week = i // 7
            money += 1 + i % 7 + week
        return money

def test_case_run():
    n = 4
    result = Solution.totalMoney(Solution, n)
    print(result)
    n = 10
    result = Solution.totalMoney(Solution, n)
    print(result)
    n = 20
    result = Solution.totalMoney(Solution, n)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= n <= 1000
"""

""" 
思路:
1. week數即為offset, 星期一到日所存的錢 = offset + 1~7
"""