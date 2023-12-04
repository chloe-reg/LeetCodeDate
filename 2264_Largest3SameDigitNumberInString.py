""" 
有一個num的字串表示一個大整數
找出最大的num中連續三個相同的數字
"""
import time

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = -1
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                result = max(result,int(num[i]))
        return "" if result == -1 else str(result)*3

def test_case_run():
    num = "6777133339"
    result = Solution.largestGoodInteger(Solution, num)
    print(result)
    num = "2300019"
    result = Solution.largestGoodInteger(Solution, num)
    print(result)
    num = "42352338"
    result = Solution.largestGoodInteger(Solution, num)
    print(result)
    num = "666528888"
    result = Solution.largestGoodInteger(Solution, num)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
3 <= num.length <= 1000
num only consists of digits.
"""

""" 
思路:
1. 連續三個位置比較
2. 相同的話取出數字和result比較, 比result大則取代
"""