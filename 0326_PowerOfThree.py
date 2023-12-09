""" 
判斷整數n是否為3的x次方
Follow up: 不使用遞迴或loop
"""
import time

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return ((1162261467 % n) == 0) if n > 0 else False

def test_case_run():
    n = 27
    result = Solution.isPowerOfThree(Solution, n)
    print(result)
    n = 0
    result = Solution.isPowerOfThree(Solution, n)
    print(result)
    n = -1
    result = Solution.isPowerOfThree(Solution, n)
    print(result)
    n = 81
    result = Solution.isPowerOfThree(Solution, n)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
-2^31 <= n <= 2^31 - 1
"""

""" 
思路:
1. 3的x次方永遠不可能為負數及0
2. 題目限制範圍中最大的3的x次方數值是1162261467, 所有比這個小的3的x次方值都可以整除他
3. 判斷1162261467除n的餘數是否為0即可得知是否為3的x次方值
"""