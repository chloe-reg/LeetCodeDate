""" 

"""
import time

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for i in range(len(columnTitle)):
            number *= 26
            number += ord(columnTitle[i]) - ord('A') + 1
        return number

def test_case_run():
    columnTitle = "A"
    result = Solution.titleToNumber(Solution, columnTitle)
    print(result) # 1
    columnTitle = "AB"
    result = Solution.titleToNumber(Solution, columnTitle)
    print(result) # 28
    columnTitle = "ZY"
    result = Solution.titleToNumber(Solution, columnTitle)
    print(result) # 701
    columnTitle = "FXSHRXW"
    result = Solution.titleToNumber(Solution, columnTitle)
    print(result) # 2147483647
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""

""" 
思路:
1. 26進位計算法
2. 用ascii code換算出字母代表的數值
"""