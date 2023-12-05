""" 
回傳n中bit為1的數量
"""
import time

class Solution:
    def hammingWeight(self, n: int) -> int:
        return 0 if n == 0 else (n & 1) + self.hammingWeight(self, n>>1)

def test_case_run():
    n = 0b00000000000000000000000000001011
    result = Solution.hammingWeight(Solution, n)
    print(result)
    n = 0b00000000000000000000000010000000
    result = Solution.hammingWeight(Solution, n)
    print(result)
    n = 0b11111111111111111111111111111101
    result = Solution.hammingWeight(Solution, n)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The input must be a binary string of length 32.
"""

""" 
思路:
1. 判斷最後1 bit是否為1, 剩下的向右位移1送進去遞迴, 直到n=0
"""