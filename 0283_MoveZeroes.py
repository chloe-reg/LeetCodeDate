""" 
將nums中的0移到末端, 保持原有的數字順序
"""
import time

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        index = 0
        index_check = 0
        while index_check < len(nums):
            if nums[index_check] != 0:
                nums[index] = nums[index_check]
                index += 1
            index_check += 1
        nums[index:] = [0]*(len(nums)-index)
        return

def test_case_run():
    nums = [0,1,0,3,12]
    Solution.moveZeroes(Solution, nums)
    print(nums)
    nums = [0]
    Solution.moveZeroes(Solution, nums)
    print(nums)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""

""" 
思路:
1. 把非0的數字依序往前放, 放完全部非0數字後, 將其後的所有位置歸0
"""