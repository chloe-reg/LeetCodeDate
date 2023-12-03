""" 
左右翻轉32bit所得的unsigned integer
"""
import time

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result += (n>>i & 1) * pow(2, 32-1-i)
        return result
    
    def reverseBits2(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

def test_case_run():
    n = 0b00000010100101000001111010011100
    result = Solution.reverseBits(Solution, n)
    print(result)
    n = 0b11111111111111111111111111111101
    result = Solution.reverseBits(Solution, n)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
The input must be a binary string of length 32
"""

""" 
思路:
1. 取得各個bit值, 並反向計算二進位order

1. 不用乘法計算, 以位移結合and or運算子
"""