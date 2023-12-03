""" 

"""
import time

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return
        
        m -= 1
        n -= 1
        for i in reversed(range(len(nums1))):
            if m < 0:
                nums1[i] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[i] = nums1[m]
                m -= 1
            else:
                if nums1[m] >= nums2[n]:
                    nums1[i] = nums1[m]
                    m -= 1
                else:
                    nums1[i] = nums2[n]
                    n -= 1
        return
    
    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
        
def test_case_run():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution.merge2(Solution, nums1, m, nums2, n)
    print(nums1)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
"""

""" 
思路:
1. 從最末端開始填, 將兩數組最大值填入, 依序往前比較
"""