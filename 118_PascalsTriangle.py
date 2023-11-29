""" 
給予一個整數數字,回傳該數字Pascal's triangle數列
"""
import time

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        for i in range(numRows):
            rows = []
            for j in range(i+1):
                if j-1 < 0 or j+1 > i:
                    rows.append(1)
                else:
                    rows.append(result[i-1][j-1]+result[i-1][j])
            result.append(rows)
        return result

def test_case_run():
    numRows = 5
    result = Solution.generate(Solution, numRows)
    print(result)
    numRows = 1
    result = Solution.generate(Solution, numRows)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= numRows <= 30
"""

""" 
思路:
1. 單純考慮Pascal's triangle數列計算方式
"""