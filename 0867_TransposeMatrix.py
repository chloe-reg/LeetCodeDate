""" 
轉置矩陣
"""
import time

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        result = []
        for i in range(n):
            result.append([0]*m)
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]
        return result

def test_case_run():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = Solution.transpose(Solution, matrix)
    print(result)
    matrix = [[1,2,3],[4,5,6]]
    result = Solution.transpose(Solution, matrix)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
-10^9 <= matrix[i][j] <= 10^9
"""

""" 
思路:

"""