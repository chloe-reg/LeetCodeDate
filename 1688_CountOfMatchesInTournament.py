""" 
給定參賽隊伍的數量 n, 返回比賽期間進行的比賽數量
一場比賽中, 兩隊參賽, 只有一隊能夠獲勝
"""
import time

class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n >= 2:
            matchs = n // 2
            result += matchs
            n = n - matchs
        return result

def test_case_run():
    n = 7
    result = Solution.numberOfMatches(Solution, n)
    print(result)
    n = 14
    result = Solution.numberOfMatches(Solution, n)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= n <= 200
"""

""" 
思路:
1. 至少有兩組以上存活時, 會進行比賽
2. 每次比賽兩兩一賽場, matchs = n // 2, 此時如果剩下奇數隊伍可能會剩下一組沒有被匹配到
3. 存活的隊伍 n = n - matchs
"""