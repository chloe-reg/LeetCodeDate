""" 
給予一個非負數整數x, 回傳其根號值(無條件捨去到整數)
不要使用內建函式 ex pow(x,0.5)in c++ or x ** 0.5 in python
"""
import time

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 0
        right = x
        while left <= right:
            mid = left + ((right - left) // 2)
            if mid * mid <= x:
                if (mid+1) * (mid+1) > x:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1 
        return right

def test_case_run():
    x = 4
    result = Solution.mySqrt(Solution, x)
    print(result)
    x = 8
    result = Solution.mySqrt(Solution, x)
    print(result)
    x = 10501
    result = Solution.mySqrt(Solution, x)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
0 <= x <= 2^31 - 1
"""

""" 
思路:
1. 用二分法逼近O(log(n))
2. 因為無條件捨去到整數, 當 y^2<=x<(y+1)^2 成立時, 答案為y
"""