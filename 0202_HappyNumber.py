""" 
寫一個演算法, 判斷整數n是否為happy number
happy number具備以下:
    該數字的每一位數平方後相加得到新的數值, 重複步驟, 最終得到數字1, 即為快樂數
"""
import time

class Solution:
    def isHappy(self, n: int) -> bool:
        history = []
        while n != 1:
            result = 0
            for char in str(n):
                result += int(char) * int(char)
            
            if result in history:
                return False
            else:
                history.append(result)
                n = result
        return True

def test_case_run():
    n = 19
    result = Solution.isHappy(Solution, n)
    print(result)
    n = 2
    result = Solution.isHappy(Solution, n)
    print(result)
    n = 1111111
    result = Solution.isHappy(Solution, n)
    print(result)
    n = pow(2, 31) -1
    result = Solution.isHappy(Solution, n)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= n <= 2^31 - 1
"""

""" 
思路:
1. 難點在判斷是否進入迴圈狀態, 不能使用單純的遞迴來完成
"""