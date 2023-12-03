""" 
給予一個n大小的陣列nums, 回傳主要元素, 主要元素會出現n/2次數以上

Follow-up: linear time, O(1) space
"""
import time

class Solution:
    # O(N logN)
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums)//2]
    
    # time O(n), space O(1)
    # (https://leetcode.com/problems/majority-element/solutions/1788112/python-easy-solution-o-n-o-1-explained/)
    def majorityElement(self, nums: list[int]) -> int:
        major = nums[0]
        count = 1
        
        for num in nums[1:]:
            count += 1 if num == major else -1
            if count <= 0:
                major = num
                count = 1
        return major

def test_case_run():
    nums = [3,2,3]
    result = Solution.majorityElement(Solution, nums)
    print(result)
    nums = [2,2,1,1,1,2,2]
    result = Solution.majorityElement(Solution, nums)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
"""

""" 
思路:
1. 因為主要元素會出現在總數一半以上
2. 將nums排序後, 取中間值必然會是主要元數
"""