""" 
Follow up: O(1) extra space complexity and O(n) runtime complexity
"""
import time

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        return 0
    
    def missingNumber2(self, nums: list[int]) -> int:
        expect_sum = sum(range(len(nums)+1))
        sum_of_nums = sum(nums)
        return expect_sum-sum_of_nums

def test_case_run():
    nums = [3,0,1]
    result = Solution.missingNumber(Solution, nums)
    print(result)
    nums = [0,1]
    result = Solution.missingNumber(Solution, nums)
    print(result)
    nums = [9,6,4,2,3,5,7,0,1]
    result = Solution.missingNumber(Solution, nums)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
"""

""" 
思路:
1. 逐一判斷數字是否在字串中

1. 分別計算預期和實際的加總數值, 相減後即為缺失的數字 
"""