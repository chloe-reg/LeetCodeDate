""" 
給予數字字串num, 找到最大的奇數子字串
"""
import time

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 != 0:
                return num[:i+1]
        return ""
    
    def largestOddNumber2(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if num[i] in "13579":
                return num[:i+1]
        return ""

def test_case_run():
    num = "52"
    result = Solution.largestOddNumber2(Solution, num)
    print(result)
    num = "4206"
    result = Solution.largestOddNumber2(Solution, num)
    print(result)
    num = "35427"
    result = Solution.largestOddNumber2(Solution, num)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.
"""

""" 
思路:
1. 從最後一位往前判斷是否為奇數
2. 為奇數的話, 則從第0位到該位為最大的奇數子字串
"""