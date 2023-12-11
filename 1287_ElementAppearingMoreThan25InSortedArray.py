""" 
找出在一個以排序的list中出現超過25%的元素
"""
import time

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        len_25p = len(arr) // 4
        count = 1
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                count += 1
            else:
                count = 1
            
            if count > len_25p:
                return arr[i]
        return arr[0]

def test_case_run():
    arr = [1,2,2,6,6,6,6,7,10]
    result = Solution.findSpecialInteger(Solution, arr)
    print(result)
    arr = [1,1,1,1,2,2,2,2,6,6,6,6,6,7,10]
    result = Solution.findSpecialInteger(Solution, arr)
    print(result)
    arr = [1,1]
    result = Solution.findSpecialInteger(Solution, arr)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""

""" 
思路:
1. 計算相同的數量大於1/4
"""